# Income and Expense Tracking.py

income_expense_data = []

def add_entry(entry_type, category, amount):
    entry = {
        "type": entry_type,
        "category": category,
        "amount": amount
    }
    income_expense_data.append(entry)

def display_entries():
    for entry in income_expense_data:
        print(f"{entry['type']} - {entry['category']}: {entry['amount']}")

def edit_entry(index, entry_type, category, amount):
    if 0 <= index < len(income_expense_data):
        income_expense_data[index] = {'type': entry_type, 'category': category, 'amount': amount}
        print("Entry updated successfully.")
    else:
        print("Invalid index.")

def delete_entry(index):
    if 0 <= index < len(income_expense_data):
        del income_expense_data[index]
        print("Entry deleted successfully.")
    else:
        print("Invalid index.")