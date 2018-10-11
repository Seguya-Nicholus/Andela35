# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it

from tasks import todo_list, create_task,delete_task,mark_as_finished,delete_all_tasks # import other functions as well
from accounts import accounts, add_account,login  # import the function as well


if __name__ == "__main__":
    """
        Allow a person to input a name and a password

        E.g
    """
    add_account("brian", "ndela35$$")
    add_account("seguya", "256")
    add_account("nakandi", "123")
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
    # else:
    login(name,password)
    
    # Check if username and password exists then login
    if login(name,password) == True:

        """
        Let the person sign in. If there details do not exist,
        create an account for them

        E.g 
        """
        print("\n================= WELCOME " + name.upper() + " PLEASE MAKE A SELECTION =====================")
        print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
    
        # ..... skipped code
        # selection = input("Make a selection: ")
        selection = input("\nMake a selection : ")
            
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
        
        while selection not in (1,2,3,4,5):                              
            if selection == '1':
                create_task(input("\n\tPlease Add a Task to your List : "))
                print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
                selection = input("\nMake a selection : ")
            elif selection == '2':
                delete_task()
                print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
                selection = input("\nMake a selection : ")
            elif selection == '3':
                mark_as_finished(task)   
            elif selection == '4':
                delete_all_tasks() 
            elif selection == '5':
                exit()
            elif selection < '1' or selection > '5':
                print("****** Please " + name.upper() + " your selection is out of range ******")
                print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
                selection = input("\nMake a selection : ")
            else:
                print("****** Please " + name.upper() + " you have to make a selection ******")  
                print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
                selection = input("\nMake a selection : ")  
        
        
    else:
        print("\n *********** Username and Password doesn't Exit !!!! ************")
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
    

        """
        Provide options:
            1. creating a task
            2. deleting a task 
            3. deleting all tasks
            4. Marking a task finished
        
        E.g
        """
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
        # else:
        login(name,password)
    
        # Check if username and password exists then login
        if login(name,password) == True:

            """
            Let the person sign in. If there details do not exist,
            create an account for them

            E.g 
            """
            print("\n================= WELCOME " + name.upper() + " PLEASE MAKE A SELECTION =====================")
            print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
    
        # ..... skipped code
        # selection = input("Make a selection: ")
            selection = input("\nMake a selection : ")
            
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
        
            while selection not in (1,2,3,4,5):
                # Select 1 to Add a task to your list                              
                if selection == '1':
                    create_task(input("\n\t Please Add a Task to your List : "))
                    print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
                    selection = input("\nMake a selection : ")
                # Select 2 to Delete a task from the list
                elif selection == '2':
                    delete_task()
                    print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
                    selection = input("\nMake a selection : ")
                # select 3 to mark an item as finished
                elif selection == '3':
                    mark_as_finished(task)  
                # select 4 to delete all tasks 
                elif selection == '4':                     
                    delete_all_tasks()
                    print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
                    selection = input("\nMake a selection : ")
                    # else:
                    #     print("Please " + name.upper() + " Choose Yes or No to continue")
                # select 5 exit program
                elif selection == '5':
                    exit()
                # if selction is out of range
                elif selection < '1' or selection > '5':
                    print("****** Please " + name.upper() + " your selection is out of range ******")
                    print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
                    selection = input("\nMake a selection : ")
                #if no selection is made  
                else:
                    print("****** Please " + name.upper() + " you have to make a selection ******")  
                    print("Select Option: \n\t1. Create a Task \n\t2. Deleting a task \n\t3. Marking a task finished \n\t4. Deleting all tasks \n\t5. Exit App")
                    selection = input("\nMake a selection : ")
        

