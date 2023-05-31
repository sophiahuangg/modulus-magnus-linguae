import re, json, os, codecs

file_path = 'quizzes.json'

with open(file_path, 'r') as file:
    js_function = file.read()

# Extracting each json for each chapter
pattern = r'JSON\.parse\((["\'])(.*?)\1\)'

matches = re.findall(pattern, js_function, re.DOTALL)

json_objects = []

# Iterates through each json for each chapter
numerrors = 0
for match in matches:
    try:
        unescaped_str = codecs.decode(match[1], 'unicode_escape')
        json_obj = json.loads(unescaped_str)
        print("json_obj=", json_obj['id'])
        json_objects.append(json_obj)
    except (json.JSONDecodeError, UnicodeDecodeError):
        print("JSON ERROR ON=", match[1])
        numerrors+=1
        pass

print("NUM ERRORS=", numerrors)

directory = "chapterinfo"
if not os.path.exists(directory):
    os.makedirs(directory)

# Creates a json file for each chapter
for chapter in json_objects:
    #print("Chapter id=", chapter['id'])
    # Naming as Chapter ID + 1 because ID starts at 0 (i.e. first chapter has id 0, second chapter has id 1, etc.)
    filename = f"CH_{chapter['id'] + 1}.json"
    filepath = os.path.join(directory, filename)

    with open(filepath, 'w') as f:
        json.dump(chapter, f, indent=4)

