pin = 1306                                     #User apna personal pin banyega
pin = int(input("Enter your Pin:"))            #Yaha program user se uska banya hua pin mangega

if pin != 1306:                                 #Yaha user ka dala pin check hoga agar pin galat dala to
    print("Wrong Pin:")                         #To fir ye output dega or program exit ho jayega
    exit()
else:                                            #Warna agar pin sahi ha to account login ho jayega
    print("Correct Pin:")
balance = 10000                                  #Then sabse phele balance show hoga
print("Balance:",balance)              

while True:
    print("\n1. Deposit")
    print("2.   Withdraw")

    choice = int(input("Enter your choice :"))    #Yaha user se uska choice pucha jayega

    if choice == 1:                               #Agar user choice 1 ha to amount deposit hoga
        deposit = int(input("Enter amount to deposit :"))
        balance += deposit
        print("Amount deposited successfully")
        print("Your balance",balance)

    elif choice == 2:                              #Agar user choice 2 ha to amount withdraw hoga
        withdraw = int(input("Enter amount to withdraw :"))
        if withdraw <= balance:                    #Agar amount balance se kam ya uske equal hua to withdraw hoga 
            balance -= withdraw
            print("Withdraw Successful")
            print("Your balance :", balance)
        else:                                     #Agar amount balance se jayda hua to ye output dega
            print("Insufficietn balance")
    break