# Your code here
from operator import itemgetter

# Read in all the words in one go
with open("robin.txt") as f:
    words = f.read()
words = words.lower().translate(str.maketrans("", "", '":;,.-+=/\\|[]{}()*^&'))
list_s = words.split()


def word_count(s):
    counts = {}
    for word in list_s:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def print_histo(dct):
    items = list(dct.items())
    items.sort(key=lambda e: (-e[1], e[0]))  # , reverse=(True, False))
    longestword = len(
        sorted(items, key=lambda e: len(e[0]), reverse=True)[0][0])
    for tup in items:
        print(f'{tup[0]:{longestword+2}}', tup[1]*'#')


#print(list_s, len(list_s), word_count(list_s))
print_histo(word_count(list_s))
