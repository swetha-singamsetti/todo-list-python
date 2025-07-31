import json

# Define the Task class
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

# Save tasks to JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Load tasks from JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            data = json.load(f)
            return [Task(**task) for task in data]
    except FileNotFoundError:
        return []

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return
    for idx, task in enumerate(tasks):
        status = "✅ Completed" if task.completed else "❌ Pending"
        print(f"\nTask {idx + 1}:")
        print(f"Title      : {task.title}")
        print(f"Description: {task.description}")
        print(f"Category   : {task.category}")
        print(f"Status     : {status}")

# Main menu loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- PERSONAL TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter category (Work/Personal/Urgent): ")
            task = Task(title, description, category)
            tasks.append(task)
            print("✅ Task added.")

        elif choice == '2':
            view_tasks(tasks)

        elif choice == '3':
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                tasks[index].mark_completed()
                print("✅ Task marked as completed.")
            except (IndexError, ValueError):
                print("❌ Invalid task number.")

        elif choice == '4':
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                removed_task = tasks.pop(index)
                print(f"🗑️ Task '{removed_task.title}' deleted.")
            except (IndexError, ValueError):
                print("❌ Invalid task number.")

        elif choice == '5':
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()