from gendiff.formatters.plain import make_plain_output
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.json_format import make_json_format


PLAIN_FORMAT = "plain"
STYlISH_FORMAT = "stylish"
JSON_FORMAT = "json"


def make_format_diff(data, format_name):
    if format_name == STYlISH_FORMAT:
        return make_stylish(data)
    elif format_name == PLAIN_FORMAT:
        return make_plain_output(data)
    elif format_name == JSON_FORMAT:
        return make_json_format(data)
    else:
        raise Exception("Wrong format!")
