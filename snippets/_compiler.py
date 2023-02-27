import os
import re

#| Function 

def get_subfolder_files():
    current_dir = os.getcwd()
    subfolder_files = []

    for subdir in os.listdir(current_dir):
        if os.path.isdir(os.path.join(current_dir, subdir)):
            obj = {"name": subdir, "files": []}

            for file in os.listdir(os.path.join(current_dir, subdir)):
                if os.path.isfile(os.path.join(current_dir, subdir, file)):
                    obj["files"].append(file)

            subfolder_files.append(obj)

    return subfolder_files

def remove_first_last_lines(text):
    lines = text.split('\n')
    lines = lines[1:-4]
    result = '\n'.join(lines)

    return result

#| Config 

text = '{\n'

for item in get_subfolder_files():
    name = item['name']
    list_files = item['files']
    text += f'\n\t//| {name}\n'
    
    for file in list_files:
        with open(f'./{name}/{file}', 'r', encoding="utf8") as input_file:
                file_text = f'\n{remove_first_last_lines(input_file.read())}\n'
                pattern = r"(.*)(\n[^\n]*)$"
                replacement = r"\1,\2"

                text += re.sub(pattern, replacement, file_text)

text += '\n}\n\n//| 🔥 by kah3vich 🔥\n'

with open('./_config.json', 'w', encoding="utf-8") as output_file:
    output_file.write(text)

#| Readme json

config_text = '{\n\t"config": ['

for item in get_subfolder_files():
    name = item['name']
    list_files = item['files']
    config_text += '\n\t\t{'
    config_text += f'\n\t\t\t"title": "{name}",\n\t\t\t"snippets": ['
    for file in list_files:
        config_text += '\n\t\t\t\t{'
        with open(f'./{name}/{file}', 'r', encoding="utf8") as input_file:
                input_file_text = input_file.read()

                name_text = re.search(r'"prefix": "(.*?)"', input_file_text).group(1)
                description_text = re.search(r'"description": "(.*?)"', input_file_text).group(1)
                config_text += f'\n\t\t\t\t\t"name": "{name_text}",\n\t\t\t\t\t"description": "{description_text}"'
        config_text += '\n\t\t\t\t},'
    config_text += '\n\t\t\t],\n\t\t},'

config_text += '\n\t]\n}'


with open('./_readme.json', 'w', encoding="utf-8") as output_file:
    output_file.write(config_text)

#| Result

print('Done ✅')
