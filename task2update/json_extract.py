import re, json, os
import codecs

file_path = 'quizzes.json'

with open(file_path, 'r') as file:
    js_function = file.read()

# Extracting each json for each chapter
pattern = r'JSON\.parse\((["\'])(.*?)\1\)'

matches = re.findall(pattern, js_function, re.DOTALL)

json_objects = []

# Iterates through each json for each chapter
for match in matches:
    try:
        unescaped_str = codecs.decode(match[1], 'unicode_escape')
        json_obj = json.loads(unescaped_str)
        json_objects.append(json_obj)
    except (json.JSONDecodeError, UnicodeDecodeError):
        pass

# Creates a json file for each chapter
for chapter in json_objects:
    name = chapter['name']
    filename = name.replace(" ", "") + ".json"
    with open(filename, 'w') as f:
        json.dump(chapter, f)

