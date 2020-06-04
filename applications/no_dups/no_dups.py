def no_dups(s):
    # Your code here
    s = s.split()
    seen = set()
    words = [x for x in s if not (x in seen or seen.add(x))]
    return ' '.join(words)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
