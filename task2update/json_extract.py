import re, json, os, codecs

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

directory = "chapterinfo"
if not os.path.exists(directory):
    os.makedirs(directory)

# Creates a json file for each chapter
for chapter in json_objects:
    name = chapter['name']
    filename = name.replace(" ", "") + ".json"
    filepath = os.path.join(directory, filename)

    with open(filepath, 'w') as f:
        json.dump(chapter, f, indent=4)

