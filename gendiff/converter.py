from pathlib import Path
import json

def get_full_path(file_name):
    return Path(__file__).parent / 'tests' / 'test_data' / file_name

def get_data(file_name):
    if file_name.endswith('.json'):
        return json.load(open(get_full_path(file_name)))
    