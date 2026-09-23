balance = 10000

while balance > 0:
    amount = int(input("How much do you want to withdraw? "))
    
    if amount > balance:
        print("Insufficient funds")
    else:
        balance = balance - amount
        print("Remaining balance: ₦", balance)
        
        if balance == 0:
            print("Account empty")