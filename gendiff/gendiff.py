from gendiff.parser import parsing
from gendiff.formatters.format import STYlISH_FORMAT
from gendiff.formatters.format import format_diff
from gendiff.comparator import comparing


def generate_diff(path1, path2, format=STYlISH_FORMAT):
    first_dict = get_data(path1)
    second_dict = get_data(path2)
    diff = comparing(first_dict, second_dict)
    return format_diff(diff, format)


def get_file_extension(some_data):
    file_extension = some_data.split('.')[-1]
    return file_extension


def get_data(pathfile):
    with open(pathfile, 'r') as data:
        return parsing(data, get_file_extension(pathfile))
