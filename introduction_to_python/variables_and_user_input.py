#Q1 Write a program that takes two numbers from the user, and outputs their sum
first_value = float(input("To find the sum of two numbers, please enter your first number "))

second_value = float(input("Now enter your second number "))

#number1=float(number1)
#number2=float(number2)

result= (first_value + second_value)
print(f"Your result is {result}" )


#Q2 Write a program that takes two numbers from the user,
# and outputs the equation representing the multiplication of the two numbers
first = float(input("To find the product of two numbers, please enter your first number "))

second = float(input("Now enter your second number "))

result= (first * second)
print(f"{first} * {second} = {result}")


#Q3 Write a program that takes a distance in kms form the user and the output distance is in meters and cms
km = float(input("Hey give me a number in kilometers and I will convert it to meters and centimeters for you "))

result1= int(km * 1000)
result2= int(km * 100000)
print(f"{km}km = {result1}m")
print(f"{km}km = {result2}cm")

#Q4 Write a program that takes th users name and height in cms and outputs a sentence
name = input("What is your name? ")

height_prompt = f"Hi {name}, what is your height in centimeters? "
height=input(height_prompt)

print(f"{name} is {height}cms tall.")
