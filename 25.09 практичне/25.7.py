m = int(input("Введіть кількість чисел: "))

numbers = []

for i in range(m):
    x = float(input("Введіть число: "))
    numbers.append(x)

average = sum(numbers) / m

sum_squares = 0

for x in numbers:
    sum_squares += (x - average) ** 2

variance = sum_squares / (m - 1)
standard_deviation = variance ** 0.5

print("Дисперсія:", variance)
print("Стандартне відхилення:", standard_deviation)