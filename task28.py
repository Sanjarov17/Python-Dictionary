def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result = {}
    for word in words:
        l = len(word)
        if l not in result:
            result[l] = []
        result[l].append(word)
    return result


print(group_by_length(["ali", "vali", "diyor", "karim", "aziza", "bobur"]))
