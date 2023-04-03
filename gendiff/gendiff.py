from gendiff.parser import parse_data
from gendiff.formatters.format import STYlISH_FORMAT
from gendiff.formatters.format import make_format_diff
from gendiff.comparator import comparing


def generate_diff(path1, path2, format=STYlISH_FORMAT):
    first_dict = parse_data(read_data(path1), get_file_extension(path1))
    second_dict = parse_data(read_data(path2), get_file_extension(path2))
    diff = comparing(first_dict, second_dict)
    return make_format_diff(diff, format)


def get_file_extension(some_data):
    file_extension = some_data.split(".")[-1]
    return file_extension


def read_data(some_data):
    result = ""
    with open(some_data) as file_data:
        result = file_data.read()
    return result
