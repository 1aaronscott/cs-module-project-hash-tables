import string


def word_count(s):
    punc = 0
    counts = {}
    # Your code here
    ignore = list('":;,.-+=/\\|[]{}()*^&')
    # If the input contains no ignored characters, return an empty dictionary.
    # for i in ignore:
    #     if i in s:
    #         punc += 1
    # if punc == 0:
    #     return {}
    s = s.lower().translate(str.maketrans("", "", '":;,.-+=/\\|[]{}()*^&'))
    list_s = s.split()
    for word in list_s:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
