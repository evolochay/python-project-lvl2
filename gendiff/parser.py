import json
import yaml


def parsing(some_path):
    file_extension = some_path.split('.')[-1]
    if file_extension in ('yml', 'yaml'):
        result_dict = yaml.load(open(some_path), Loader=yaml.FullLoader)
    elif file_extension == 'json':
        result_dict = json.load(open(some_path))
    return result_dict
