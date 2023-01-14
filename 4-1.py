name = input("enter name = ")
family = input("enter family = ")
age = float(input("enter age = "))
city = input("enter city = ")
average = float(input("enter average = "))



if average == 20 :
    average1 = 20
    
else :
    if age < 15 :
        average1 = average + 1
        if average1 > 20 :
            average1 = 20

    if 15 <= age < 25 :
        average1 = average + 2

    if 25 <= age < 35 :
        average1 = average + 3

    if 35 <= age < 45 :
        average1 = average + 4

    if age >= 45 :
        average1 = average
    
    if average1 > 20 :
        average1 = 20



print("your name is", name, family, "age:", age, "city:", city, "average:", average1)