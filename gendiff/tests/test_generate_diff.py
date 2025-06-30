from os import path

from gendiff import generate_diff


def test_gendiff():
    current_dir = path.dirname(path.abspath(__file__))
    actual = generate_diff('file1.json', 'file2.json')
    expected = open(path.join(current_dir, 'test_data', 'expected_json.txt')) \
        .read()
    actual == expected
    
    

