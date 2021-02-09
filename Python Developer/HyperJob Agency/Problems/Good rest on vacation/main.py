days = int(input())
food_cost = int(input())
flight_cost = int(input())
night_in_hotel = int(input())

print(days * food_cost + 2 * flight_cost + night_in_hotel * (days - 1))
