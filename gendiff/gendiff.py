from gendiff.parser import parsing
from collections import OrderedDict
from operator import itemgetter


def get_file_from_path(path):
    return parsing(path)


def generate_diff(path1, path2):
    first_file = parsing(path1)
    second_file = parsing(path2)

    def diff_dict(first_file, second_file):
        result = {}
        common_keys = first_file.keys() & second_file.keys()
        deleted_keys = first_file.keys() - second_file.keys()
        added_keys = second_file.keys() - first_file.keys()

        for key in common_keys:
            result = helping_with_common(key, first_file,
                                         second_file, diff_dict)

        for key in deleted_keys:
            result[('- ', key)] = first_file[key]

        for key in added_keys:
            result[('+ ', key)] = second_file[key]

        result_keys = sorted(result.keys(), key=itemgetter(1))
        output_dict = OrderedDict.fromkeys(result_keys)

        for key in result_keys:
            output_dict[key] = result[key]
        return output_dict
    return diff_dict(first_file, second_file)


def helping_with_common(key, first_file, second_file, diff_dict):
    result = {}
    if isinstance(first_file[key],
                  dict) and isinstance(second_file[key], dict):
        result[('  ', key)] = diff_dict(first_file[key],
                                        second_file[key])
    else:
        if first_file[key] == second_file[key]:
            result[('  ', key)] = first_file[key]
        else:
            result[('- ', key)] = first_file[key]
            result[('+ ', key)] = second_file[key]
    return result
