from gendiff.types import CHANGED, ADDED, DELETED, NESTED

LF_CHAR = '\n'
INDENT_CHAR = ' '
INDENT_STEP = 4


get_status_sign = {
    ADDED: '+ ',
    DELETED: '- ',
}.get


def format_stylish(diff, indent=0):
    stylish_diff = []
    for diff_key, diff_value in sorted(diff.items()):
        new_indent = indent + INDENT_STEP
        status = diff_value['type']
        if status == CHANGED:
            value = format_value(diff_value['old_value'], new_indent)
            stylish_diff.append(add_prefix
                                (new_indent, DELETED, diff_key, value))
            value = format_value(diff_value['value'], new_indent)
            stylish_diff.append(add_prefix(new_indent, ADDED, diff_key, value))
            continue
        if status == NESTED:
            value = format_stylish(diff_value['value'], new_indent)
        else:
            value = format_value(diff_value['value'], new_indent)
        stylish_diff.append(add_prefix(new_indent, status, diff_key, value))
    return compose_stylish(indent, stylish_diff)


def format_value(value, indent):
    if isinstance(value, dict):
        stylish_value = []
        for node_key, node_value in value.items():
            new_indent = indent + INDENT_STEP
            value = format_value(node_value, new_indent)
            stylish_value.append(add_prefix(new_indent, None, node_key, value))
        return compose_stylish(indent, stylish_value)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def add_prefix(indent, status, node_key, node_value):
    prefix = LF_CHAR + INDENT_CHAR * indent
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return '{0}{1}: {2}'.format(prefix, node_key, node_value)


def compose_stylish(indent, output):
    return '{{{0}}}'.format(''.join(output) + LF_CHAR + INDENT_CHAR * indent)


def stylish(diff):
    return format_stylish(diff)
