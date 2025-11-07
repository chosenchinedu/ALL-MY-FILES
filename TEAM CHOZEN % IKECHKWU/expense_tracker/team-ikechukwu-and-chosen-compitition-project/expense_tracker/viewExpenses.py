import os
import csv
from expenseStorage import FILE_name
from expenseStorage import HEADS
from expenseSummary import summerize_expense


def view_expenses():

    if not os.path.exists(FILE_name):
        print("No entry recorded. Add first!")
        return

    with open(FILE_name, 'r', newline='') as file:
        reader = csv.reader(file)
        header = HEADS
        expenses = list(reader)
        

    if not expenses:
        print("No expenses to be added")
        return

    print("\n--- Your Expenses ---")
    print(f"{header[0]:<12} {header[1]:<15} {header[2]:<30} {header[3]:<10}")
    print("_" * 70)

    for expense in expenses:
        print(
            f"{expense[0]:<12} {expense[1]:<15} {expense[2]:<30} {expense[3]:<10}")
       
    print("_" * 70)
    summerize_expense()


