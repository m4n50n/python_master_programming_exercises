import math

def car_route(km, length):
  return math.ceil(length / km)

print(car_route(700, 750))
