from random import randint
Accounts = []

def createuser():
    user_id = ''.join(str(randint(0, 9)) for i in range(5))
    balance = 100
    new_account = {
        "Account_id": user_id,
        "Account_balance": balance
    }
    Accounts.append(new_account)
    print(f"User '{user_id}' created successfully!")

def login():
    user_id_login = input("Enter Account ID: ")
    for accounts in Accounts:
        if accounts["Account_id"] == user_id_login:
            return accounts

def withraw(accounts):
    amountwithraw = int(input("Enter Amount :"))
    if amountwithraw > accounts["Account_balance"]:
        print("balance is not enough")
    else:
        accounts["Account_balance"] -= amountwithraw
    
def deposit(accounts):
    depositAmount = int(input("Entert value deposit :"))
    if depositAmount > 0:
        print("Invalid value")
    else:
        accounts["Account_balance"] += depositAmount
        print("deposit has been successful ")
   
    
def checkbalance(accounts):
    return accounts["Account_balance"]

def main():
    while True:
        print("\n1. Create User\n2. Login\n3. Check Balance\n4. Deposit\n5. Withdraw\n6. Exit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            createuser()
        elif choice == '2':
            logged_in_account = login()
            if logged_in_account:
                print(f"Logged in as '{logged_in_account['Account_id']}'")
            else:
                print("Account not found.")
        elif choice == '3':
            logged_in_account = login()
            if logged_in_account:
                balance = (logged_in_account)
                print(f"Current balance: {balance}")
            else:
                print("Please log in first.")
        elif choice == '4':
            logged_in_account = login()
            if logged_in_account:
                deposit(logged_in_account)
            else:
                print("Please log in first.")
        elif choice == '5':
            logged_in_account = login()
            if logged_in_account:
                withraw(logged_in_account)
            else:
                print("Please log in first.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

main()




