# Your code here
cache = {}


def expensive_seq(x, y, z):
    # Your code here
    key = (x, y, z)
    if x <= 0:  # handle base case
        return y+z
    else:  # recurse if key not already present
        if key not in cache:
            cache[key] = expensive_seq(
                x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    return cache[key]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
