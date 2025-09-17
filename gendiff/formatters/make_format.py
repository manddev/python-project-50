from formatters.stylish import format_stylish


def make_format(diff, format="stylish"):
    match (format):
        case "stylish":
            return format_stylish(diff, format)