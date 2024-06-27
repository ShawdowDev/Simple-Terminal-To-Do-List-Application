import os

# ANSI color codes for formatting
class color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

TODO_FILE = 'todo_list.txt'

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        tasks = [line.strip() for line in file]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def display_tasks(tasks):
    if not tasks:
        print(color.YELLOW + "No tasks found." + color.END)
    else:
        print(color.BOLD + "Current Tasks:" + color.END)
        for index, task in enumerate(tasks, 1):
            print(f"{color.BLUE}{index}. {task}{color.END}")

def add_task(tasks):
    task = input(color.GREEN + "Enter a new task: " + color.END)
    tasks.append(task)
    save_tasks(tasks)
    print(color.GREEN + "Task added." + color.END)

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input(color.GREEN + "Enter the number of the task to delete: " + color.END))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(color.GREEN + "Task deleted." + color.END)
        else:
            print(color.RED + "Invalid task number." + color.END)
    except ValueError:
        print(color.RED + "Invalid input. Please enter a number." + color.END)

def mark_task_complete(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input(color.GREEN + "Enter the number of the task to mark as complete: " + color.END))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1] += " [Completed]"
            save_tasks(tasks)
            print(color.GREEN + "Task marked as complete." + color.END)
        else:
            print(color.RED + "Invalid task number." + color.END)
    except ValueError:
        print(color.RED + "Invalid input. Please enter a number." + color.END)

def main():
    print(color.HEADER + color.BOLD + "Welcome to Your To-Do List Application!" + color.END)
    print(color.UNDERLINE + "Made by ShadowDev" + color.END)
    print("Hello! This simple tool helps you manage your tasks.")
    print("Let's get started!")
    
    tasks = load_tasks()
    while True:
        print("\n" + color.BOLD + "Menu:" + color.END)
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Mark a task as complete")
        print("5. Exit")
        choice = input(color.GREEN + "Enter your choice: " + color.END)

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_task_complete(tasks)
        elif choice == '5':
            print(color.BOLD + "Thank you for using the To-Do List Application!" + color.END)
            break
        else:
            print(color.RED + "Invalid choice. Please try again." + color.END)

if __name__ == "__main__":
    main()