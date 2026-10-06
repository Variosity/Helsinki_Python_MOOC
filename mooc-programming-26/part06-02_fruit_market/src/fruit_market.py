def read_fruits():
    with open("fruits.csv") as fruit:
        fruit_dict = {}
        for item in fruit:
            item = item.replace("\n", "")
            selection = item.split(";")
            fruit_dict[selection[0]] = selection[1:]
        fruits = {key: float(value[0]) for key, value in fruit_dict.items()}
    return fruits

if __name__ == "__main__":
    print(read_fruits())