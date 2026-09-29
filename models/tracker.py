import array
from datetime import datetime
from models.task import Task
from utils.storage import load_json, save_json
from utils.ui import clr_screen

class Tracker:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no
        self.tasks = {}
        self.task_counter = 1
        self.study_hours = array.array("d", [])
        self.filename = f"{self.reg_no}_data.json"
        self.load_data()

    def save_data(self):
        data = {
            "task_counter": self.task_counter,
            "tasks": {str(k): v.get_dict() for k, v in self.tasks.items()},
            "study_hours": self.study_hours.tolist()
        }
        save_json(self.filename, data)

    def load_data(self):
        data = load_json(self.filename)
        if data:
            self.task_counter = data.get("task_counter", 1)
            self.study_hours = array.array("d", data.get("study_hours", []))
            for k, v in data.get("tasks", {}).items():
                t = Task(
                    v["task_id"], v["title"], v["category"],
                    v["deadline"], v["priority"], v["is_completed"]
                )
                self.tasks[int(k)] = t

    def add_task(self):
        clr_screen()
        print("--- Add New Task ---")
        title = input("Enter task name: ").strip()
        category = input("Category (like Coding, Physics, etc.): ").strip()
        
        while True:
            deadline = input("Deadline (DD-MM-YYYY): ").strip()
            try:
                datetime.strptime(deadline, "%d-%m-%Y")
                break
            except:
                print("Oops, wrong format. Try DD-MM-YYYY")

        while True:
            try:
                priority = int(input("Priority (1 for High, 2 for Med, 3 for Low): "))
                if priority in [1, 2, 3]:
                    break
                print("Just enter 1, 2, or 3")
            except:
                print("Enter a valid number please")

        t = Task(self.task_counter, title, category, deadline, priority)
        self.tasks[self.task_counter] = t
        self.task_counter += 1
        self.save_data()
        print(f"\nTask '{title}' added!")
        input("Press Enter to go back...")

    def view_tasks(self, mode="all"):
        clr_screen()
        print(f"--- My Tasks ({mode}) ---")
        if len(self.tasks) == 0:
            print("No tasks yet.")
            input("\nPress Enter...")
            return

        print(f"{'ID':<4} | {'Title':<20} | {'Category':<12} | {'Deadline':<10} | {'Status'}")
        print("-" * 65)
        
        shown = 0
        for tid, t in self.tasks.items():
            if mode == "pending" and t.is_completed:
                continue
            if mode == "completed" and not t.is_completed:
                continue
                
            stat = "Done" if t.is_completed else "Pending"
            print(f"{tid:<4} | {t.title:<20} | {t.category:<12} | {t.deadline:<10} | {stat}")
            shown += 1
            
        if shown == 0:
            print("Nothing to show here.")
        print("-" * 65)
        input("Press Enter...")

    def mark_done(self):
        clr_screen()
        print("--- Mark Task Done ---")
        pending = [t for t in self.tasks.values() if not t.is_completed]
        if len(pending) == 0:
            print("All caught up! No pending tasks.")
            input("Press Enter...")
            return

        print("Here are your pending tasks:")
        for t in pending:
            print(f"[{t.task_id}] {t.title} (Due: {t.deadline})")
            
        try:
            choice = int(input("\nEnter the ID of the task you finished: "))
            if choice in self.tasks and not self.tasks[choice].is_completed:
                self.tasks[choice].mark_done()
                self.save_data()
                print(f"Nice! Task {choice} is marked done.")
            else:
                print("Invalid ID or it's already done.")
        except:
            print("Enter a real number.")
        input("Press Enter...")

    def log_hours(self):
        clr_screen()
        print("--- Log Study Hours ---")
        try:
            hrs = float(input("How many hours did you study just now? "))
            if hrs > 0:
                self.study_hours.append(hrs)
                self.save_data()
                print(f"Logged {hrs} hours. Keep it up!")
            else:
                print("Enter something greater than zero.")
        except:
            print("Enter a valid number like 1.5 or 2")
        input("Press Enter...")

    def dashboard(self):
        clr_screen()
        print("==================================================")
        print(f"   My Dashboard - {self.name} ({self.reg_no})")
        print("==================================================")

        total = len(self.tasks)
        done = sum(1 for t in self.tasks.values() if t.is_completed)
        left = total - done
        prog = (done / total * 100) if total > 0 else 0.0

        bars = int(20 * prog // 100)
        bar_str = '█' * bars + '-' * (20 - bars)

        total_hrs = sum(self.study_hours)
        avg_hrs = total_hrs / len(self.study_hours) if len(self.study_hours) > 0 else 0

        print(f"Progress : [{bar_str}] {prog:.1f}%")
        print(f"Total    : {total}")
        print(f"Done     : {done}")
        print(f"Pending  : {left}")
        print("--------------------------------------------------")
        print(f"Study Sessions : {len(self.study_hours)}")
        print(f"Total Hours    : {total_hrs:.1f} hrs")
        print(f"Avg / Session  : {avg_hrs:.1f} hrs")
        print("==================================================")
        input("Press Enter...")
