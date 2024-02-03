import os
import re


def get_files_in_current_folder():
    current_directory = os.getcwd()
    file_list = os.listdir(current_directory)

    return file_list

def remove_elements_by_name(array, names):
    for name in names:
        index = None

        for i, element in enumerate(array):
            if element == name:
                index = i
                break

        if index is not None:
            array.pop(index)

    return array

def remove_first_last_lines(text):
    lines = text.split('\n')
    lines = lines[1:-2]
    result = '\n'.join(lines)

    return result

def compiler_finally_config():
    text = '{\n\t//| 🔥 Config Kah3vich - https://github.com/kah3vich \n\n\t//? 🧨 Info - https://code.visualstudio.com/docs/editor/codebasics \n\t//? 🤔 Config - https://code.visualstudio.com/docs/getstarted/settings \n'

    file_list = remove_elements_by_name(get_files_in_current_folder(), ['_info.txt', '_.json', '_compiler.py', '_backup.json'])

    for file in file_list:
        with open(file, 'r', encoding="utf8") as input_file:
            if (file_list[-1] == file):
                text += f'\n{remove_first_last_lines(input_file.read())}\n'
            else:
                file_text = f'\n{remove_first_last_lines(input_file.read())}\n'
                pattern = r"(.*)(\n[^\n]*)$"
                replacement = r"\1,\2"

                text += re.sub(pattern, replacement, file_text)

    text += '\n}\n\n//| 🔥 by kah3vich 🔥\n'

    with open('./_.json', 'w', encoding="utf-8") as output_file:
        output_file.write(text)

if __name__ == "__main__":
    compiler_finally_config()

    print('\ncompiler_finally_config - Done ✅')
