SEPARATOR = " "
SPACES_COUNT = 4
NODE_KEY_OFFSET = 2


def stringify(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        ind_size = depth * SPACES_COUNT
        indent = SEPARATOR * ind_size
        close_ind = SEPARATOR * (ind_size - SPACES_COUNT)
        lines = [f"{indent}{key}: {stringify(val, depth + 1)}"
              for key, val in value.items()]
        return "{\n" + "\n".join(lines) + f"\n{close_ind}}}"
    elif value is None:
        return "null"
    return str(value)


def format_stylish(diff, depth=1):
    ind_size = depth * SPACES_COUNT
    key_ind = SEPARATOR * (ind_size - NODE_KEY_OFFSET)
    close_ind = SEPARATOR * (ind_size - SPACES_COUNT)
    lines = []

    for node in diff:
        name = node["name"]
        node_status = node["node_status"]
        value = node.get("value")
        old_value = node.get("old_value")
        new_value = node.get("new_value")
        children = node.get("children")
        
        match (node_status):
            case "added":
                lines.append(
                    f"{key_ind}+ {name}: {stringify(value, depth + 1)}"
                )
                             
            case "deleted":
                lines.append(
                    f"{key_ind}- {name}: {stringify(value, depth + 1)}"
                )
            case "unchanged":
                lines.append(
                    f"{key_ind}  {name}: {stringify(value, depth + 1)}"
                )       
            case "modified":
                lines.append(
                    f"{key_ind}- {name}: {stringify(old_value, depth + 1)}"
                )          
                lines.append(
                    f"{key_ind}+ {name}: {stringify(new_value, depth + 1)}"
                )           
            case "nested":
                lines.append(
                    f"{key_ind}  {name}: {format_stylish(children, depth + 1)}"
                )
           
    return "{\n" + "\n".join(lines) + f"\n{close_ind}}}"