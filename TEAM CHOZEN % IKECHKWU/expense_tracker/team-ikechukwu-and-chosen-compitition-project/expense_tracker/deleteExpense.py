from expenseStorage import FILE_name
import csv

def delete_expense():
    with open(FILE_name, "r") as file:
        reader = csv.reader(file)
        header = next(reader)   
        expenses = list(reader) 


    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expenses List ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense[0]} {expense[1]} {expense[2]} {expense[3]}")


    choice = input("\nEnter the number of the expense to delete: ")

    try:
        number = int(choice) - 1
        if number < 0 or number >= len(expenses):
            print(" Invalid choice. No expense deleted.")
            return
    except ValueError:
        print(" Invalid. Please enter a number.")
        return


    deleted = expenses.pop(number)


    with open(FILE_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)   
        writer.writerows(expenses)


    print(f"Expense deleted: {deleted[0]} {deleted[1]} {deleted[2]} {deleted[3]}")