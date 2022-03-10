from gendiff.parser import parsing
from collections import OrderedDict
from operator import itemgetter


def get_file_from_path(path):
    return parsing(path)


def gen_diff(path1, path2):
    first_file = parsing(path1)
    second_file = parsing(path2)

    def diff_dict(first_file, second_file):
        result = {}
        common_keys = first_file.keys() & second_file.keys()
        deleted_keys = first_file.keys() - second_file.keys()
        added_keys = second_file.keys() - first_file.keys()

        for key in common_keys:
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

        for key in deleted_keys:
            result[('- ', key)] = first_file[key]

        for key in added_keys:
            result[('+ ', key)] = second_file[key]

        result_keys = sorted(result.keys(), key=itemgetter(1))
        print('RESULT {}'.format(result_keys))
        output_dict = OrderedDict.fromkeys(result_keys)
        for key in result_keys:
            print('KEY: {}'.format(key))
            output_dict[key] = result[key]
            print('OUTPUT {}'.format(output_dict))
        return output_dict
    return diff_dict(first_file, second_file)
