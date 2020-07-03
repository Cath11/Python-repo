#Q1
foods = ["orange", "apple", "banana","strawberry","grape","blueberry",
["carrot", "cauliflower", "pumpkin"],
"passionfruit","mango","kiwifruit"]

print(foods)
print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])

foods_sublist=["carrot", "cauliflower", "pumpkin"]
print(foods_sublist[-1])

#Q2
mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus" , "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw" , "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory" , "rory@whippies.park"],
]


print(mailing_list[0][0:2], sep=":")
print(mailing_list[1][0:2])
print(mailing_list[2][0:2])
print(mailing_list[3][0:2])
print(mailing_list[4][0:2])

#Q3
names_list = ["Bob", "Tom", "Paul"]
print(names_list)

names_list2= str(input("Please provide a name "))
names_list.append(names_list2)
names_list3= str(input("Please provide another name "))
names_list.append(names_list3)
names_list4= str(input("Please provide another name "))
names_list.append(names_list4)
print(names_list)

#Q4a 
string_list= str(input("Please enter a string "))
sls= string_list.split()
print(len(sls))
print(sls)
 
res=list(string_list)
print(len(res))
print(res)

#Q4b
string_list2= str(input("Please enter a string "))
sls2= string_list2.split()
print(len(sls2))
print(sls2)
 
res=list(string_list2)
print(len(res))
print(res)
