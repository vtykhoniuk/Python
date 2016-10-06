def split(s, words, result = None):

    if result is None:
        result = []

    if not s:
        return result

    for w in words:
        if s.startswith(w):
            result.append(w)
            split(s[len(w):], words, result)

    return result
