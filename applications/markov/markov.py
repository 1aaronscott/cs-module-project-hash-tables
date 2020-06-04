import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
words = words.split()

# TODO: analyze which words can follow other words
# Your code here


def build_cache(lst):
    cache = {}
    for cur in range(len(lst)-1):
        if lst[cur] in cache:
            cache[lst[cur]].append(lst[cur+1])
        else:
            cache[lst[cur]] = [lst[cur+1]]

    return cache


def build_corpus(cache, start):
    sequence = [start]
    current = start
    while current in cache:
        if current[-1] in list('.?!') or current[-2:] in ['."', '?"', '!"']:
            break
        else:
            sequence.append(random.choice(cache[current]))
            current = sequence[-1]
    return " ".join(sequence)

# TODO: construct 5 random sentences
# Your code here


w = build_cache(words)
#start_list = [x for x in w if x.isupper()]
for _ in range(5):
    print(build_corpus(w, random.choice(words)))
