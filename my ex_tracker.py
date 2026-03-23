import csv
expenses = []

def add_expenses():
    name = input("Enter Expense Name: ")
    amount = float(input("Enter Amount: "))
    expenses.append({"name": name, "amount":amount})

def show_expenses():
    if not expenses:
        print("No Expenses Found")
    else :
        print("\n Expenses: ")
        for i, exp in enumerate(expenses):
            print (f" {i+1}. {exp['name']} - ₹{exp['amount']}")

def total_expenses():
    total=sum (exp["amount"] for exp in expenses)
    print ("Total Expenses: " ,total)

def save_expenses():
    with open ("expenses.csv", "w" ,newline= "")as file:
     writer = csv.writer(file)
     writer . writerow (["name", "Amount"])
    for exp in expenses:
        writer.writerow ([exp["name"], exp["amount"]])

def load_expenses():
    try:
        with open("expenses.csv" , 'r')as file:
            reader = csv.DictReader (file)
            for row in reader:
                expenses.append ({
                    "name": row["name"],
                    "amount": float(row["amount"])
                })
    except:
        pass
    
load_expenses()

while True:
    print("\n1. Add Expenses")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4.  Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        add_expenses()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_expenses()
    elif choice== "4":
        save_expenses()
        print("Expenses saved. Exiting...")
        break
    print("Invalid Choice")

