
#Import libraries and neccessary functions
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import pickle
from datetime import datetime

#Function to add task to To-do list
def add_task():
    task = task_field.get()
    due_date = due_date_entry.get()
    if task != "":
        task_with_date = f"{task} (Due on: {due_date})"
        task_listbox.insert(tk.END, task_with_date)
        task_field.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning(title="Warning", message="You must enter a task and its Due date")

#Function to delete tasks from task list
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning(title="Warning", message="You must select a task.")

#Function to Save tasks to a file
def save_task():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.dat", "wb") as file:
        pickle.dump(tasks, file)

#Function to load task from file
def load_task():
    try:
        with open("tasks.dat", "rb") as file:
            tasks = pickle.load(file)
            task_listbox.delete(0, tk.END)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="Cannot find file")

#Funtion to mark completed Tasks
def mark_completed():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_task = task_listbox.get(selected_index)
        completed_task = selected_task.replace("(Due on: ", "(Completed: ")
        task_listbox.delete(selected_index)
        task_listbox.insert(tk.END, completed_task)
    else:
        messagebox.showwarning(title="warning", message="You must select a Completed task ")

#Fuction to Edit tasks
def edit_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_task = task_listbox.get(selected_index)
        edited_task = simpledialog.askstring("Edit Task", "Edit Task:", initialvalue=selected_task)

        if edited_task:
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, edited_task)
    else:
            messagebox.showwarning(title="warning", message="Select a task to Edit")

#Function to Sort task by due date
def sort_by_due_date():
 try:
    tasks = list(task_listbox.get(0, tk.END))
    tasks.sort(key=lambda x: datetime.strptime(x.split("(Due on: ")[1].split(")")[0], "%Y-%m-%d"))
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)
 except:
    messagebox.showwarning(title="warning", message="Invalid Date format")

 # Save tasks to file
    save_task()

# Create GUI
root = tk.Tk()
root.title("To-Do List")


# Frames
header_frame = ttk.Frame(root, style="My.TFrame")
functions_frame = ttk.Frame(root, style="My.TFrame")
listbox_frame = ttk.Frame(root, style="My.TFrame")

header_frame.pack(fill="both")
functions_frame.pack(side="left", expand=True, fill="both")
listbox_frame.pack(side="right", expand=True, fill="both")

# Labels
header_label = ttk.Label(header_frame, text="Daily Planner", font=("Brush Script MT", 32),
                         background="pink", foreground="#8B4513")
header_label.pack(padx=20, pady=20)

listbox_label = ttk.Label(listbox_frame, text="To-Do List:", font=("Consolas", 12, "bold"),
                         background="pink", foreground="#A52A2A")
listbox_label.pack(padx=10, pady=10)

task_label = ttk.Label(functions_frame, text="Enter the Task:", font=("Consolas", 11, "bold"),
                       background="pink", foreground="#000000")
task_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

due_date_label = ttk.Label(functions_frame, text="Due Date(yyyy-mm-dd):", font=("Consolas", 11, "bold"),
                            background="pink", foreground="#000000")
due_date_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

# Entry field
task_field = ttk.Entry(functions_frame, font=("Consolas", 12), width=18,
                       background="pink", foreground="#A52A2A")
task_field.grid(row=0, column=1, pady=10, padx=10)

due_date_entry = ttk.Entry(functions_frame, font=("Consolas", 12), width=18,
                            background="pink", foreground="#A52A2A")
due_date_entry.grid(row=1, column=1, pady=10, padx=10)

# Buttons
add_button = ttk.Button(functions_frame, text="Add Task", command=add_task)
save_button = ttk.Button(functions_frame, text="Save Task", command=save_task)
load_button = ttk.Button(functions_frame, text="Load Task", command=load_task)
mark_completed_button = ttk.Button(functions_frame, text="Mark Completed Tasks", command=mark_completed)
edit_button = ttk.Button(functions_frame, text="Edit Task", command=edit_task)
delete_button = ttk.Button(functions_frame, text="Delete Task", command=delete_task)
sort_by_due_date_button = ttk.Button(functions_frame, text="Sort by Due Date", command=sort_by_due_date)
exit_button = ttk.Button(functions_frame, text="Exit", command=root.destroy)

# Listbox
task_listbox = tk.Listbox(listbox_frame, width=50, height=20, font=("Consolas", 12), selectmode='SINGLE',
                          background="#FFFFFF", foreground="#A52A2A", selectbackground="#CD853F",
                          selectforeground="#FFFFFF")
task_listbox.pack(padx=10, pady=10)

# Scrollbar
scrollbar_tasks = tk.Scrollbar(listbox_frame)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=task_listbox.yview)

# Pack buttons
add_button.grid(row=2, column=0, columnspan=1, rowspan=1)
save_button.grid(row=2, column=1, columnspan=2, rowspan=1)
load_button.grid(row=3, column=0, columnspan=1, rowspan=1)
mark_completed_button.grid(row=3, column=1, columnspan=2, rowspan=1)
edit_button.grid(row=4, column=0, columnspan=1, rowspan=1)
delete_button.grid(row=4, column=1, columnspan=2, rowspan=1)
sort_by_due_date_button.grid(row=5, column=1, columnspan=2, rowspan=1)
exit_button.grid(row=5, column=0, columnspan=1, rowspan=1)

root.mainloop()
