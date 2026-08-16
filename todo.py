
# To-Do List Application

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    if tasks:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index] = input("Enter new task: ")
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

def delete_task():
    view_tasks()
    if tasks:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

def menu():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

# Main Program
menu()