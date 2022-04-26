import json
import yaml


def parsing(some_data, format):
    try:
        if format in ('yml', 'yaml'):
            result_dict = yaml.load(some_data, Loader=yaml.FullLoader)
        elif format == 'json':
            result_dict = json.load(some_data)

        if result_dict is None:
            raise TypeError
    except (TypeError, yaml.parser.ParserError):
        return False
    else:
        return result_dict
