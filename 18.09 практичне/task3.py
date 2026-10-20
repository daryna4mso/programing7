x = int(input("Введіть x: "))
y = int(input("Введіть y: "))

if x > 0 and y > 0:
    print("1 чверть")
elif x < 0 and y > 0:
    print("2 чверть")
elif x < 0 and y < 0:
    print("3 чверть")
elif x > 0 and y < 0:
    print("4 чверть")
elif x == 0 and y == 0:
    print("Початок координат")
elif x == 0:
    print("Точка лежить на осі Y")
else:
    print("Точка лежить на осі X")
