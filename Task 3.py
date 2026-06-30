# Smart ATM Simulator
print("Welcome to Smart ATM")
real_pin = 2006
balance = 3000
user_pin = int(input("Enter your PIN: "))
if user_pin == real_pin:
    print("1. Withdraw")
    print("2. Check Balance")
    choice = int(input("Choose an option: "))
    if choice == 1:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Sorry, insufficient balance.")
        else:
            balance -= amount
            print(f"Transaction successful. Remaining balance: {balance}")
    elif choice == 2:
        print(f"Your balance is: {balance}")
    else:
        print("Invalid choice.")
else:
    print("Incorrect PIN. Access denied.")