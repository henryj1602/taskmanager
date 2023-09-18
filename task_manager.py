


from task import Task, TaskManager

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add a Task")
        print("2. View Your Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Quit Task Manager")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
            print("Task added successfully.")
        
        elif choice == "2":
            task_manager.view_tasks()
        
        elif choice == "3":
            task_manager.view_tasks()
            task_id = int(input("Enter the ID of the task to mark as completed: "))
            task_manager.mark_task_completed(task_id)
            print("Task marked as completed.")
        
        elif choice == "4":
            task_manager.view_tasks()
            task_id = int(input("Enter the ID of the task to remove: "))
            task_manager.remove_task(task_id)
            print("Task removed successfully.")
        
        elif choice == "5":
            break

if __name__ == "__main__":
    main()

   
