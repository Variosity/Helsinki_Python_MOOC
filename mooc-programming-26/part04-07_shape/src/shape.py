# Copy here code of line function from previous exercise and use it in your solution
def line(n, s):
    i = 0
    if s == "":
        s = '*'
    while i < n:
        i += 1
        for letter in s:
            print(letter, end="")
            break

def shape(tsize, tchar, rsize, rchar):
    i = 0
    while i != tsize -1:
        i+=1
        line(i, tchar)
        line(1, '\n')
        
    line(tsize, tchar)
    line(1, '\n')
    x = 0
    while x != rsize:
        x+=1
        line(tsize, rchar)
        line(1, '\n')

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")