from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper))
    weekly_draw = sample(number_pool, amount)
    sort = weekly_draw.sort()
    return weekly_draw

if __name__ == "__main__":
    pass