def sentencereverse(s):
    if not isinstance(s, str):
        raise ValueError()

    result = []
    i = 0
    while i < len(s):
        if not s[i].isspace():
            j = i
            i += 1
            while i < len(s) and not s[i].isspace():
                i += 1

            result.append(s[j:i][::-1])
        else:
            i += 1

    return " ".join(result)[::-1]
