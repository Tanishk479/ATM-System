#WITHDRAW MONEY

def withdraw_money():
    amount  = int(input("ENTER THE AMOUNT TO WITHDRAW : "))
    global balance
    if amount>balance:
        print("INSUFFICIENT BALANCE 🚨")
    elif amount<=0:
        print("ERROR , ENTER VALID AMOUNT⚠️")
    else:
        
        balance -= amount
        print(f'{amount} WITHDRAWN SUCCESSFULLY ✅')