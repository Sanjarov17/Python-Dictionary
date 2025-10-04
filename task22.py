def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    result = {}
    for s in students:
        group = s["group"]
        name = s["name"]
        if group not in result:
            result[group] = []
        result[group].append(name)
    return result


data = [
    {"name": "Ali", "group": "A"},
    {"name": "Soli", "group": "A"},
    {"name": "Vali", "group": "B"},
    {"name": "Karim", "group": "B"},
]
print(group_students(data))
