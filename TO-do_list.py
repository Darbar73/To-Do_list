# Constants
FILE_NAME = "todo_list.txt"

# 1. Core Functions for File Handling

def load_tasks():
    """Loads tasks from the text file into a list."""
    try:
        with open(FILE_NAME, 'r') as file:
            # Use .strip() to remove the newline character from each line
            tasks = [line.strip() for line in file if line.strip()]
        return tasks
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []

def save_tasks(tasks):
    """Writes the current list of tasks back to the text file."""
    # 'w' mode overwrites the entire file with the current list
    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# 2. Core Functionality (Add/Remove/View)

def add_task(tasks):
    """Prompts user for a task and adds it to the list."""
    task_description = input("Enter the new task: ").strip()
    if task_description:
        tasks.append(task_description)
        print(f"Task added: '{task_description}'")
        save_tasks(tasks)
    else:
        print("Task cannot be empty.")

def view_tasks(tasks):
    """Prints all tasks in the list with their index."""
    if not tasks:
        print("\n--- Your To-Do List is Empty! ---")
    else:
        print("\n--- TO-DO LIST ---")
        for index, task in enumerate(tasks):
            # Displaying index starting from 1 for user convenience
            print(f"{index + 1}. {task}")
        print("--------------------")

def remove_task(tasks):
    """Prompts user for a task number and removes it."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num_input = input("Enter the number of the task to remove: ")
        task_index = int(task_num_input) - 1 # Convert 1-based index to 0-based

        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task removed: '{removed_task}'")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# 3. Main CLI Loop

def display_menu():
    """Shows the user menu options."""
    print("\n--- Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("------------")

def todo_app():
    """Main application loop."""
    tasks = load_tasks()
    print("Welcome to the Console To-Do List Application!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    todo_app()