from gendiff.formatters.plain import plain_output
from gendiff.formatters.stylish import stylish


PLAIN_FORMAT = 'plain'
STYlISH_FORMAT = 'stylish'


def format_diff(data, format_name):
    if format_name == STYlISH_FORMAT:
        return stylish(data)
    elif format_name == PLAIN_FORMAT:
        return plain_output(data)