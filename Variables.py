is_running = True

while is_running:
    print('Welcome to Mwangi Withdraw ATM')
    withdraw_amount = float(input("Enter amount to withdraw (Ksh): "))
    if withdraw_amount >= 10000:
        new_amount = withdraw_amount + withdraw_amount * 0.01
        print(new_amount)
    elif withdraw_amount >= 5000:
        new_amount = withdraw_amount - withdraw_amount * 0.05
        print(new_amount)
    else:
        print("Thank your for using our atm")