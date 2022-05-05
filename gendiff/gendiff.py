from gendiff.parser import parsing
from gendiff.formatters.format import STYlISH_FORMAT
from gendiff.formatters.format import format_diff
from gendiff.comparator import comparing


def generate_diff(path1, path2, format=STYlISH_FORMAT):
    first_dict = parsing(reader(path1), get_file_extension(path1))
    second_dict = parsing(reader(path2), get_file_extension(path2))
    diff = comparing(first_dict, second_dict)
    return format_diff(diff, format)


def get_file_extension(some_data):
    file_extension = some_data.split('.')[-1]
    return file_extension


def reader(some_data):
    result = ''
    with open(some_data) as file_data:
        result = file_data.read()
    return result
