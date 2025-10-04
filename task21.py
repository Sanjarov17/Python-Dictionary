def count_names(names: list[str]) -> dict[str, int]:
    result = {}
    for n in names:
        result[n] = result.get(n, 0) + 1
    return result


print(count_names(["Ali", "Vali", "Ali", "Sami", "Ali", "Vali"]))
