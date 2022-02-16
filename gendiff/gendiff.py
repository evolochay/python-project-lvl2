import json


def generate_diff(file_path1, file_path2):
    result = '{\n'
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))
    all_keys = sorted(list(first_file.keys() | second_file.keys()))
    two_keys = first_file.keys() & second_file.keys()
    deleted_keys = first_file.keys() - second_file.keys()
    added_keys = second_file.keys() - first_file.keys()

    for key in all_keys:
        if key in two_keys:
            if first_file[key] == second_file[key]:
                result += '    {}: {}\n'.format(
                    key, lower_case(first_file[key]))
            else:
                result += '  - {}: {}\n'.format(
                    key, lower_case(first_file[key]))
                result += '  + {}: {}\n'.format(
                    key, lower_case(second_file[key]))
        elif key in deleted_keys:
            result += '  - {}: {}\n'.format(key, lower_case(first_file[key]))
        elif key in added_keys:
            result += '  + {}: {}\n'.format(key, lower_case(second_file[key]))

    result += '}'
    print(result)
    return result


def lower_case(element):
    if element is True:
        return 'true'
    if element is False:
        return 'false'
    if element is None:
        return 'null'
    else:
        return element
