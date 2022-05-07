from gendiff.types import CHANGED, ADDED, DELETED, NESTED

LF_CHAR = '\n'
INDENT_CHAR = ' '
INDENT_STEP = 4


get_status_sign = {
    ADDED: '+ ',
    DELETED: '- ',
}.get


def make_stylish(diff, depth=0):
    stylish_diff = []
    for diff_key, diff_value in sorted(diff.items()):
        new_depth = depth + INDENT_STEP
        status = diff_value['type']
        if status == CHANGED:
            value = format_value(diff_value['old_value'], new_depth)
            stylish_diff.append(make_line
                                (new_depth, DELETED, diff_key, value))
            value = format_value(diff_value['value'], new_depth)
            stylish_diff.append(make_line(new_depth, ADDED, diff_key, value))
            continue
        if status == NESTED:
            value = make_stylish(diff_value['value'], new_depth)
        else:
            value = format_value(diff_value['value'], new_depth)
        stylish_diff.append(make_line(new_depth, status, diff_key, value))
    return '{{{0}}}'.format(
           ''.join(stylish_diff) + LF_CHAR + INDENT_CHAR * depth)


def format_value(value, depth):
    if isinstance(value, dict):
        stylish_value = []
        for node_key, node_value in value.items():
            new_depth = depth + INDENT_STEP
            value = format_value(node_value, new_depth)
            stylish_value.append(make_line(new_depth, None, node_key, value))
        return '{{{0}}}'.format(
               ''.join(stylish_value) + LF_CHAR + INDENT_CHAR * depth)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def make_line(depth, status, node_key, node_value):
    prefix = LF_CHAR + INDENT_CHAR * depth
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return '{0}{1}: {2}'.format(prefix, node_key, node_value)
