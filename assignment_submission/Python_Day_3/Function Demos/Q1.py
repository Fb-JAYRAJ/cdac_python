def add():
    print("Add function called.")

def modify():
    print("Modify function called.")

def delete():
    print("Delete function called.")

user_choice_q1 = input("Enter a number (1 for add, 2 for modify, 3 for delete): ")
if user_choice_q1.isdigit(): 
    choice_num_q1 = int(user_choice_q1)
    match choice_num_q1:
        case 1:
            add()
        case 2: 
            modify()
        case 3:
            delete()
        case _: 
            print("Invalid choice. Please enter 1, 2, or 3.")
else:
    print("Invalid input. Please enter a number.")
