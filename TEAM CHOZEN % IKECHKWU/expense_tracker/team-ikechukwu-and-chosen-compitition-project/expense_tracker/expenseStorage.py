import csv
import os
from datetime import datetime


FILE_name = "expenses.csv"
HEADS = ["Date", "Category", "Description", "amount"]


def create_csv():
    if not os.path.exists(FILE_name):
        with open(FILE_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(HEADS)
    print(f"'{FILE_name}' created with headers: {', '.join(HEADS)}")

