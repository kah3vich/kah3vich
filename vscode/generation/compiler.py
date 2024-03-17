import os
import re

def get_files_in_current_folder():
    current_directory = "{}/data".format(os.getcwd())

    file_list = os.listdir(current_directory)

    return file_list

def get_info():
    result = ''

    with open('./info.txt', 'r', encoding='utf-8') as file:
        result = file.read()
        file.close()

    return result

def remove_first_last_lines(text):
    lines = text.split('\n')
    lines = lines[1:-2]
    result = '\n'.join(lines)

    return result

def compiler_finally_config():
    text = '{}\n\n'.format(get_info())
    print(text)
    text += '{\n'

    file_list = get_files_in_current_folder()

    for file in file_list:
        with open(f'./data/{file}', 'r', encoding="utf8") as input_file:
            if (file_list[-1] == file):
                text += '\n{}\n'.format(remove_first_last_lines(input_file.read()))
            else:
                file_text = '\n{}\n'.format(remove_first_last_lines(input_file.read()))
                pattern = r"(.*)(\n[^\n]*)$"
                replacement = r"\1,\2"

                text += re.sub(pattern, replacement, file_text)

            input_file.close()

    text += '\n}\n'

    with open('./result.json', 'w', encoding="utf8") as output_file:
        output_file.write(text)
        output_file.close()

if __name__ == "__main__":
    compiler_finally_config()

    print('\nCompiler config - Done ✅')
