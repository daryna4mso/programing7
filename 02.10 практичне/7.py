import math

def calculate_buses(people, bus_capacity):
    buses = people / bus_capacity
    return math.ceil(buses)