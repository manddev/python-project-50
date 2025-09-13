SEPARATOR = " "
SPACES_COUNT = 4
NODE_KEY_OFFSET = 2


def stringify(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if not isinstance(value, dict):
        return str(value)
    ind_size = depth * SPACES_COUNT
    indent = SEPARATOR * ind_size
    end_ind = SEPARATOR * (ind_size - SPACES_COUNT)
    lines = [f"{indent}{key}: {stringify(val, depth + 1)}" for key, val in value.items()]
    return "{\n" + "\n".join(lines) + f"\n{end_ind}}}"


def format_stylish(diff, depth=1):
    ind_size = depth * SPACES_COUNT
    key_ind = SEPARATOR * (ind_size - NODE_KEY_OFFSET)
    end_ind = SEPARATOR * (ind_size - SPACES_COUNT)
    lines = []
    
    for item in diff:
        name = item["name"]
        node_status = item["node_status"]

        match(node_status):
            case "unchanged":
                lines.append(f"{key_ind}  {name}: {stringify(item.get("value", " "), depth + 1)}")
            case "added":
                lines.append(f"{key_ind}+ {name}: {stringify(item.get("value", " "), depth + 1)}")
            case "deleted":
                lines.append(f"{key_ind}- {name}: {stringify(item.get("value", " "), depth + 1)}")
            case "nested":
                children = format_stylish(item.get("children"), depth + 1)
                lines.append(f"{key_ind}  {name}: {children}")
            case "modified":
                lines.append(f"{key_ind}- {name}: {stringify(item.get("old_value", " "), depth + 1)}")
                lines.append(f"{key_ind}+ {name}: {stringify(item.get("new_value", " "), depth + 1)}")
    
    return "{\n" + "\n".join(lines) + f"\n{end_ind}}}"


