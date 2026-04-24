def deposit_money():
    amt = int(input("enter the amount to deposit : "))
    global balance
    if amt>0:
        balance += amt
        print(f'{amt} DEPOSITED SUCCESSFULLY ✅')
    else:
        print("ERROR,ENTER VALID AMOUNT ⚠️")