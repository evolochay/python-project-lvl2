from gendiff.types import CHANGED, ADDED, DELETED, NESTED, UNCHANGED


MESSAGE = {
    CHANGED: "Property '{path}' was updated. " "From {old_value} to {value}",
    ADDED: "Property '{path}' was added with value: {value}",
    DELETED: "Property '{path}' was removed",
}


def get_str_from_value(value):
    if type(value) in (list, dict):
        value = "[complex value]"
    elif isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = "null"
    elif isinstance(value, str):
        value = f"'{value}'"
    return value


def make_plain_output(values):
    def walk(current_value, path):
        result = []
        for key, value in current_value.items():
            type = value.get("type")
            if type == UNCHANGED:
                continue
            elif type == NESTED:
                path.append(key)
                result.append(walk(value.get("value"), path))
            else:
                path.append(key)
                old_value = get_str_from_value(value.get("old_value"))
                new_value = get_str_from_value(value.get("value"))
                result.append(
                    MESSAGE[type].format(
                        path=".".join(path), old_value=old_value,
                        value=new_value
                    )
                )
            path.pop(len(path) - 1)
        return "\n".join(result)

    return walk(values, [])
