import math

def hypotenuse(leg1: float, leg2: float):
    leg1 *= leg1
    leg2 *= leg2
    c2 = leg1 + leg2
    return math.sqrt(c2)

if __name__ == "__main__":
    print(hypotenuse(2, 4))