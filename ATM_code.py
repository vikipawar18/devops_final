# Simple ATM Program using while loop

balance = 5000  # initial balance
pin = 1234      # ATM PIN

print("==== Welcome to Simple ATM ====")

# Verify PIN
entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print(f"Your current balance is ₹{balance}")

        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print(f"₹{amount} deposited successfully! New balance: ₹{balance}")

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"₹{amount} withdrawn successfully! Remaining balance: ₹{balance}")
            else:
                print("Insufficient balance!")

        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

else:
    print("Incorrect PIN! Access Denied.")
