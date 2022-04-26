from gendiff.parser import parsing, get_file_extension
from gendiff.formatters.format import STYlISH_FORMAT
from gendiff.formatters.format import format_diff
from gendiff.comparator import comparing


def generate_diff(path1, path2, format=STYlISH_FORMAT):
    first_data_extension = get_file_extension(path1)
    second_data_extension = get_file_extension(path2)
    first_dict = parsing(path1, first_data_extension)
    second_dict = parsing(path2, second_data_extension)
    diff = comparing(first_dict, second_dict)
    return format_diff(diff, format)
