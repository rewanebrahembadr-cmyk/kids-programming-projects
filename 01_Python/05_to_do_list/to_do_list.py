# To-Do List Project
# This project helps beginners practice lists, functions, loops, and menu systems.

tasks = []


def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(index, "-", task)


def delete_task():
    view_tasks()

    if len(tasks) > 0:
        task_number = int(input("Enter the task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print("Deleted task:", removed_task)
        else:
            print("Invalid task number.")


while True:
    show_menu()
    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
