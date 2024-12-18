# data_analytics.py

import matplotlib.pyplot as plt
from income_expense import income_expense_data

def generate_report():
    total_income = sum(entry['amount'] for entry in income_expense_data if entry['type'] == 'income')
    total_expense = sum(entry['amount'] for entry in income_expense_data if entry['type'] == 'expense')
    print(f"Total Income : {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Net Savings: {total_income - total_expense}")

def visualize_data():
    categories = [entry['category'] for entry in income_expense_data]
    amounts = [entry['amount'] for entry in income_expense_data]
    plt.bar(categories,amounts)
    plt.xlabel('Category')
    plt.ylabel("Amount")
    plt.title("Income and Expenses")
    plt.show()