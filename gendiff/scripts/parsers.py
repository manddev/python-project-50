import json
from pathlib import Path

import yaml


def get_full_path(file_name):
    return Path(__file__).parent.parent / 'tests' / 'test_data' / file_name


def get_data(file_name):
    if file_name.endswith('.json'):
        return json.load(open(get_full_path(file_name)))
    
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        fullpath = get_full_path(file_name)
        with open(fullpath, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)