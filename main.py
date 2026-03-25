from services.task_service import add_task, list_tasks, complete_task

def menu():
    while True:
        print("\n==== TO-DO MENU ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Task title: ")
            priority = input("Priority (Low/Medium/High): ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            add_task(title, priority, deadline)

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            index = int(input("Task number: ")) - 1
            complete_task(index)

        elif choice == "4":
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()