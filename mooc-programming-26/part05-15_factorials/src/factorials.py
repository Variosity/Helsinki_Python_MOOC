def factorials(n: int):
    dictionary = {}
    i = 0
    x = 1
    for num in range(n):
        i += 1
        dictionary[i] = i * x
        x = i * x
    return dictionary

if __name__ == "__main__":
    print(factorials(5))