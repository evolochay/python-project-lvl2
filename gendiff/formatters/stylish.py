from gendiff.types import CHANGED, ADDED, DELETED, NESTED

LF_CHAR = "\n"
INDENT_CHAR = " "
INDENT = 4


get_status_sign = {
    ADDED: "+ ",
    DELETED: "- ",
}.get


def make_stylish(diff, depth=0):
    stylish_diff = [
        make_line(
            (depth + 1) * INDENT,
            DELETED,
            diff_key,
            format_value(diff_value["old_value"], depth + 1),
        ) + make_line(
            (depth + 1) * INDENT,
            ADDED,
            diff_key,
            format_value(diff_value["value"], depth + 1),
        )
        if diff_value["type"] == CHANGED
        else make_line(
            (depth + 1) * INDENT,
            status,
            diff_key,
            make_stylish(diff_value["value"], depth + 1)
            if status == NESTED
            else format_value(diff_value["value"], depth + 1),
        )
        for diff_key, diff_value in sorted(diff.items())
        for status in [diff_value["type"]]
    ]
    return "{{{0}}}".format(
        "".join(stylish_diff) + LF_CHAR + INDENT_CHAR * (depth * INDENT)
    )


def format_value(value, depth):
    if isinstance(value, dict):
        stylish_value = []
        for node_key, node_value in value.items():
            new_depth = depth + 1
            value = format_value(node_value, new_depth)
            stylish_value.append(make_line(new_depth * INDENT,
                                           None, node_key, value))
        return "{{{0}}}".format(
            "".join(stylish_value) + LF_CHAR + INDENT_CHAR * (depth * INDENT)
        )
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def make_line(indent, status, node_key, node_value):
    prefix = LF_CHAR + INDENT_CHAR * indent
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return "{0}{1}: {2}".format(prefix, node_key, node_value)
