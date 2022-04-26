import json
import itertools
from gendiff.actions import CHANGED, ADDED, DELETED, NESTED, UNCHANGED

ACTION_SIGN = {CHANGED: ['-', '+'],
               UNCHANGED: ' ',
               ADDED: '+',
               DELETED: '-',
               NESTED: ' '}


def get_str(value):
    if isinstance(value, str):
        return value
    else:
        return json.dumps(value)


def make_output(values, replacer=' ', spaces_count=1):
    def walk(value, depth):
        if not isinstance(value, dict):
            return get_str(value)
        deep_indent_size = depth * spaces_count
        deep_indent = replacer * deep_indent_size
        current_replacer = replacer * (deep_indent_size - spaces_count)
        lines = []
        for key, value in value.items():
            # if only copy dictionary
            is_value_dict = isinstance(value, dict)
            if (is_value_dict and value.get('type') is None) \
                    or not is_value_dict:
                sign = ACTION_SIGN[UNCHANGED]
                new_value = value
            else:
                sign = ACTION_SIGN[value.get('type')]
                if isinstance(sign, list):
                    old_sign = sign[0]
                    old_value = value['old_value']
                    lines.append(f'{deep_indent}{old_sign}{replacer}{key}: '
                                 f'{walk(old_value, depth + 2)}')
                    sign = sign[1]
                new_value = value['value']
            lines.append(f'{deep_indent}{sign}{replacer}{key}: '
                         f'{walk(new_value, depth + 2)}')
        result = itertools.chain("{", lines, [current_replacer + "}"])
        return '\n'.join(result)

    return walk(values, 1)


def stylish(data):
    return make_output(data, replacer=' ', spaces_count=2)
