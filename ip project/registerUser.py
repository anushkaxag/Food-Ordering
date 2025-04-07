
from database.addUser import addUser

def registerUser():
    name = input("Enter Name: ")
    email = input("Enter E-mail: ")
    phone = input("Enter Phone Number: ")
    password = input("Enter Password: ")

    addUser(name, email, phone, password)
    