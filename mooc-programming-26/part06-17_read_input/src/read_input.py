def read_input(message, x, y):
    while True:
        try:
            input_s = input(message)
            num = int(input_s)
            if num >= x and num <= y:
                print(f'You typed in number: {num}')
                return num
        except ValueError:
            pass
        print(f'You must type in an integer between {x} and {y}')

if __name__ == '__main__':
    read_input(1, 4)