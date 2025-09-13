from parsers import get_data
from get_diff import get_diff
from formatters.make_format import make_format


def generate_diff(filepath1, filepath2, format='stylish'):
    dict1 = get_data(filepath1)
    dict2 = get_data(filepath2)
    diff = get_diff(dict1, dict2)
    return make_format(diff, format)



print(generate_diff('file1.json', 'file2.json'))