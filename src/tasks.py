# --- tasks.py ---
# This file contains code that manages your todo_list
todo_list = []

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
    while True:
        try:
            task = int(input("\n\t Please Input the Index of the Task to be Deleted from List : "))       
        except ValueError:
            print("\n Wrong Input, you have to input the Index of the Task to be Deleted from List !!!!!!!")
            continue
        else:
            if task < 0 or task > len(todo_list):
                print("\n Wrong Input, your input is out of range !!!!!!!")
                continue
            else:
                return task 
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
                break 
    # task = int(input("\n\t Please Input the Index of the Task to be Deleted from List : "))
    # if type(task) is not int:
    #     print("\n Wrong Input, you have to input the Index of the Task to be Deleted from List !!!!!!!")
    #     task = int(input("\n\t Please Input the Index of the Task to be Deleted from List : "))
    # else:
    #     del todo_list[task]
    #     No_of_items = str(len(todo_list))
    #     print("\n======= Your to_do_list has " + No_of_items + " Item(s) =======")
    #     print("-----------------------------")
    #     print("Index    Item")
    #     print("-----------------------------")
    #     for index,item in enumerate(todo_list):
    #         print(index ,Space, item ,end='\n')
    #     print("\n-------------------------------")
    #     print(todo_list)
    #     print("=========== End Of List =======")

# Write a function that marks a task finished


def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task 
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    pass

# Write a function deletes all tasks


def delete_all_tasks():
    """
    Empty the the todo_lsit
    """
    # del_tasks = (input("Are sure you want to delete all Items in the List ? Yes or No : "))
    #     if del_tasks == 'Yes' or  del_tasks == 'yes' or del_tasks == 'YES' or del_tasks == 'Y' or del_tasks == 'y':
    #         del todo_list[:]
    # print(todo_list)