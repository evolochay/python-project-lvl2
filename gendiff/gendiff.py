import json


def generate_diff(file_path1, file_path2):
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))
    result = '{' + '\n'
    for i in first_file.keys() & second_file.keys():
        if first_file[i] == second_file[i]:
            result = result + '   ' + i + ': ' + str(first_file[i]) + '\n'
        else:
            result = result + ' + ' + i + ': ' + str(second_file[i]) + '\n'
            result = result + ' - ' + i + ': ' + str(first_file[i]) + '\n'
    for i in first_file.keys() - second_file.keys():
         result = result + ' - ' + i + ': ' + str(first_file[i]) + '\n'
    for i in second_file.keys() - first_file.keys():
         result = result + ' + ' + i + ': ' + str(second_file[i]) + '\n'
    result = result + '}'

    return result