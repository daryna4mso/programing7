a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Введіть оператор: ")

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b == 0:
            print("Помилка")
        else:
            print(a / b)
    case _:
        print("Невідомий оператор")