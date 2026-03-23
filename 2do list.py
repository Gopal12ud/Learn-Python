tasks = []

def show_tasks():
    if not tasks:
        print("No Tasks Available")
    else: 
        print("\n Your Tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_tasks():
    task = input("Enter task")
    tasks.append (task)
    print ("task added")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print("Removed:", removed)
        else:
            print("Invalid Index")
    except: 
          print("Enter Valid Number")

def save_task():
 with open("tasks.txt", "w" )as file:
    for task in tasks:
        file.write (task + "\n")

def load_tasks():
    try:
        with open ("tasks.txt", "r")as file:
            for line in file:
                tasks.append (line.stripe())
    except:
        pass

load_tasks()
while True:
    print("\n1.View Tasks")
    print("2.Add Tasks")
    print("3.Delete Tasks")
    print("4.Exit")
    choice = input("Enter Choice: ")
    if choice =="1":
        show_tasks()
    elif choice == "2":
        add_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        save_task()
        print("Tasks saved. Exiting...")
        break
    else:
        print("Invalid choice")