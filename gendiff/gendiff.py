from gendiff.parser import parsing
from gendiff.formatters.format import STYlISH_FORMAT
from gendiff.formatters.format import format_diff
from gendiff.comparator import comparing


def generate_diff(path1, path2, format=STYlISH_FORMAT):
    first_file_extension = get_file_extension(path1)
    second_file_extension = get_file_extension(path2)
    first_dict = parsing(path1, first_file_extension)
    print(first_dict)
    second_dict = parsing(path2, second_file_extension)
    print(second_dict)
    diff = comparing(first_dict, second_dict)
    return format_diff(diff, format)


def get_file_extension(some_data):
    file_extension = some_data.split('.')[-1]
    return file_extension
