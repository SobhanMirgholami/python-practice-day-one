
# Homework 4: ATM Simulator

def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("====================")


def deposit(balance):
    try:
        amount = float(input("Deposit amount: $"))
    except ValueError:
        print("Invalid input! Enter a number.")
        return balance

    if amount <= 0:
        print("Amount must be positive!")
        return balance

    balance += amount

    print(f"Deposited: ${amount:.2f}")
    return balance


def withdraw(balance):
    try:
        amount = float(input("Withdraw amount: $"))
    except ValueError:
        print("Invalid input! Enter a number.")
        return balance

    if amount <= 0:
        print("Amount must be positive!")

    elif amount > balance:
        print("Insufficient balance!")

    else:
        balance -= amount
        print(f"Withdrawn: ${amount:.2f}")

    return balance


def main():
    balance = 1000.0

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your balance: ${balance:.2f}")

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()
