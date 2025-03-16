#Author: Thisanga
#Course work - stage 1

# List to store tasks
tasks = []


# Functions for CRUD operations
def add_task():
    name = str(input("\nEnter the task name:"))
    description = str(input("Enter the task description:"))
    priority = str(input("Enter the task priority level(High/Medium/Low):"))
    due_date = str(input("Enter the Due date for the task(dd/mm/yyyy):"))

    task = {"name": name, "description": description, "priority": priority, "due_date": due_date}
    tasks.append(task)
    print(f"task: {name} added successully")


def view_tasks():
    if len(tasks) == 0:
        print("\nThere is no task to be done!")
        return
    else:
        print("_____________________________Task List_______________________________")
        count = 1
        for task in tasks:
            print(f"{count}. {task['name']} | {task['priority']} | Due: {task['due_date']} | Description: {task['description']} ")
            count += 1 
    

def update_task():
    if len(tasks) == 0:
        print("\nNo tasks available to update!")
        return 
    #Display the task list
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number you want to update: "))
        
        # Check the task number is valid or not
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number!")
            return
        
        # Get the correct task from the task list 
        task = tasks[task_num - 1]

        # Ask for confirmation before updating
        confirm = input(f"Do you want to update task '{task['name']}'? (yes/no): ").lower()
        if confirm != 'yes':
            print("Task update cancelled successfully!")
            return
        
        # get the new data to be update
        task['name'] = input("Enter new name: ")
        task['description'] = input("Enter new description: ")
        task['priority'] = input("Enter new priority (High/Medium/Low): ")
        task['due_date'] = input("Enter new due date (dd/mm/yyyy): ")
        
        print("Task updated successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    


def delete_task():
    if len(tasks) == 0:
        print("\nNo tasks available to Delete!")
        return 
    #Display the task list
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number you want to delete: "))
        
        # Check the task number is valid or not
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number!")
            return
        
        # Get the correct task from the task list
        task = tasks[task_num - 1]

        # Ask for confirmation before deleting
        confirm = input(f"Do you want to delete task '{task['name']}'? (yes/no): ").lower()
        if confirm != 'yes':
            print("Task deletion cancelled successfully!")
            return
        
        # Delete the task
        tasks.remove(task)
        print("Task deleted successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    


if __name__ == "__main__":
    while True:
        print("\nTask Manager")
        print("1. Show the tasks")
        print("2. Update a task")
        print("3. Delete a task")
        print("4. Add a task")
        print("5. Exit")
        choice = input("Select the number to do:")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            update_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            add_task()
        elif choice == "5":
            print("Exiting Task Manager. Thanks for using.Goodbye!")
            break
        else:
            print("Invalid input! Please select a valid number.")


