def times_ten(start_index: int, end_index: int):
    i = start_index
    dictionary = {}
    for nums in range(end_index + 1):
        if i > end_index:
            break
        dictionary[i] = i * 10
        i += 1
    return dictionary

if __name__ == "__main__":
    d = times_ten(0, 6)
    print(d)