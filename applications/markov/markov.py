import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
words = words.split()

# TODO: analyze which words can follow other words
# Your code here


def build_cache(lst):
    ''' take in a list and build a dict cache of all possible 
    succeeding words '''
    cache = {}
    for cur in range(len(lst)-1):
        if lst[cur] in cache:  # if the word is alread in the cache
            # add following word to its value list
            cache[lst[cur]].append(lst[cur+1])
        else:  # add the word as a key and the following word as a value list
            cache[lst[cur]] = [lst[cur+1]]

    return cache


def build_corpus(cache, start):
    ''' take in a cache of words and a start word and build a sentence until stop 
    condition is met '''
    sequence = [start]
    current = start
    while current in cache:  # make sure the current word is a key in the cache
        # stop if the current word meets the stop word conditions
        if current[-1] in list('.?!') or current[-2:] in ['."', '?"', '!"']:
            break
        else:  # add the word to the sequence list and make it the next word
            sequence.append(random.choice(cache[current]))
            current = sequence[-1]
    return " ".join(sequence)

# TODO: construct 5 random sentences
# Your code here


w = build_cache(words)
#start_list = [x for x in w if x.isupper()]
for _ in range(5):
    print(build_corpus(w, random.choice(words)))
