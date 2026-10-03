# Write your solution here
def first_word(sentence):
    i = -1
    word = ''
    while sentence[i] != ' ':
        i += 1
        for letters in sentence[i]:
            if letters == ' ':
                break
            word += letters
    return word

def second_word(sentence):
    words = []
    for word in sentence:
        words.append(word)
    words_string = "".join(words)
    words_list = words_string.split()
    return words_list[1]

def last_word(sentence):
    words = []
    for word in sentence:
        words.append(word)
    words_string = "".join(words)
    words_list = words_string.split()
    return words_list[-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))