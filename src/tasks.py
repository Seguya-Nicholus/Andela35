import os
# --- tasks.py ---
# This file contains code that manages your todo_list
todo_list = []

def clear_screen():
    osname = os.name
    if osname == 'posix':
        os.system('clear') # For Linux/OS X
    elif osname == 'nt' or osname == 'dos':
        os.system('cls') # For Windows
    else:
        print("\n" * 30)

# Write a function creates a task


def create_task(task):
    """
    Adds the task (string value) to todo_list
    """
    Space = '\t'
    if task == "":
        print("\nPlease Field cannot be Blank,you have to input a Task!!!!!!!")
    else:
        todo_list.append(task)
        No_of_items = str(len(todo_list))
        print("\n======= Your to_do_list has " + No_of_items + " Item(s) =======")
        print("-----------------------------")
        print("Index    Item")
        print("-----------------------------")
        for index,item in enumerate(todo_list):
            print(index ,Space, item ,end='\n')
        print("\n-----------------------------")
        print(todo_list)
        print("======== End Of List ========")

# Write a function deletes a task


def delete_task():
    """
    Removes the specified task from the todo_list
    """
    Space = '\t'
    No_of_items = str(len(todo_list))
    print("\n======= Your to_do_list has " + No_of_items + " Item(s) =======")
    print("-----------------------------")
    print("Index    Item")
    print("-----------------------------")
    for index,item in enumerate(todo_list):
        print(index ,Space, item ,end='\n')
    print("\n-------------------------------")
    print(todo_list)
    print("=========== End Of List =======")
    
    task = int(input("\n\n\t Please Input the Index of the Task to be Deleted from List : "))
    if type(task) is not int:
        print("\n ****** Wrong Input, you have to input the Index of the Task to be Deleted from List !!!!!!! ******")
        task = int(input("\n\t Please Input the Index of the Task to be Deleted from List : "))
    else:
        clear_screen()
        del todo_list[task]
        No_of_items = str(len(todo_list))
        print("\n======= Your to_do_list has " + No_of_items + " Item(s) =======")
        print("-----------------------------")
        print("Index    Item")
        print("-----------------------------")
        for index,item in enumerate(todo_list):
            print(index ,Space, item ,end='\n')
        print("\n-------------------------------")
        print(todo_list)
        print("=========== End Of List =======")

# Write a function that marks a task finished


def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task 
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    

# Write a function deletes all tasks


def delete_all_tasks():
    """
    Empty the the todo_lsit
    """
    Space = '\t'
    del_tasks = (input("Are sure you want to delete all Items in the List ? Yes or No : "))
    if del_tasks == 'Yes' or  del_tasks == 'yes' or del_tasks == 'YES' or del_tasks == 'Y' or del_tasks == 'y':
        del todo_list[:]
        No_of_items = str(len(todo_list))
        print("\n======= Your to_do_list has " + No_of_items + " Item(s) =======")
        print("-----------------------------")
        print("Index    Item")
        print("-----------------------------")
        for index,item in enumerate(todo_list):
            print(index ,Space, item ,end='\n')
        print("\n-------------------------------")
        print(todo_list)
        print("=========== End Of List =======")
    elif del_tasks == 'No' or  del_tasks == 'no' or del_tasks == 'NO' or del_tasks == 'n' or del_tasks == 'N':
        No_of_items = str(len(todo_list))
        print("\n======= Your to_do_list has " + No_of_items + " Item(s) =======")
        print("-----------------------------")
        print("Index    Item")
        print("-----------------------------")
        for index,item in enumerate(todo_list):
            print(index ,Space, item ,end='\n')
        print("\n-------------------------------")
        print(todo_list)
        print("=========== End Of List =======")
    else:
        print("****** Please your selection is out of range ,Make the right selection !!!! ******")
        del_tasks = (input("Are sure you want to delete all Items in the List ? Yes or No : "))

    