import time
# To do using list
to_do_list = []


# To display a task
def display_task():
    print(f"\n{"-"*35}\n{"Index":>6} | {"Status":12s} | {"Task":}\n{"+"*35}")
    for i in range(len(to_do_list)):
        print(f"{i:>6} | {to_do_list[i][1]:20s} | {to_do_list[i][0]:}")
    print("-"*35,"\n")

# To add a task
def add_task():
    to_do_list.append([input("Enter a task to add:"), "\x1b[31mINCOMPLETED\x1b[m"])


# To mark a task as completed
def mark():
    mark_choice = int(input("Please provide an index."))
    if to_do_list[mark_choice][1] == "\x1b[31mINCOMPLETED\x1b[m":
        a = input("Still not completed, do you want to mark it as completed? y/n:\
->")
        if a == "y" or a == "Y":
            to_do_list[mark_choice][1] = "\x1b[32mCOMPLETED\x1b[m"
            print("Successfully Completed")
        else:
            print("Nothing changed")
    else:
        print("Already completed")


# To remove a task
def remove_task(index):
    print(f"Task {to_do_list.pop(index)[0]} removed successfully")


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
                index = int(
                    input(
                        "Enter the index of task you want to remove:\n\
-> "
                    )
                )
                remove_task(index)
            case 5:  # breaking the loop
                break  # or return 0
            case _:
                print("Please enter a valid choice!")

    print("Thank you for using the to do list")


menu()
# print("\x1b[?25l")
# while 1:
#     for r in range(255):
#         for g in range(255):
#             for b in range(255):
#                 print(f"\x1b[38;2;{r};{g};{b}mTHE MORE YOU KNOW\x1b[m",end="\r")
#                 # time.sleep(0.02)
# print("\x1b[?25h")
