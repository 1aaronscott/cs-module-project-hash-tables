# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

most_common = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
               'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
with open("ciphertext.txt") as f:
    words = f.read()


def letters_by_count(corpus):
    counts = {}
    corpus = corpus.translate(str.maketrans(
        "", "", ' ":;,.-+=/\\|[]{}()*^&\n\'\!—?1'))

    for c in corpus:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    items = list(counts.items())
    items.sort(key=lambda e: e[1], reverse=True)
    items = [x[0] for x in items]
    return items


converter = dict(zip(letters_by_count(words), most_common))
print(words.translate(str.maketrans(converter)))
