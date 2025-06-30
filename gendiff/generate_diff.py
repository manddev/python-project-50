from gendiff.converter import get_data


def generate_diff(filepath1, filepath2):
    dict1 = get_data(filepath1)
    dict2 = get_data(filepath2)
    keys = sorted(dict1.keys() | dict2.keys())

    def get_string(key):
        deleted = """  - """
        added = """  + """
        not_changed = "    "
        
        if key not in dict1:
            return f'{added}{key}: {dict2[key]}'
        if key not in dict2:
            return f'{deleted}{key}: {dict1[key]}'
        if dict1[key] == dict2[key]:
            return f'{not_changed}{key}: {dict1[key]}'
        return f'{deleted}{key}: {dict1[key]}\n{added}{key}: {dict2[key]}'
    strings = list(map(lambda key: get_string(key), keys))
    result = '{\n' + '\n'.join(strings) + '\n}'
    print(result)
    return result