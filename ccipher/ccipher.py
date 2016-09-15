import sys

def encode_char(c, shift):
    if len(c) != 1:
        raise ValueError()

    if c.isalpha():
        start = ord('A' if c.isupper() else 'a')
        return chr(start + (ord(c) - start + shift)%26)
    else:
        return c

def encode_str(s, shift):
    if not isinstance(s, str):
        raise ValueError()

    for c in s:
        yield encode_char(c, shift)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <SHIFT>".format(sys.argv[0]), file=sys.stderr)
        exit(1)

    shift = int(sys.argv[1])
    for line in sys.stdin:
        line = line.rstrip()
        print("".join(encode_str(line, shift)))
