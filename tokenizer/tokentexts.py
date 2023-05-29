import requests, gzip, csv
import pandas as pd
from bs4 import BeautifulSoup 
from transformers import BertTokenizer

url = "https://opus.nlpl.eu/bible-uedin.php"
response = requests.get(url)

tokens = BertTokenizer.from_pretrained('bert-base-uncased')
print("tokens=", tokens)

soup = BeautifulSoup(response.content, "html.parser")
div_counts = soup.find('div', class_='counts')
if div_counts:
    table = div_counts.find('table')
    if table:
        rows = table.find_all('tr')
        languages = [row.find('th').text.strip() for row in rows]
        languages = languages[1:]
print(languages)

zipfiles = {}

for lang in languages:
	ziplink = f'https://opus.nlpl.eu/download.php?f=bible-uedin/v1/mono/{lang}.txt.gz'
	response = requests.get(ziplink)
	uncompressed = gzip.decompress(response.content).decode()
	zipfiles[lang] = uncompressed

with open('texts.csv', 'w', newline ='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Language', 'Token Length'])
	for lang, text in zipfiles.items():
		tokenize = tokens.encode(text)
		tokenlength = len(tokenize)
		writer.writerow([lang, tokenlength])

df1 = pd.read_csv("HuggingTransformCount.csv")
df2 = pd.read_csv("tiktokenCount.csv")

combined = pd.merge(df2, df1, on = 'Language', how = 'left')
combined.to_csv('finalTokenCount.csv', index=False)
