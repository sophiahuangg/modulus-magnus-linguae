import requests, langcodes, gzip, csv, pandas as pd
from bs4 import BeautifulSoup
from transformers import BertTokenizer

url = "https://link.springer.com/article/10.1007/s10579-014-9287-y/tables/1"
response = requests.get(url)

table = BeautifulSoup(response.content, "html.parser").find("table", class_="data last-table")

fulllang = []
for row in table.tbody.find_all("tr"):
    lang = row.find_all("td")
    if lang[0].b is not None:
        fulllang.append(lang[0].text.strip())

print("full languages=", fulllang)
print("num =", len(fulllang))
print("========")

# Turn full languages into abbreviations

abbrev = []
for language in fulllang:
    try:
        code = langcodes.find(language)
        abbreviation = code.language
        abbrev.append(abbreviation)
    except:
        pass

print("abbreviations=", abbrev)
print("num=", len(abbrev))

# Tokenizing only the languages above
tokens = BertTokenizer.from_pretrained('bert-base-uncased')

zipfiles = {}

for lang in abbrev:
        ziplink = f'https://opus.nlpl.eu/download.php?f=bible-uedin/v1/mono/{lang}.txt.gz'
        r = requests.get(ziplink)
        print("ziplink=", ziplink)
        try:
            uncompressed = gzip.decompress(r.content).decode()
            zipfiles[lang] = uncompressed	
        except:
            print("Dataset doesn't exist for {lang}")
with open('bibleTextToken.csv', 'w', newline ='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Language', 'Token Length'])
	for lang, text in zipfiles.items():
		tokenize = tokens.encode(text)
		tokenlength = len(tokenize)
		writer.writerow([lang, tokenlength])
