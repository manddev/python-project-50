SEPARATOR = " "
SPACES_COUNT = 4
NODE_KEY_OFFSET = 2


def stringify(value, depth):
    if not isinstance(value, dict):
        return str(value)
    ind_size = depth * SPACES_COUNT
    indent = SEPARATOR * ind_size
    close_ind = SEPARATOR * (ind_size - SPACES_COUNT)
    lines = [f"{indent}{key}: {stringify(val, depth + 1)}" for key, val in value.items()]
    return "{\n" + "\n".join(lines) + f"\n{close_ind}}}"


def format_stylish(diff, depth=1):
    ind_size = depth * SPACES_COUNT
    key_ind = SEPARATOR * (ind_size - NODE_KEY_OFFSET)
    close_ind = SEPARATOR * (ind_size - SPACES_COUNT)
    lines = []

    for item in diff:
        name = item["name"]
        node_status = item["node_status"]
        value = stringify(item.get("value", " "), depth + 1)
        old_value = stringify(item.get("old_value", " "), depth + 1)
        new_value = stringify(item.get("new_value", " "), depth + 1)
        children = format_stylish(item.get("chidlren", " "), depth + 1)

        match(node_status):
            case "added":
                lines.append(f"{key_ind}+ {name}: {value}")
            case "deleted":
                lines.append(f"{key_ind}- {name}: {value}")
            case "unchanged":
                lines.append(f"{key_ind}  {name}: {value}")
            case "modified":
                lines.append(f"{key_ind}- {name}: {old_value}")
                lines.append(f"{key_ind}+ {name}: {new_value}")
            case "nested":
                lines.append(f"{key_ind}  {name}: {children}")
            
    return "{\n" + "\n".join(lines) + f"\n{close_ind}}}"
