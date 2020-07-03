#Q1
print('This program calculates the sum of the numbers entered and ends after inputting a blank' )
total = 0
while True:
   number = (input("Enter a number (blank if you wish to terminate program): "))
   if number != "":
       total += float(number) #equivalent to total=total + sum
   else:
       break # break out of while loop

print('The sum is', total)

#Q2
mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],["Rory", "rory@whippies.park"],
]

for mailing in mailing_list:
    print(f"{mailing[0]} : {mailing[1]}")
    
#Q3
names_list = ["Bob", "Tom", "Paul"]

names_list2= str(input("Please provide a name "))
names_list.append(names_list2)
names_list3= str(input("Please provide another name "))
names_list.append(names_list3)
names_list4= str(input("Please provide another name "))
names_list.append(names_list4)

for names in names_list:
    if names == "Bob":
        continue
    if names == "Paul":
        continue
    if names=="Tom":
        continue
    print(names)




#Q4
groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]


#for item in groceries:
 #   print(f"{item[0]} ${item[1]}")

for index,item in enumerate(groceries):
    print(f"{item[0]:<20} ${item[1]:.2f}")



print('This program calculates your total grocery shopping bill' )
total = 0 #Baby Spinach
while True:
   number = float(input(f"How many units of {groceries[0][0]} do you need?: "))
   if number == "":
       number = float(input(f"How many units of {groceries[1][0]} do you need?: ")) 
   else:
       break # break out of while loop

total = float((number)*groceries[0][1]) 

total2 = 0 #Hot Choc
while True:
   number2 = float(input(f"How many units of {groceries[1][0]} do you need?: "))
   if number2 == "":
       number2 = float(input(f"How many units of {groceries[2][0]} do you need?: ")) 
   else:
       break # break out of while loop

total2 = float((number2)*groceries[1][1]) 


total3 = 0 #Crackers
while True:
   number3 = float(input(f"How many units of {groceries[2][0]} do you need?: "))
   if number3 == "":
       number3 = float(input(f"How many units of {groceries[3][0]} do you need?: ")) 
   else:
       break # break out of while loop

total3 = float((number3)*groceries[2][1]) 

total4 = 0 #Bacon
while True:
   number4 = float(input(f"How many units of {groceries[3][0]} do you need?: "))
   if number4 == "":
       number4 = float(input(f"How many units of {groceries[4][0]} do you need?: ")) 
   else:
       break # break out of while loop

total4 = float((number4)*groceries[3][1]) 

total5 = 0 #Carrots
while True:
   number5 = float(input(f"How many units of {groceries[4][0]} do you need?: "))
   if number5 == "":
       number5 = float(input(f"How many units of {groceries[5][0]} do you need?: ")) 
   else:
       break # break out of while loop

total5 = float((number5)*groceries[4][1]) 

total6 = 0 #Oranges
while True:
   number6 = float(input(f"How many units of {groceries[5][0]} do you need?: "))
   if number6 == "":
       number6 = float(input(f"How many units of {groceries[6][0]} do you need?: ")) 
   else:
       break # break out of while loop

total6 = float((number6)*groceries[5][1]) 

total7 = float(total + total2 + total3 + total4 + total5 + total6)


print("====Izzy's Food Emporium=====")
print(f'Baby Spinach     ${total:0.2f}')
print(f'Hot Chocolate    ${total2:0.2f}')
print(f'Crackers         ${total3:0.2f}')
print(f'Bacon            ${total4:0.2f}')
print(f'Carrots          ${total5:0.2f}')
print(f'Oranges          ${total6:0.2f}')
print("=============================")
print(f'grand total      ${total7:0.2f}')

