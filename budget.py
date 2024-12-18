# budget.py

budgets = {}

def set_budget(category, amount):
    budgets[category] = amount
    print(f"Budget set for {category}: {amount}")

def display_budgets():
    for category, amount in budgets.items():
        print(f"{category}: {amount}")

def check_budget(category, spending):
    if category in budgets:
        if spending>budgets[category]:
            print(f"Over budget in {category}: spend: {spending}, Budget: {budgets[category]}")
        else:
            print(f"Under budget in {category}. Spend:{spending}, Budget: {budgets[category]}")
    else:
        print(f"No budget set for {category}.")