import json
import yaml


def parsing(some_data, file_extension):
    result_dict = {}
    if file_extension in ('yml', 'yaml'):
        result_dict = yaml.load(open(some_data), Loader=yaml.FullLoader)
    elif file_extension == 'json':
        result_dict = json.load(open(some_data))
    return result_dict
