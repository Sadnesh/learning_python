# To do using set
to_do_set= set()
count:int=0


# To display task
def display_task():
    print(f"\n{"-"*35}\n{"Id":>6} | {"Status":12s} | {"Task":}\n{"+"*35}")
    for i in to_do_set:
            print(f"{i[0]:>6} | {i[1]:20s} | {i[2]}")
    print("-"*35,"\n")


# To add task
def add_task():
    global count
    new_task=(f"{count}","\x1b[31mINCOMPLETED\x1b[m",input("Enter a task to add:")) 
    #makes two elements in set where one is incompleted
    to_do_set.add(new_task)
    count+=1


# To mark a task as completed
def mark(): # bruh cannot do this cause once set is made we cannot modify it but can only add or remove an item in it 
    Id = input("Please provide the name of task.")
    for task in to_do_set:
        if task[0]==Id:
            if task[1]=="\x1b[31mINCOMPLETED\x1b[m":
                to_do_set.remove(task)
                new_task=(task[0],"\x1b[32mCOMPLETED\x1b[m",task[2])
                to_do_set.add(new_task)
                print("Task successfully completed")
                break
            else:
                print("Task already completed")
                break
    else:
        print("Nothing changed")


# To remove a task
def remove_task(Id):
    for task in to_do_set:
        if task[0]==Id:
            to_do_set.discard(task)
            print(f"Task {task[2]} removed successfully")
            break
    else:
             print("Id not found. So nothing changed!")


# Menu
def menu():
    choice: int = 0
    while 1:
        choice = int(
            input("\n\
        ***********Menu***********\n\
        1. Display the to-do list.\n\
        2. Add a task to the to-do list.\n\
        3. Mark a task as completed. \n\
        4. Remove a task from the list.\n\
        5. Quit the application.\n\
->"
            )
        )
        match (choice):
            case 1:
                display_task()
            case 2:
                add_task()
            case 3:
                display_task()
                mark()
            case 4:
                display_task()
                index = input(
                        "Enter the id of task you want to remove:\n\
-> "
                    )
                remove_task(index)
            case 5:  # breaking the loop
                break  # or return 0
            case _:
                print("Please enter a valid choice!")

    print("Thank you for using the to do list")


menu()
