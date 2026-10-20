import random

def get_daily_discount():
    number = random.randint(1,10)

    if number <= 10:
        return "Ваша знижка: 50%"
    elif number <= 30:
        return "Ваша знижка: 20%"
    else:
        return "Ваша знижка: 5%"