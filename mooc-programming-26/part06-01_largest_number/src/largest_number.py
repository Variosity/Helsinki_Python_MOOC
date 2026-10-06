def largest():
    with open("numbers.txt") as numbers:
        num_list = []
        for nums in numbers:
            num_list.append(nums)
    return int(max(num_list))

if __name__ == "__main__":
    print(largest())