# Write your solution here
def same_chars(word, x, y):
    try:
        if word[x] == word[y]:
            return True
    except IndexError:
        return False
    return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))