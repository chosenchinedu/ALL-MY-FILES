from datetime import datetime
import csv

from expenseStorage import FILE_name

# function to add your expense


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input(
        "Enter category(e.g food, transport, bills, education.): ")
    description = input("Enter description: ")

    while True:
        try:
            Amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("invalid. Enter a valid number")
    with open(FILE_name, 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, Amount])
    print("Expense added successfully.")
