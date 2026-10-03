# Write your solution here

def longests(strings : list):
    longest_string_finder = []
    for string in strings:
        longest_string_finder += [len(string)]
    longest_string = max(longest_string_finder)
    return longest_string

def longest(strings : list):
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest


if __name__ == '__main__':
    strings = ['first', 'second', 'third']
    print(longest(strings))