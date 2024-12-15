

expenses = []

def add_exp():
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    if amount.replace('.', '', 1).isdigit():
        amount = float(amount)
        expenses.append({"date": date, "description": description, "amount": amount})
        print("Expense added successfully!\n")
    else:
        print("Invalid amount. Please enter a numeric value.\n")

def view_exp():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    total = 0
    print("Date        | Description         | Amount")
    print("------------------------------------------")
    for expense in expenses:
        print(f"{expense['date']} | {expense['description']:<20} | ${expense['amount']:.2f}")
        total += expense['amount']
    print("------------------------------------------")
    print(f"Total: ${total:.2f}\n")

def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_exp()
        elif choice == "2":
            view_exp()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
