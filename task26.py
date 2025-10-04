def merge_dicts(a: dict, b: dict) -> dict:
    result = a.copy()
    result.update(b)
    return result


print(merge_dicts({"x": 1, "y": 2}, {"y": 99, "z": 5}))
