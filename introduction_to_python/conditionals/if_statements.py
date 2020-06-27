is_raining= False #change this to see changes
is_cold=False #change this to see changes in output in Windows Powershell

if is_raining:
    print("You will need an umbrella today!")

if is_cold:
    print("You will need a jumper today!")

temperature = 12 #change this number to see changes in output in Windows Powershell
if temperature <= 12:
    print("OMG it is actually slightly cool in Perth")
else: 
    print("ugh when can I wear my jeans?")


temperature = 16
windchill = 4

is_cold = (temperature - windchill) <16
is_raining= False
print(is_cold)

# if is_cold:
#     print("You wil need a jumper today!")
# else:
#     print:("No need for a jumper today!")


if is_cold and is_raining:
    print("just stay home.")
else:
    if is_raining:
        print("You will need an umbrella today!")
    if is_cold:
        print("You will need a jumper today!")