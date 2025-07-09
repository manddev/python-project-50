from os import path

from gendiff import generate_diff

CURRENT_DIR = path.dirname(path.abspath(__file__))


def test_json():
    actual = generate_diff('file1.json', 'file2.json')
    expected = open(path.join(CURRENT_DIR, 'test_data', 'expected_json.txt')) \
        .read()
    actual == expected


def test_yaml():
    actual = generate_diff('file1.yml', 'file2.yml')
    expected = open(path.join(CURRENT_DIR, 'test_data', 'expected_json.txt')) \
        .read()
    actual == expected
    
