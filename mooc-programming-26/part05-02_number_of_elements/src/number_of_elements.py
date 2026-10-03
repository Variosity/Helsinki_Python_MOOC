def count_matching_elements(my_matrix: list, element: int):
    i = 0
    for row in my_matrix:
        for lmnt in row:
            if lmnt == element:
                i += 1
    return i


if __name__ == "__main__":
    the_matrix = [[6, 9, 3], [9, 3, 6], [4, 2, 3]]
    print(count_matching_elements(the_matrix, 3))