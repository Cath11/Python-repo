#Q1 Kate's cat, Roary, loves catching moths. Write a program that determines whether or not it is thime for catching moths.
moths_in_house = False
if moths_in_house: 
    print("Get the moths!")
else: 
    print("No threats detected")

 #Q2 Amend the previous program to determine whethe ror not it is time for Roary to go moth hunting.

moths_in_house = False
mitch_is_home = True
if moths_in_house and mitch_is_home: 
    print("Hooman! Help me get the moths!")
if not moths_in_house and not mitch_is_home: 
    print("No threats detected!")
if moths_in_house and not mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
if not moths_in_house and mitch_is_home:
    print("Climb on Mitch")

#Q3 Write a program that implements the algorithm for Red Light Cameras.

light_colour = True
car_detected = True
if light_colour and car_detected:
    print("Flash!")
else:
    print("Do nothing.")

#Q4 Write a program that asks the user for their height, 
# and determine whether or not they are tall enough to ride the rollercoaster, 
# which has a height requirmeent of 120cms.
height = int(input(f"Hi, what is your height in centimeters? "))
if height >=120:
    print("Hop on!")
if height < 120:
    print("Sorry, not today short stuff :(")