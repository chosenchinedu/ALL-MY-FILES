from expenseStorage import create_csv
from addExpences import add_expense
from viewExpenses import view_expenses
from deleteExpense import delete_expense


def main():
    create_csv()
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4. Exist")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
