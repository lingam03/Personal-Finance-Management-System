# main.py
from user_authentication import sign_up, log_in
from income_expense import add_entry, display_entries, edit_entry, delete_entry
from budget import set_budget, display_budgets, check_budget
from data_analytics import generate_report, visualize_data

def process_user_actions():
    """This function handles the main functionality after login."""
    while True:
        print("\n1. Add Entry\n2. Display Entries\n3. Edit Entry\n4. Delete Entry\n5. Set Budget")
        print("6. Display Budgets\n7. Generate Report\n8. Visualize Data\n9. Log Out")
        inner_choice = int(input("Enter your choice: "))

        if inner_choice == 1:
            while True:
                entry_type = input("Enter entry type (income/expense): ")
                category = input("Enter category: ")
                amount = float(input("Enter amount: "))
                add_entry(entry_type, category, amount)
                next_step = input("Do you want to add more entries? (yes/no): ").strip().lower()
                if next_step != "yes":
                    break
        elif inner_choice == 2:
            display_entries()
        elif inner_choice == 3:
            index = int(input("Enter entry index to edit: "))
            entry_type = input("Enter entry type (income/expense): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            edit_entry(index, entry_type, category, amount)
        elif inner_choice == 4:
            index = int(input("Enter entry index to delete: "))
            delete_entry(index)
        elif inner_choice == 5:
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            set_budget(category, amount)
        elif inner_choice == 6:
            display_budgets()
        elif inner_choice == 7:
            generate_report()
        elif inner_choice == 8:
            visualize_data()
        elif inner_choice == 9:
            print("Logging out and returning to the main menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\n1. Sign Up\n2. Log In\n3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            sign_up(username, password)
            print("User signed up successfully. Proceeding to main functionality.")
            process_user_actions()  # Automatically proceed after sign-up
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            logged_in = log_in(username, password)
            if logged_in:
                process_user_actions()  # Proceed to main functionality after login
            else:
                print("Invalid credentials. Please try again.")
        elif choice == 3:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
