#1) შექმენით ბანკის სისტემა სადაც იქნება ძალიან ბევრი პირობები და გამოიყენებთ if, elif და else -ს, გამოიყენებთ ასევე განვლილ მასალასაც

balance=0

while True:
    operation = input("Please enter your operation: 1.Deposit 2.Withdraw 3.Balance :")
    if operation == "1":
        deposit_amount= input("please enter your deposit: ")
        if deposit_amount.isdigit():
            balance += int(deposit_amount)
        else:
            print("invalid amount,please enter valid amount next time")
    elif operation =="2":
        withdraw_amount = input("Please enter your withdrawl amount: ")
        if withdraw_amount.isdigit():
            if int(withdraw_amount) <= balance:
                balance -= int(withdraw_amount)
            else:
                print("Invalid amount, not enough balance")
        else:
            print("Invalid amount, please enter valid amount next time")
    elif operation == "3":
        print("Your current balance is $" + str(balance))
    else:
        print("Invalid operation, please try again")