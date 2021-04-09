# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:57:51 2021

@author: Emeka Aladimma
"""
import random
from datetime import datetime
now = datetime.now()

symbol_processed = lambda value: chr(int(value, 16))
naira_symbol = symbol_processed("20A6")

database = {
        "seyi@zuriteam" : ["Seyi","Onifade","passwordSeyi",2343135679]
    }

def init():
    print("Welcome to Acel Bank")
    accountCheck = input("Do you have an account with us? \n 1) Yes \n 2) No \n")
    if int(accountCheck) == 1:
        login()
    elif int(accountCheck) == 2:
        register()
    else:
        print("Invalid input. Enter a number")
        init()
    
def login():
    print("********* Login ***********")
    emailFromUser = input("What is your email address? \n")
    passwordFromUser = input("What is your password? \n")
    
    for email,userDetails in database.items():
        if email == emailFromUser:
            if userDetails[2] == passwordFromUser:
                global currentUserName
                currentUserName = userDetails[0]
                menu(currentUserName)
    
def register():
    print("****** Register *******")
    firstName = input("Enter your first name - ")
    lastName = input("Enter your last name - ")
    email = input("Enter your email address - ")
    password = input("Enter your password - ")
    accountNumber = generateAccountNumber()
    
    database[email] = [firstName,lastName,password,accountNumber]
    print("Your Account registration was successful")
    init()
    
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

def menu(currentUserName):
    print("****** Menu *******")
    print(f"{now.hour}:{now.minute} {now.day}-{now.month}-{now.year}")
    print(f"Welcome {currentUserName}")
    print("These are the available options:")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Complaint")
    selectedOption()

def selectedOption():
        selectedOption = int(input("Please select an option "))
         
        if (selectedOption == 1):
            withdrawalAmount = float(input(f"How much would you like to withdraw \n{naira_symbol}"))
            print("Take your cash")
            menuReturn()
        elif (selectedOption == 2):
            depositAmount = float(input(f"How much would you like to deposit? \n{naira_symbol}"))
            currentBalance = round((random.random())*100000,2)
            print(f"Your current balance is {naira_symbol}{currentBalance}")
            menuReturn()
        elif  (selectedOption == 3):
            userComplaint = input("What issue will you like to report?\n")
            print("")
            menuReturn()
        else:
            print("Invalid Option selected, please try again")    
    
def menuReturn():
    print("")
    print("Would you like to return to the menu?")
    menuReturnOption = input("If yes, enter 1. Press 2 to close the program ")
    if int(menuReturnOption) == 1:
        menu(currentUserName)
    
init()
    
    