def no_dups(s):
    # Your code here
    s = s.split()
    # make a set containing unique values
    seen = set()
    # Use a set to keep track of which elements you’ve seen
    # At the same time, populate the new list by a list comprehension
    # relies on the fact that set.add() returns None
    # http://www.martinbroadhurst.com/removing-duplicates-from-a-list-while-preserving-order-in-python.html
    words = [x for x in s if not (x in seen or seen.add(x))]
    return ' '.join(words)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
