from gendiff.formatters.plain import plain_output
from gendiff.formatters.stylish import stylish
from gendiff.formatters.json_format import json_format


PLAIN_FORMAT = 'plain'
STYlISH_FORMAT = 'stylish'
JSON_FORMAT = 'json'


def format_diff(data, format_name):
    if format_name == STYlISH_FORMAT:
        return stylish(data)
    elif format_name == PLAIN_FORMAT:
        return plain_output(data)
    elif format_name == JSON_FORMAT:
        return json_format(data)
    else:
        raise Exception('Wrong format!')
