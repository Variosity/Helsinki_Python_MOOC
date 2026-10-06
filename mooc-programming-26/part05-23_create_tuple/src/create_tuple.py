def create_tuple(x: int, y: int, z: int):
    as_list = [x, y, z]
    the_sum = sum(as_list)
    smallest = min(as_list)
    largest = max(as_list)
    as_tuple = (smallest, largest, the_sum)
    return as_tuple


if __name__ == "__main__":

    print(create_tuple(1, 5, 3))