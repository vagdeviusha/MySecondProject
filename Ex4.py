#Assigning value 100 to cars variable
cars = 100

# Space in a car
space_in_a_car = 4.0

#Number of drivers
drivers = 30

#Numbe of passengers
passengers = 90

#Total number of cars which are not driven
cars_not_driven = cars - drivers

#Total number of cars driven
cars_driven = drivers

#Total capacity in all the cars
carpool_capacity = cars_driven * space_in_a_car

#Average passengers in a car.
average_passengers_per_car = passengers / cars_driven




#This line will print the number of cars available
print("There are", cars, "cars available")

#This line provides number of drivers available
print("There are only", drivers, "drivers available")

#This line gives the number of empy cars today
print("There will be", cars_not_driven, "empty cars today")

#number of people transporting today
print("We can transport", carpool_capacity, "people today")

#number of paasengers in car pool
print("we have", passengers, "to carpool today")

#Average passengers in each car
print("We need to put about", average_passengers_per_car, "in each car")


