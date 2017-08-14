#This program converts inches to centimeters & pounds to kilograms
import sys

#passing string value to float data type, converts the string into flote type.
data = float(input("please enter the number of inches you wanted to convert to centimeters: ")) 

# 1 inch = 2.54 centimeters
inch = 2.54

total = data * inch

print("centimeters: ", total)

# passing string value to float data type, converts the string into float type.
data1 = float(input("please enter number of pounds you wanted to convert kgs: "))

# 1 pound = 0.453592 kg              
pound = 0.453592

total1 = data1 * pound

print("Kilograms: ", total1)
