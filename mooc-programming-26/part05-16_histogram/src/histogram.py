def histogram(string: str):
    dictionary = {}
    i = 0
    for letter in string:
        f = string.count(letter)
        dictionary[letter] = f * "*"
        i += 1
    values = list(dictionary.items())
    for letter in values:
        print(letter[0], letter[1])
    return None

if __name__ == "__main__":
    histogram("funnn")
