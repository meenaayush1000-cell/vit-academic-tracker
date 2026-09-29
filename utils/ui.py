import os

def clr_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clr_screen()
    print("==============================")
    print("          Main Menu")
    print("==============================")
    print(" 1. View Dashboard")
    print(" 2. Add New Task")
    print(" 3. View Pending Tasks")
    print(" 4. View All Tasks")
    print(" 5. Complete a Task")
    print(" 6. Log Study Hours")
    print(" 7. Save and Exit")
    print("==============================")
