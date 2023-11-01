# To do using list
to_do_dic:dict ={}
count:int=1

# To display a task
def display_task():
    print(f"\n{"-"*35}\n{"Index":>6} | {"Status":12s} | {"Task":}\n{"+"*35}")
    for i,j in to_do_dic.items():
         print(f"{i:>6} | {j[1]:20s} | {j[0]}")
    print("-"*35,"\n")

# To add a task
def add_task():
    global count
    to_do_dic[f"{count}"]=[input("Enter a task to add: "),"\x1b[31mINCOMPLETE\x1b[m"]
    count+=1
    # to_do_dic[input("Enter a task to add:")]="\x1b[31mINCOMPLETED\x1b[m"
    #task={input("Enter a task to add:"):"\x1b[31mINCOMPLETED\x1b[m"}
    #to_do_dic.update(task)


# To mark a task as completed
def mark():
    index = input("Please provide the index of the task.")
    if value:=to_do_dic.get(index):
        # value=to_do_dic.get(index)
        if value[1]== "\x1b[31mINCOMPLETE\x1b[m":
            a = input("Still not completed, do you want to mark it as completed? y/n:\
->")
            if a == "y" or a == "Y":
                value[1] = "\x1b[32mCOMPLETED\x1b[m"
                print("Successfully Completed")
            else:
                print("Nothing changed")
        else:
            print("Already completed")
    else:
        print("The index isn't present")


# To remove a task
def remove_task(index):
    if index in to_do_dic.keys():
        print(f"Task {to_do_dic.pop(index)[0]} removed successfully")


# Menu
def menu():
    choice: int = 0
    while 1:
        choice = int(
            input(
                "\n\
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
                        "Enter the index of task you want to remove:\n\
-> "
                    )
                remove_task(index)
            case 5:  # breaking the loop
                break  # or return 0
            case _:
                print("Please enter a valid choice!")

    print("Thank you for using the to do list")


menu()
