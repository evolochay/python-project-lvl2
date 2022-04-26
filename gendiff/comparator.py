from gendiff.actions import CHANGED, ADDED, DELETED, NESTED, UNCHANGED
from operator import itemgetter


def comparing(first_dict, second_dict):
    result = {}
    common_keys = first_dict.keys() & second_dict.keys()
    deleted_keys = first_dict.keys() - second_dict.keys()
    added_keys = second_dict.keys() - first_dict.keys()

    for key in common_keys:
        if isinstance(first_dict[key],
                      dict) and isinstance(second_dict[key], dict):
            result[key] = \
                {'action': NESTED,
                 'value': comparing(first_dict[key], second_dict[key])}

        elif first_dict[key] == second_dict[key]:
            result[key] = \
                {'action': UNCHANGED,
                 'value': first_dict[key]}
        else:
            result[key] = \
                {'action': CHANGED,
                 'old_value': first_dict[key],
                 'value': second_dict[key]}

    some_dict = {}
    for key in deleted_keys:
        some_dict[key] = {'action': DELETED, 'value': first_dict[key]}
        result.update(some_dict)

    for key in added_keys:
        some_dict[key] = {'action': ADDED, 'value': second_dict[key]}
        result.update(some_dict)

    output_dict = dict(sorted(result.items(), key=itemgetter(0)))
    return output_dict
