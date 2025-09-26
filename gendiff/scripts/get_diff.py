def get_diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())

    def get_status(key):
        if key not in dict2:
            return {"name": key, 
                    "node_status": "deleted", 
                    "value": dict1[key],
                }
        if key not in dict1:
            return {"name": key,
                    "node_status": "added",
                    "value": dict2[key],
                }
        if dict1[key] == dict2[key]:
            return {"name": key,
                    "node_status": "unchanged",
                    "value": dict1[key],
                }
        if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            return {"name": key,
                    "node_status": "nested",
                    "children": get_diff(dict1[key], dict2[key]),
                }
        return {"name": key,
                "node_status": "modified",
                "old_value": dict1[key],
                "new_value": dict2[key],
            }
    return list(map(get_status, keys))
