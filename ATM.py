#ATM MACHINE

balance = 0
#DISPLAY BALANCE

def display_balance():
    if balance==0:
        print("YOUR CURRENT BALANCE IS : 0")
    else:
        print("YOUR CURRENT BALANCE IS : ", balance)


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


#DEPOSIT MONEY

def deposit_money():
    amt = int(input("enter the amount to deposit : "))
    global balance
    if amt>0:
        balance += amt
        print(f'{amt} DEPOSITED SUCCESSFULLY ✅')
    else:
        print("ERROR,ENTER VALID AMOUNT ⚠️")


#menu
def atm():
    print("\n====== WELCOME TO THE ATM MACHINE ======")
    while True:
        print("\n👉 1. DISPLAY BALANCE ")
        print("👉 2. WITHDRAW MONEY ")
        print("👉 3. DEPOSIT MONEY ")
        print("👉 4. EXIT")
        choice = int(input("ENTER YOUR CHOICE : "))
        if choice==1:
            display_balance()
        elif choice==2:
            withdraw_money()
        elif choice==3:
            deposit_money()
        elif choice==4:
            print("THANK YOU FOR USING OUR ATM MACHINE 👋 ")
            break
        else:
            print("INVALID CHOICE 🚫. PLEASE TRY AGAIN.")
#run the atm machine
atm()