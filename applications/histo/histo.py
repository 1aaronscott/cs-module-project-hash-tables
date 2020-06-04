# Your code here
from operator import itemgetter

# Read in all the words in one go
with open("robin.txt") as f:
    words = f.read()
# strip out unwanted characters
words = words.lower().translate(str.maketrans("", "", '":;,.-+=/\\|[]{}()*^&'))
# and convert to a list
list_s = words.split()


def word_count(s):
    ''' take in a list and count words into a cache '''
    counts = {}
    for word in list_s:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def print_histo(dct):
    ''' take in a dict and print out histo gram based on word frequency '''

    items = list(dct.items())
    # sort the list first by descending frequency, then by alphabetically
    items.sort(key=lambda e: (-e[1], e[0]))  # , reverse=(True, False))
    # determine the longest word for formatting purposes
    longestword = len(
        sorted(items, key=lambda e: len(e[0]), reverse=True)[0][0])
    # process each tuple in the list
    for tup in items:
        print(f'{tup[0]:{longestword+2}}', tup[1]*'#')


#print(list_s, len(list_s), word_count(list_s))
print_histo(word_count(list_s))
