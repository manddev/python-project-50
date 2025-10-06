def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    return str(value)


def format_plain(diff, path=''):
    PROP = "Property "
    ADDED = " was added with value: "
    REMOVED = " was removed"
    UPD = " was updated. From "

    lines = []

    def format_node(node):
        name = node["name"]
        node_status = node["node_status"]
        cur_path = f"{path}.{name}" if path else name

        match (node_status):
            case "added":
                value = stringify(node.get("value", ""))
                return (
                    f"{PROP}'{cur_path}'{ADDED}{value}"
                )
            case "deleted":
                return (
                    f"{PROP}'{cur_path}'{REMOVED}"
                )
            case "modified":
                old_val = stringify(node.get("old_value", ""))
                new_val = stringify(node.get("new_value", ""))
                return (
                    f"{PROP}'{cur_path}'{UPD}{old_val} to {new_val}"
                )
            case "nested":
                children = node.get("children", "")
                return format_plain(children, cur_path)
    for item in diff:
        formatted_node = format_node(item)
        if formatted_node is not None:
            lines.append(formatted_node)
    
    return "\n".join(lines)