from gendiff.formatters.make_format import make_format
from gendiff.get_diff import get_diff
from gendiff.parsers import get_data


def generate_diff(filepath1, filepath2, format='stylish'):
    dict1 = get_data(filepath1)
    dict2 = get_data(filepath2)
    diff = get_diff(dict1, dict2)
    print(make_format(diff))


generate_diff("file1.json", "file2.json")





