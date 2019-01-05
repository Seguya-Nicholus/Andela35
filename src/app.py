# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it
import os
from tasks import todo_list, create_task,delete_task,mark_as_finished,delete_all_tasks,clear_screen # import other functions as well
from accounts import accounts, add_account,login  # import the function as well

def display_menu():
    
    print("""
    Select Option:
        1. Create a Task 
        2. Deleting a task 
        3. Marking a task finished 
        4. Deleting all tasks 
        5. Logout
        """)
    

def display_startup():
    print("=========================== WELCOME TO MY TODO-LIST APP ========================")
    print("""
    Make a Choice :
        1) Create User Account
        2) Login into the App
        3) Quit the App   
    """)
    Choice = input("Please Make a Choice : ")
    while 1:
        if Choice == '1':
            clear_screen()  
            """
            Let the person sign up. If there details do not exist,
            create an account for them

            E.g 
            """
            create_user()
            clear_screen()
            print("=========================== WELCOME TO MY TODO-LIST CONSOLE APP ========================")
            print("""
            Make a Choice :
                1) Create User Account
                2) Login into the App
                3) Quit the App   
            """)
            Choice = input("Please Make a Choice : ")

        elif Choice == '2':
            """
            Allow a person to input a name and a password
            E.g
            """
            login_user()
        elif Choice == '3':
            clear_screen()
            break
        else:
            clear_screen()
            print("****** Wrong Selection ,Please Make the right Choice !!!! ******")
            print("=========================== WELCOME TO MY TODO-LIST CONSOLE APP ========================")
            print("""
            Make a Choice :
                1) Create User Account
                2) Login into the App
                3) Quit the App   
            """)
            Choice = input("Please Make a Choice : ")
    


def main_app():
    #Write code that implements the selected option        
    """
    The above should appear as
        Select Options:
            1. Create Task
            2 .... 
            3 ....
            4 ....
            
        selection:
    """
    selection = input("\nPlease Make a selection : ")
    while selection not in (1,2,3,4,5):                              
        if selection == '1':
            clear_screen()
            create_task(input("\n\tPlease Add a Task to your List : "))
            print("Item Added Successfully ... ")
            display_menu()
            selection = input("\nMake a selection : ")
        elif selection == '2':
            clear_screen()
            delete_task()
            print("Task Deleted Successfully ... ")
            display_menu()
            selection = input("\nMake a selection : ")
        elif selection == '3':
            clear_screen()
            mark_as_finished(task)   
        elif selection == '4':                
            delete_all_tasks()
            clear_screen()
            print("Items Deleted Successfully ... ")
            display_menu()
            selection = input("\nMake a selection : ") 
        elif selection == '5':
            clear_screen()
            print("You have Successfully Logged Out of the System ... ")
            exit()
        elif selection < '1' or selection > '5':
            clear_screen()
            print("****** Please your selection is out of range ******")
            display_menu()
            selection = input("\nMake a selection : ")
        else:
            clear_screen()
            print("****** Please you have to make a selection ******")  
            display_menu()
            selection = input("\nMake a selection : ")

def create_user():
    print("\n ================= PLEASE ENTER YOUR USERNAME AND PASSWORD TO SIGNUP =============")
    name = input("\nPlease Enter your UserName: ")
    if name == "":
        print("\n############# Check Error Below  #############")
        print("***** Filed cannot be blank , Please input your preferred Username !!!! *****")
        name = input("\nPlease Enter your UserName: ")

    password = input("\nPlease Enter your password : ")
    # Check if password field is blank    
    if password == "" and name != "":
        print("\n############# Check Error Below  #############")
        print("***** Filed cannot be blank ,Please input your password !!!! *****")
        password = input("\nEnter your password : ")

    confirm_password = input("\nPlease Confirm your password : ")
    # Check if confirm password field is blank    
    if confirm_password == "" and password != "" and name != "":
        print("\n############# Check Error Below  #############")
        print("*****Filed cannot be blank ,Please confirm your password !!!! *****")
        confirm_password = input("\nPlease Confirm your password : ")
        # else:
        #     pass
        # Check if confirm password field is the same as password   
    if confirm_password != password and name != "":
        print("\n############# Check Error Below  #############")
        print("**** Your Passwords Donot Match !!!! ****")
        confirm_password = input("\nPlease Confirm your password : ")
    
    # If username and password doesnot exist then create one
    add_account(name,password)


def login_user():
    clear_screen()
    print("\n================= PLEASE ENTER YOUR USERNAME AND PASSWORD TO LOGIN =============")    
    name = input("Enter your name: ")
    # Check if username field is blank
    if name == "":
        print("***** Filed cannot be blank ,Please input your username !!!! *****")
        name = input("\nEnter your name: ")
    else:
        pass    
    password = input("\nEnter your password : ")
        # Check if password field is blank    
    if password == "" and name != "":
        print("***** Filed cannot be blank ,Please input your password !!!! ***** ")
        password = input("\nEnter your password : ")
    else:
        pass
    login(name,password)
    if login(name,password) == True:
        clear_screen()
        print("\n================= WELCOME " + name.upper() + " PLEASE MAKE A SELECTION =====================")
        display_menu()
        main_app()
    else:
        pass
    clear_screen()
    print("\n\t******Username and Password doesnot exit !!! ******")
    display_startup()

#=============================== MAIN PROGRAM ========================================

if __name__ == "__main__":
    clear_screen()
    add_account("brian", "ndela35$$")
    add_account("seguya", "256")
    add_account("nakandi", "123")
    display_startup()
    

