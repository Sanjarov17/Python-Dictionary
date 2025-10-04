def most_common_char(text: str) -> str:
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return max(freq, key=freq.get)


print(most_common_char("assalomu alaykum"))
