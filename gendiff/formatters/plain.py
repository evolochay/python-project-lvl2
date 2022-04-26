from gendiff.actions import CHANGED, ADDED, DELETED, NESTED, UNCHANGED


MESSAGE = {CHANGED: "Property '{path}' was updated. "
                    "From {old_value} to {value}",
           ADDED: "Property '{path}' was added with value: {value}",
           DELETED: "Property '{path}' was removed"}


def get_name(value):
    if type(value) in (list, dict):
        value = '[complex value]'
    elif isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, str):
        value = f"'{value}'"
    return value


def plain_output(values):
    def walk(current_value, path):
        result = []
        for key, value in current_value.items():
            action = value.get('type')
            if isinstance(value, dict) and action != UNCHANGED:
                path.append(key)
                if action == NESTED:
                    result.append(walk(value.get('value'), path))
                else:
                    old_value = get_name(value.get('old_value'))
                    new_value = get_name(value.get('value'))
                    result.append(MESSAGE[action].format(
                        path='.'.join(path),
                        old_value=old_value,
                        value=new_value
                    ))
                path.pop(len(path) - 1)
        return '\n'.join(result)

    return walk(values, [])
