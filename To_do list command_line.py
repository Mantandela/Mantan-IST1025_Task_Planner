# Import Library
import json
from datetime import datetime

# Global variable to store tasks
tasks = []

#Menu with options for to-do list
def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Save Tasks to File")
    print("5. Load Tasks from File")
    print("6. Mark Task as Completed")
    print("7. Edit Task Details")
    print("8. Sort Tasks by Due Date")
    print("9. Exit")

# Function to Add new tasks to the todo list
def add_tasks():
    description = input("Enter a New task: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        tasks.append({"description": description, "due_date": due_date, "completed": False})
        print("Task added successfully!")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Function to View Added task in todo list
def view_tasks():
    if not tasks:
        print("No Tasks Found.")
    else:
        print("\n===== Task List =====")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['description']} - Due Date: {task['due_date']} - {status}")

# Function to Remove added task from todo list
def remove_task():
    if not tasks:
        print("No tasks to remove.")
    else:
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]
                print("Task removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to Save Tasks on todo list to a file
def save_tasks():
    with open("project.json", "w") as file:
        json.dump(tasks, file, default=str)  # Serialize datetime objects to string
    print("Tasks saved successfully!")

# Funtion to load tasts from file
def load_tasks():
    global tasks
    try:
        with open("project.json", "r") as file:
            tasks = json.load(file)
            print("Tasks loaded successfully!")
            print("\n===== Task List =====")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['description']} - Due Date: {task['due_date']} - {status}")
    except FileNotFoundError:
        print("No saved tasks found.")
    except json.JSONDecodeError:
        print("Error decoding JSON. File might be corrupt.")

# Function to mark task as completed
def mark_completed():
    if not tasks:
        print("No tasks to mark as completed.")
    else:
        try:
            task_number = int(input("Enter the task number completed: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print(f"Task '{task_number}' marked as completed!")
            else:
                print(f"Task '{task_number}' not found.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to edit tasks in todo list
def edit_task():
    if not tasks:
        print("No tasks to edit.")
    else:
        task_name = input("Enter the task name to edit: ")
        for task in tasks:
            if task["description"] == task_name:
                new_name = input("Enter the new task name: ")
                new_due_date_str = input("Enter the new due date (YYYY-MM-DD): ")
                try:
                    new_due_date = datetime.strptime(new_due_date_str, "%Y-%m-%d")
                    task["description"] = new_name
                    task["due_date"] = new_due_date
                    print("Task details updated successfully!")
                    return
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
        print(f"Task '{task_name}' not found.")

# Function to Sort tasks by due date
def sort_tasks():
    if not tasks:
        print("No tasks to sort.")
    else:
        tasks.sort(key=lambda x: x["due_date"])
        print("Tasks sorted by due date.")

def main():
    while True:
        show_menu()
        option = input("Enter your option (1-9): ")

        if option == "1":
            add_tasks()
        elif option == "2":
            view_tasks()
        elif option == "3":
            remove_task()
        elif option == "4":
            save_tasks()
        elif option == "5":
            load_tasks()
        elif option == "6":
            mark_completed()
        elif option == "7":
            edit_task()
        elif option == "8":
            sort_tasks()
        elif option == "9":
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()

