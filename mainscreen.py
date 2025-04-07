
from registerUser import registerUser
from orderFood import orderFood

while True:
    print("\n**********************************")
    print("\n* ONLINE FOOD ORDER SYSTEM \U0001F642 *")
    print("\n**********************************")

    print("\n\n")

    print("Choose Option:")
    print("1.\t Register User")
    print("2.\t Place Order")
    print("3.\t Exit ")
    


    optionChosen = int(input("Option: "))


    if optionChosen == 1: registerUser()
    if optionChosen == 2: orderFood()
    if optionChosen == 3: exit()








    