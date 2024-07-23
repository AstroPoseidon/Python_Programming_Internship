from datetime import datetime
import csv

# Defining an Expense class for storage of data
class Expense:
    def __init__(self, amount, description, category, date_time=None):
        self.amount = amount
        self.description = description
        self.category = category
        self.date_time = date_time 

# Load expenses from a CSV file
def load_expenses():
    expenses = []
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                try:
                    # Assuming date format in CSV is YYYY-MM-DD
                    date_str, amount, description, category = row
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()  # Convert to date object
                    amount = float(amount)  # Assuming amount is in the second element
                except (ValueError, IndexError):  # Handle conversion and potential missing data
                    date_obj = None
                    amount = 0.0  # Or handle differently based on your needs
                expenses.append(Expense(amount, description, category, date_obj))
    except FileNotFoundError:
        pass  # Ignore if file doesn't exist
    return expenses

# Save expenses to a CSV file
def save_expenses(expenses):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Description", "Category"])
        for expense in expenses:
            # Include date if available during saving
            if expense.date_time:
                date_str = expense.date_time.strftime('%Y-%m-%d')
            else:
                date_str = ""  # Or handle differently (e.g., placeholder)
            writer.writerow([date_str, expense.amount, expense.description, expense.category])

# Add a new expense
def add_expense():
    amount = float(input("\nEnter amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter expense category (e.g., food, transportation): ")
    # Capture current date and time
    current_datetime = datetime.now()
    expenses.append(Expense(amount, description, category, current_datetime))
    save_expenses(expenses)
    print("\nExpense added successfully!")

# View monthly expense summary
def view_monthly_summary():
    current_month = datetime.today().strftime('%Y-%m')
    total_expense = 0
    for expense in expenses:
        # Check if expense has a date and if it falls within the current month
        if expense.date_time and expense.date_time.strftime('%Y-%m') == current_month:
            total_expense += expense.amount
    print(f"\nTotal expense for {current_month}: {total_expense:.2f}")

# View category-wise expenditure
def view_category_wise():
    categories = {}
    for expense in expenses:
        category = expense.category
        if category in categories:
            categories[category] += expense.amount
        else:
            categories[category] = expense.amount
    print("\nCategory-wise expenditure:")
    for category, amount in categories.items():
        print(f"{category}: {amount:.2f}")

# Main Program for expense tracker
if __name__ == "__main__":
    expenses = load_expenses()
    while True:
        print("\n\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenditure")
        print("4. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_monthly_summary()
        elif choice == "3":
            view_category_wise()
        elif choice == "4":
            save_expenses(expenses)
            print("\nThank You!!")
            break
        else:
            print("Invalid choice. Please try again.")
