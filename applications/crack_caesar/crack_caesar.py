# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# most common letters in descending order according to rubric
most_common = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
               'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# read in the cipher file
with open("ciphertext.txt") as f:
    words = f.read()


def letters_by_count(corpus):
    ''' take in a text body and return a list of letters in descending order of
    frequency '''

    counts = {}
    # eliminate all non-alphabet characters, probably should be RE to be more
    # portable
    corpus = corpus.translate(str.maketrans(
        "", "", ' ":;,.-+=/\\|[]{}()*^&\n\'\!—?1'))

    # keep count of letters in a dict
    for c in corpus:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    # convert dict to list of tuples, then sort list by letter frequency
    items = list(counts.items())
    items.sort(key=lambda e: e[1], reverse=True)
    # make a list of just the letters in order
    items = [x[0] for x in items]
    return items


# create a dict to translate letters in cipertext to most common letters
converter = dict(zip(letters_by_count(words), most_common))
print(words.translate(str.maketrans(converter)))
