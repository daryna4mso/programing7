a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    solutions = (x1, x2)
elif D == 0:
    x = -b / (2 * a)
    solutions = (x,)
else:
    solutions = ()

print(solutions)