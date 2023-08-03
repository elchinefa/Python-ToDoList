# Function to add a new task to the list
def add_task(task_list):
    task = input("Enter the task: ")
    task_list.append({"task": task, "completed": False})
    print("Task added!")

# Function to view all tasks
def view_tasks(task_list):
    if not task_list:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(task_list, start=1):
            status = "✓" if task["completed"] else "○"
            print(f"{index}. [{status}] {task['task']}")

# Function to mark a task as completed
def mark_completed(task_list):
    view_tasks(task_list)
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(task_list):
            task_list[task_index]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Save tasks to a text file
def save_tasks_to_file(task_list, filename):
    with open(filename, "w") as file:
        for task in task_list:
            file.write(f"{task['task']},{task['completed']}\n")

# Load tasks from a text file
def load_tasks_from_file(filename):
    task_list = []
    try:
        with open(filename, "r") as file:
            for line in file:
                task_info = line.strip().split(",")
                if len(task_info) == 2:
                    task = {"task": task_info[0], "completed": task_info[1] == "True"}
                    task_list.append(task)
    except FileNotFoundError:
        pass
    return task_list

if __name__ == "__main__":
    tasks_file = "tasks.txt"
    tasks = load_tasks_from_file(tasks_file)

    while True:
        print("\n==== To-Do List Manager ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            save_tasks_to_file(tasks, tasks_file)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
