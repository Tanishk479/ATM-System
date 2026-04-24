
from DEPOSIT_MONEY import deposit_money
from DISPLAY_BALANCE import display_balance
from WITHDRAW_MONEY import withdraw_money
from utils import balance
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