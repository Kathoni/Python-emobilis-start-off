Withdrawal = float(input("Enter Amount You Wish to Withdraw: "))

if Withdrawal >= 10000.0:
    Amount = Withdrawal * 0.01 + Withdrawal
    print(f"Amount to be withdrawn: {Amount}")
elif Withdrawal <= 5000.0:
    Amount = Withdrawal * 0.005 + Withdrawal
    print(f"Amount to be withdrawn: {Amount}")
else:
    print("Error: Withdrawal amount is too low.")