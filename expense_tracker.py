import csv

def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, description])
    print("Expense added successfully!\n")

def view_summary():
    expenses = {}
    total = 0
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                category, amount = row[0], float(row[1])
                expenses[category] = expenses.get(category, 0) + amount
                total += amount
        print("\nExpense Summary:")
        for category, amount in expenses.items():
            print(f"{category}: R{amount:.2f}")
        print(f"Total: R{total:.2f}\n")
    except FileNotFoundError:
        print("No expenses recorded yet!\n")

while True:
    print("1. Add Expense\n2. View Summary\n3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_summary()
    elif choice == '3':
        break
    else:
        print("Invalid choice!\n")
