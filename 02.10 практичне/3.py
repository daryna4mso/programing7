def check_baggage(*weights):
    total = 0
    for w in weights:
        total += w
    return total <= 50

print(check_baggage(10, 5, 20))
print(check_baggage(30, 25))
