# Write your solution here
def line(n, s):
    i = 0
    if s == "":
        s = '*'
    while i < n:
        i += 1
        for letter in s:
            print(letter, end="")
            break
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")