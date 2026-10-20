import math

def calculate_trip_cost(distance, fuel_consumption, fuel_price):
    fuel = distance / 100 * fuel_consumption
    cost = fuel * fuel_price
    return math.ceil(cost)

print(calculate_trip_cost(140, 8, 100))