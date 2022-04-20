import json
import yaml


def get_file_extension(some_data):
    file_extension = some_data.split('.')[-1]
    return file_extension


def parsing(some_data, file_extension):
    if file_extension in ('yml', 'yaml'):
        result_dict = yaml.load(open(some_data), Loader=yaml.FullLoader)
    elif file_extension == 'json':
        result_dict = json.load(open(some_data))
    return result_dict
