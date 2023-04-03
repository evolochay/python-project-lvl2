from gendiff.types import CHANGED, ADDED, DELETED, NESTED

LF_CHAR = '\n'
INDENT_CHAR = ' '
INDENT = 4


get_status_sign = {
    ADDED: '+ ',
    DELETED: '- ',
}.get


def make_stylish(diff, depth=0):
    stylish_diff = []
    for diff_key, diff_value in sorted(diff.items()):
        next_depth = depth + 1
        status = diff_value['type']
        if status == CHANGED:
            value = format_value(diff_value['old_value'], next_depth)
            stylish_diff.append(make_line
                                (next_depth * INDENT, DELETED, diff_key, value))
            value = format_value(diff_value['value'], next_depth)
            stylish_diff.append(make_line(next_depth * INDENT, ADDED, diff_key, value))
            continue
        if status == NESTED:
            value = make_stylish(diff_value['value'], next_depth)
        else:
            value = format_value(diff_value['value'], next_depth)
        stylish_diff.append(make_line(next_depth * INDENT, status, diff_key, value))
    return '{{{0}}}'.format(
           ''.join(stylish_diff) + LF_CHAR + INDENT_CHAR * (depth * INDENT))


def format_value(value, depth):
    if isinstance(value, dict):
        stylish_value = []
        for node_key, node_value in value.items():
            new_depth = depth + 1
            value = format_value(node_value, new_depth)
            stylish_value.append(make_line(new_depth * INDENT, None, node_key, value))
        return '{{{0}}}'.format(
               ''.join(stylish_value) + LF_CHAR + INDENT_CHAR * (depth * INDENT))
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def make_line(indent, status, node_key, node_value):
    prefix = LF_CHAR + INDENT_CHAR * indent
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return '{0}{1}: {2}'.format(prefix, node_key, node_value)

# def make_stylish(diff, depth=0):
#     def make_line(indent, status, node_key, node_value):
#         status_sign = {
#             ADDED: '+ ',
#             DELETED: '- ',
#         }.get(status, '')
#         prefix = LF_CHAR + INDENT_CHAR * indent + status_sign
#         return '{0}{1}: {2}'.format(prefix, node_key, node_value)

#     def make_line_nested(node_key, node_value):
#             new_depth = depth + 1
#             return make_line(new_depth * INDENT, None, node_key, format_value(node_value, new_depth))
    
#     def format_value(value, depth):

#         if isinstance(value, dict):
#             stylish_value = map(lambda k, v: make_line_nested(k, v), value.items())
#             return '{{{0}}}'.format(''.join(stylish_value) + LF_CHAR + INDENT_CHAR * (depth * INDENT))
#         if isinstance(value, bool):
#             return str(value).lower()
#         if value is None:
#             return 'null'
#         return str(value)

#     sorted_diff = sorted(diff.items())
#     stylish_diff = map(lambda k, v: make_line_nested(k, v) if v['type'] == NESTED else make_line(depth * INDENT, v['type'], k, format_value(v['value'], depth+1)), sorted_diff)
#     return '{{{0}}}'.format(''.join(stylish_diff) + LF_CHAR + INDENT_CHAR * (depth * INDENT))

