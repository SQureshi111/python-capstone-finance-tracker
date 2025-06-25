# Step 1: Welcome message
print("Welcome to the Personal Finance Tracker!")

# Global dictionary to store expenses
data = {}

# Step 2: Add Expense Function
def add_expense():
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        expense = (description, amount)
        if category in data:
            data[category].append(expense)
        else:
            data[category] = [expense]

        print("Expense added successfully.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Step 3: View All Expenses
def view_expenses(expense_data):
    if not expense_data:
        print("No expenses to display.")
        return
    for category, expenses in expense_data.items():
        print(f"Category: {category}")
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}")

# Step 4: View Summary by Category
def view_summary(expense_data):
    if not expense_data:
        print("No summary to display.")
        return
    print("Summary:")
    for category, expenses in expense_data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

# Step 6 & 7: Menu-driven interface
def menu():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            view_summary(data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

# Start the program
menu() 
