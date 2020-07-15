# def addition(a,b):
#     print(f"a:{a}, b:{b}")
#     result = float(a) + float(b)
#     #print(result)
#     return result 

# a=3
# b=5
# addition(a,b)
# addition_result = addition(b,a)
# print(addition_result)

# addition(2, 3)
# addition(4, 5)
# addition (6, 8)

# first_number= input("Pick a number: ")
# second_number= input("pick a number: ")
# addition(first_number, second_number)



# addition() # this line makes it run - this is calling the function

# def addition(a, b):
# a_plus_b = float(a) + float(b)
# print(a_plus_b)
# return a_plus_b

############ Even and Odds ############# 
# counter = 5
# while counter > 0:
#     if counter%2 == 0:
#         print(f"{counter} is an even number.")
#     else:
#         print(f"{counter} is an odd number.")
#     counter -= 1

# Version 2:
# def is_odd(number):
#     if number%2 == 0:
#         return False
#     else:
#         return True

# counter = 10
# while counter > 0:
#     if is_odd(counter):
#         print(f"{counter} is an odd number.")
#     else:
#         print(f"{counter} is an even number.")
#     counter -= 1


# def format_grocery_item(item_name, item_cost):
#     return(f"{item_name:<20} ${item_cost:.2f}")

# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]
# for item in groceries:
#     print(format_grocery_item(item[0], item[1]))


def temp_converter():
    temp_fahrenheit=float(input("Provide a temperature in Fahrenheit and I'll convert it to Celsius: "))
    celcius = (float(temp_fahrenheit -32)*5/9)
    print(celcius)
    return (celcius)

temp_converter()



sum = 0
counter = 0
stop = False
# Process loop
while (not stop):
    inputValue = input("Enter a number: ")

    if (inputValue == ""):
        stop = True
    else:
        sum += float(inputValue)
        counter += 1 # counter++ doesn't work in python
# Output calculation and display
if (counter != 0):
    mean = float(sum) / int(counter)
    print("Mean value is " + str(mean))
print("Have a great day!")


##
x = 1
while x == 1:
    first_number = input("What's the first number? ")
    try:
        n1 = int(first_number)
        x = 0
    except ValueError:
        try:
            n1 = float(first_number)
            x = 0
        except ValueError:
            print("This is not a number, try again")


x = 1
while x == 1:
    second_number = input("What's the second number? ")
    try:
        n2 = int(second_number)
        x = 0
    except ValueError:
        try:
            n2 = float(second_number)
            x = 0
        except ValueError:
            print("This is not a number, try again")


print(f"The sum of the two numbers is {n1 + n2}")
print()