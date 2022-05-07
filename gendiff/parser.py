import json
import yaml


def parse_data(some_data, extension):
    if extension == 'json':
        return json.loads(some_data)
    if extension == 'yaml' or extension == 'yml':
        return yaml.safe_load(some_data)
