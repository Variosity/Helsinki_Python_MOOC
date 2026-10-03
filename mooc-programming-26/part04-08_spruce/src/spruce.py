# Write your solution here

def spruce(n):
    print('a spruce!')
    i = -2
    x = n - 1
    print(x * ' ' + '*')
    x = n - 1
    c = 1
    while c < n:
        c += 1
        i += 2
        x -= 1
        print(x * ' ' + '*' * (i+2) + '*')

    x = n - 1
    print(x * ' ' + '*')


    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)