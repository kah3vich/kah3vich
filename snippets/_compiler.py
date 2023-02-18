import os
import re


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

text = '{\n'

for item in get_subfolder_files():
    name = item['name']
    list_files = item['files']
    text += f'\n\n\t//| {name}'
    
    for file in list_files:
        with open(f'./{name}/{file}', 'r', encoding="utf8") as input_file:
                file_text = f'\n\n{remove_first_last_lines(input_file.read())}\n'
                pattern = r"(.*)(\n[^\n]*)$"
                replacement = r"\1,\2"

                text += re.sub(pattern, replacement, file_text)

text += '\n}\n\n//| 🔥 by kah3vich 🔥\n'

with open('./_.json', 'w', encoding="utf-8") as output_file:
    output_file.write(text)

print('Done ✅')