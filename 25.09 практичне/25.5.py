pi = 2
product = 1

for n in range(1, 10001):
    product = product * (4 * n ** 2) / (4 * n ** 2 - 1)

    if n % 100 == 0:
        pi_approx = 2 * product
        print(n, pi_approx)