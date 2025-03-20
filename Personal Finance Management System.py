!pip install bcrypt
import sqlite3
import bcrypt
import matplotlib.pyplot as plt

def connect_db():
    return sqlite3.connect("finance.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        username TEXT UNIQUE, 
        password TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY, 
        user_id INTEGER, 
        type TEXT, 
        category TEXT, 
        amount REAL, 
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY, 
        user_id INTEGER, 
        category TEXT, 
        amount REAL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)
    conn.commit()
    conn.close()

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_password.encode())

def sign_up(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    finally:
        conn.close()

def log_in(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password(user[1], password):
        print("Login successful!")
        return user[0]
    print("Invalid username or password!")
    return None

def add_entry(user_id, entry_type, category, amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (user_id, type, category, amount) VALUES (?, ?, ?, ?)", (user_id, entry_type, category, amount))
    conn.commit()
    conn.close()
    print("Entry added successfully!")

def display_entries(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT type, category, amount FROM transactions WHERE user_id = ?", (user_id,))
    entries = cursor.fetchall()
    conn.close()
    for entry in entries:
        print(entry)

def visualize_data(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE user_id = ? GROUP BY category", (user_id,))
    data = cursor.fetchall()
    conn.close()
    if data:
        categories, amounts = zip(*data)
        plt.bar(categories, amounts)
        plt.xlabel("Category")
        plt.ylabel("Amount Spent")
        plt.title("Spending Breakdown")
        plt.show()
    else:
        print("No data to display!")

def main():
    create_tables()
    while True:
        print("\n1. Sign Up\n2. Log In\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            sign_up(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = log_in(username, password)
            if user_id:
                while True:
                    print("\n1. Add Entry\n2. Display Entries\n3. Visualize Data\n4. Log Out")
                    inner_choice = input("Enter your choice: ")
                    if inner_choice == "1":
                        entry_type = input("Enter entry type (income/expense): ")
                        category = input("Enter category: ")
                        amount = float(input("Enter amount: "))
                        add_entry(user_id, entry_type, category, amount)
                    elif inner_choice == "2":
                        display_entries(user_id)
                    elif inner_choice == "3":
                        visualize_data(user_id)
                    elif inner_choice == "4":
                        break
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
