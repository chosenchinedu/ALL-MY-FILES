import csv
from expenseStorage import FILE_name


def summerize_expense():
    total_spent = 0
    category_total = {}
    transaction_total = 0

    with open(FILE_name, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                amount = float(row[3])
                category = row[2]

                total_spent += amount
                transaction_total += 1

                if category in category_total:
                    category_total[category] += amount
                else:
                    category_total[category] = amount

    print("\n---Summary Expense---")
    for category, total in category_total.items():
        print(f"  {category}: {total}")
    print(f"Total spent: {total_spent}")
    print(f"Total transaction: {transaction_total}")


    



