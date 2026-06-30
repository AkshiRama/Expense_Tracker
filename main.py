# Expense Tracker

FILE_NAME = "expenses.txt"


# Function to add an expense
def add_expense():
    item = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{item},{amount}\n")

    print("Expense added successfully!\n")


# Function to view all expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

            if len(expenses) == 0:
                print("No expenses found.\n")
                return

            total = 0

            print("\n------ Expenses ------")

            for expense in expenses:
                item, amount = expense.strip().split(",")
                print(f"{item} - ₹{amount}")
                total += float(amount)

            print("----------------------")
            print(f"Total Expense = ₹{total}\n")

    except FileNotFoundError:
        print("No expense file found.\n")


# Function to search expenses
def search_expense():
    search = input("Enter expense name to search: ").lower()

    found = False

    with open(FILE_NAME, "r") as file:
        for expense in file:
            item, amount = expense.strip().split(",")

            if search == item.lower():
                print(f"Found: {item} - ₹{amount}")
                found = True

    if not found:
        print("Expense not found.\n")


# Main Menu
while True:

    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_expense()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice.\n")
