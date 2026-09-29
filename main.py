import sys
from models.tracker import Tracker
from utils.ui import print_menu, clr_screen

def main():
    clr_screen()
    print("****************************************")
    print("        VIT ACADEMIC TRACKER")
    print("****************************************")
    
    name = input("Enter your name: ").strip()
    reg = input("Enter your registration number: ").strip()
    
    app = Tracker(name, reg)

    while True:
        print_menu()
        try:
            opt = int(input("Pick an option (1-7): "))
            if opt == 1:
                app.dashboard()
            elif opt == 2:
                app.add_task()
            elif opt == 3:
                app.view_tasks("pending")
            elif opt == 4:
                app.view_tasks("all")
            elif opt == 5:
                app.mark_done()
            elif opt == 6:
                app.log_hours()
            elif opt == 7:
                app.save_data()
                clr_screen()
                print("Data saved. Bye!")
                sys.exit(0)
            else:
                print("Wrong choice. Pick between 1 and 7.")
                input("Press Enter...")
        except:
            print("Please type a number.")
            input("Press Enter...")

if __name__ == "__main__":
    main()