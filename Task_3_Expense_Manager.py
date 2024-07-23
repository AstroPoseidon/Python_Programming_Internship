from datetime import datetime
import csv
from collections import defaultdict

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
                    date_str, amount, description, category = row
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date() 
                    amount = float(amount) 
                except (ValueError, IndexError):
                    date_obj = None
                    amount = 0.0  
                expenses.append(Expense(amount, description, category, date_obj))
    except FileNotFoundError:
        pass 
    return expenses

# Save expenses to a CSV file
def save_expenses(expenses):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Description", "Category"])
        for expense in expenses:
            if expense.date_time:
                date_str = expense.date_time.strftime('%Y-%m-%d')
            else:
                date_str = ""  
            writer.writerow([date_str, expense.amount, expense.description, expense.category])

# Add a new expense
def add_expense():
    amount = float(input("\nEnter amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter expense category (e.g., food, transportation): ")
    current_datetime = datetime.now()
    expenses.append(Expense(amount, description, category, current_datetime))
    save_expenses(expenses)
    print("\nExpense added successfully!")

# View monthly expense summary
def view_monthly_summary():
    monthly_expenses = defaultdict(float)
    for expense in expenses:
        if expense.date_time:
            month_year = expense.date_time.strftime('%Y-%m')
            monthly_expenses[month_year] += expense.amount
    
    print("\nMonthly expense summary:")
    for month_year, total_expense in sorted(monthly_expenses.items()):
        print(f"{month_year}: {total_expense:.2f}")

# View category-wise expenditure
def view_category_wise():
    categories = {}
    for expense in expenses:
        category = expense.category
        if category in categories:
            categories[category] += expense.amount
        else:
            categories[category] = expense.amount
    print("\nCategory-wise expenditure:\n")
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
