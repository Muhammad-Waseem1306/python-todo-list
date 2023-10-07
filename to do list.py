import os
# Function to display the to-do list
def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Added: {task}")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_number):
    if 1 <= task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Removed: {removed_task}")
    else:
        print("Invalid task number.")

# Function to save the to-do list to a file
def save_to_file(todo_list, filename):
    with open(filename, "w") as file:
        for task in todo_list:
            file.write(f"{task}\n")

# Function to load the to-do list from a file
def load_from_file(filename):
    todo_list = []
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            todo_list = [line.strip() for line in file]
    return todo_list

def main():
    filename = "todo.txt"
    todo_list = load_from_file(filename)

    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == "3":
            display_todo_list(todo_list)
            task_number = int(input("Enter the task number to remove: "))
            remove_task(todo_list, task_number)
        elif choice == "4":
            save_to_file(todo_list, filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
