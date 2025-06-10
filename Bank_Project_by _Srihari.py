bank = {}

def transfer():
    sender = int(input("Enter the sender Account Number :- "))
    recever = int(input("Enter the recever Account Number :- "))
    Amount = float(input("Enter the balance to transfer :- "))
    if sender not in bank:
        print("Sender Account not found \n")
        return
    if recever not in bank:
        print("Recever Account not found \n")
        return

    sender_accno , sender_balance = bank[sender]
    recever_accno , recever_balance = bank[recever]
    if Amount <= 0:
        print("Invalid balance !!! \n")
        return
    if sender_balance < Amount:
        print("Insufficient balance in senders account !! \n")
        return
    sender_balance = sender_balance - Amount
    recever_balance = recever_balance + Amount
    bank[sender] = (sender_accno , sender_balance)
    bank[recever] = (recever_accno , recever_balance)
    print(f"Successfully transfered amount from {sender_accno} to {recever_accno} \n")
    
def check_Account():
    acc_no = int(input("enter your account number :- "))
    if acc_no in bank:
        print("Account already Exist !! \n")
    else:
        name = input("Enter Your name : ")
        balnce = float(input("Enter your balance:- "))
        if balnce <= 0:
            print("invalid balance!! \n")
            return
        bank[acc_no] = (name,balnce)
        print("Account SuccessFully Created!! \n")
        
def deposit():
    acc_no = int(input("enter your account number :- "))
    if acc_no not in bank:
        print("Account Not found !! \n")
    else:
        balnce = float(input("Enter your balance:- "))
        if balnce <= 0:
            print("invalid balance!! \n")
            return
        amount = (bank[acc_no][1])+balnce
        name=(bank[acc_no][0])
        bank[acc_no] = (name,amount)
        print(f"You Have deposited {balnce} successfully. \n{name} Your balance is  {amount} rupees \n")

        

def withdraw():
    acc_no = int(input("enter your account number :- "))
    if acc_no not in bank:
        print("Account Not found !! \n")
    else:
        balnce = float(input("Enter your balance:- "))
        if balnce <= 0:
            print("invalid balance!! \n")
            return
        amount = (bank[acc_no][1])-balnce
        name=(bank[acc_no][0])
        bank[acc_no] = (name,amount)
        print("Withdrawal Successfull!! \n")
        
def check_balance():
    acc_no = int(input("enter your account number :- "))
    if acc_no not in bank:
        print("Account Not found !! \n")
    else:
        print("Your balance is : " , bank[acc_no][0],"=>",  bank[acc_no][1])
    
       
while (True):
    print("-------------Welcome To CLI Bank---------------")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check balance ")
    print("6. Exit")
    select = int(input("Select the number between 1 to 6  :- "))
    if select == 1:
        check_Account() 
    elif select == 2:
        deposit()
    elif select == 3:
        withdraw()
    elif select == 4:
        transfer()
    elif select == 5:
        check_balance()
    elif select == 6:
        break
    else:
        print("You have entered inavlid number!!")
print(bank)




