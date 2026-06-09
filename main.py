from storage import load_tasks
import task_service as ts


def main():
    tasks = load_tasks()
    ts.set_tasks(tasks)

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        try:
            ch = int(input("Enter choice: "))
        except ValueError:
            print("Only numbers allowed")
            continue

        if ch == 1:
            task = input("Enter task name: ")
            ts.add_task(task)
        elif ch == 2:
            ts.view_tasks()
        elif ch == 3:
            index = int(input("Enter task number: "))
            ts.complete_task(index)
        elif ch == 4:
            index = int(input("Enter task number: "))
            ts.delete_task(index)
        elif ch == 5:
            break
        else:
            print("Invalid choice")

    print("Exiting CLI")


if __name__ == "__main__":
    main()