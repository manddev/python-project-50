from stylish import format_stylish


def make_format(diff, fomtat="stylish"):
    match(format):
        case "stylish":
            return format_stylish(diff)