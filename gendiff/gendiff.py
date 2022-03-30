from gendiff.parser import parsing
from operator import itemgetter
from gendiff.actions import CHANGED, ADDED, DELETED, NESTED, UNCHANGED
from gendiff.formatters.format import STYlISH_FORMAT
from gendiff.formatters.format import format_diff


def get_file_from_path(path):
    return parsing(path)


def generate_diff(path1, path2, format=STYlISH_FORMAT):
    file1 = parsing(path1)
    file2 = parsing(path2)
    diff = comparing(file1, file2)
    return format_diff(diff, format)


def comparing(file1, file2):
    def diff_dict(first_file, second_file):
        result = {}
        common_keys = first_file.keys() & second_file.keys()
        deleted_keys = first_file.keys() - second_file.keys()
        added_keys = second_file.keys() - first_file.keys()

        for key in common_keys:
            if isinstance(first_file[key],
                          dict) and isinstance(second_file[key], dict):
                result[key] = \
                    {'action': NESTED,
                     'value': diff_dict(first_file[key], second_file[key])}

            elif first_file[key] == second_file[key]:
                result[key] = \
                    {'action': UNCHANGED,
                     'value': first_file[key]}
            else:
                result[key] = \
                    {'action': CHANGED,
                     'old_value': first_file[key],
                     'value': second_file[key]}

        result.update(add_value(DELETED, deleted_keys, first_file))
        result.update(add_value(ADDED, added_keys, second_file))

        output_dict = dict(sorted(result.items(), key=itemgetter(0)))

        return output_dict
    return diff_dict(file1, file2)


def add_value(action, keys, value):
    result = {}
    for key in keys:
        result[key] = {'action': action, 'value': value[key]}
    return result
