# Simple Python program using if-else (no user input)

balance = 3000
withdraw_amount = 2500

print("==== ATM Transaction ====")

if withdraw_amount <= balance:
    balance -= withdraw_amount
    print(f"Transaction successful! Remaining balance: ₹{balance}")
else:
    print("Transaction failed! Insufficient balance.")

