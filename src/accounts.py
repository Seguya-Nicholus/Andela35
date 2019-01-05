# --- accounts.py --
# This file contains code for managing your account
accounts = {}  # dictionary where key is the  password and value is User

# Write a function adds user details to accounts


def add_account(name, password):
    """
    Adds the key value pair to the accounts dictionary
    """
    #check if name exits before adding an account
    if name in accounts.values():
        print("UserName already exits.Please Choose a different Username !")
        
    elif password in accounts.keys():
        print("Password already exits.Please Choose a different Password !")
    else:
        accounts[password] = name

def login(name, password):
    """
    returns true if the password and corresponding name exist in the 
    accounts dicitionary
    """
    if password in accounts and name == accounts[password]:
        return True
    else:
        return False
        