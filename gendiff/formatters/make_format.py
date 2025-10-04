from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def make_format(diff, format="stylish"):
    match (format):
        case "stylish":
            return format_stylish(diff)
        case "plain":
            return format_plain(diff)