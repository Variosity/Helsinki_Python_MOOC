import string

def separate_characters(my_string: str):
    string_list = []
    final_string_list = []
    clean = ''
    for char in my_string:
        if char in string.ascii_letters:
            string_list.append(char)
            clean = "".join(string_list)
    final_string_list.append(clean)
    string_list = []
    for char in my_string:
        if char in string.punctuation and not char in string.ascii_letters and not char in string.whitespace:
            string_list.append(char)
            clean = "".join(string_list)
    final_string_list.append(clean)
    string_list = []
    for char in my_string:
        if char in string.whitespace or (not char in string.ascii_letters and not char in string.punctuation):
            string_list.append(char)
            clean = "".join(string_list)
    final_string_list.append(clean)
    final_string_tuple = (final_string_list[0], final_string_list[1], final_string_list[2])
    return final_string_tuple

if __name__ == "__main__":
    test = separate_characters("hola !!!brother, como estas?")
    print(test)