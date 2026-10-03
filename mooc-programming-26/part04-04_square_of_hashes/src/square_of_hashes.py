# Copy here code of line function from previous exercise
def line(n, s):
    i = 0
    if s == "":
        s = '*'
    while i < n:
        i += 1
        for letter in s:
            print(letter, end="")
            break

def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = 0
    while i != size:
        i += 1
        line(size, "#")
        line(1, '\n')

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
