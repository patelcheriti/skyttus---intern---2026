# to do list
tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            print(i, task)

    elif choice == "3":
        num = int(input("Enter task number: "))
        tasks.pop(num - 1)
        print("Task removed")

    elif choice == "4":
        break

    else:
        print("Invalid choice")

# Bank Management System
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw:" , amount)
        else:
            print("Insufficient Balance")
    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount("User")

acc.deposit(1000)
acc.withdraw(300)
acc.show_balance()