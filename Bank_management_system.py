account = input("Enter Holder name ")   #Take name form user
print("Name :",account)

pin = int(input("Create Pin :"))        #Take pin from user to set the password for account
print("Pin :",pin)

date_of_birth = input("DD/MM/YYYY ")    #Take the date of birth from user in this format
print("D.O.B :",date_of_birth)

address = input("Enter your address :") #Take the address from user
print("Address :",address)

father_name = input("Enter your father name :")  #Take the father's name from user
print("Father's name :",father_name)
print("Account is Created :")

deposit = int(input("Enter Your amount"))  #Take amount from user to deposit in account
print("Deposited amount :",deposit)

balance = deposit                        #Show balance of user which are deposited by user
print("Your balance :",balance)

entered_pin = int(input("\nEnter your pin to access amount :")) #Enter your created pin for login
if entered_pin == pin:               #Agar pin correct ha to account login hoga warna nhi hoga
    print("Login successful!")       #Login hote hi ye output dega
    while True:                      #Yaha chaar option ha user jo number chunega vo run hoga
        print("\n1. Check Balance")  #Number 1 for balance check
        print("2. Deposit")          #Number 2 for new deposit
        print("3. Withdraw")         #Number 3 for amount withdraw
        print("4. Account Details")  #Number 4 for Check the account details
        print("5. Exit")             #And last Number 5 for exit the program

        choice = int(input("Enter your choice :")) #User apna choice dega jo usse chaiye

        if choice == 1:              #Agar user 1 chunta ha to uska balance show hoga
            print("Your balance :",balance)
        elif choice == 2:            #Warna agar user 2 chunta ha to vo apne account me new deposit kar sakta ha
            deposit = int(input("Enter amount to details :"))  #Yaha user ko amount likhna hoga for deposit
            balance += deposit 

            print("Amount deposited successfully :")
            print("Your balance :",balance)  #Yaha par user ko uska new balance show hoga
        elif choice == 3:            #Warna agar user 3 chunta ha to vo apne paise withdraw kar sakta ha
            withdraw = int(input("Enter amount to withdraw :"))  #Yaha user ko amount likhna hoga for withdraw
            if withdraw<=balance:
                balance -= withdraw
                print("Withdraw successful")
                print("Your balance :",balance)  #Abb user ka left balance show hoga after withdraw

            else:        #Agar user uske balance amount se jayda dalta ha to 
                print("Insufficient balance") #To fir yeah output dega
        elif choice == 4:           #Warna agar user 4 chunta ha to uske account ke detail show honge

            print("\nAccount Details")    
            print("Name :", account)               #Yaha par naam user
            print("D.O.B :", date_of_birth)        #Yaha par date of birth user
            print("Address :", address)            #Yaha par address of user
            print("Father's name :", father_name)  #Yaha par father's name of user
            print("Balance :", balance)            #Yaha par Balance of user account
        elif choice == 5:            #Warna agar user 5 chunta ha to uska program exit ho jayega
            print("Thank you for using our bank!")
            break
        else:                       #Or agar user diye hue number ke alava kuch or number chunta ha to
            print("Invalid choice!")    #To fir ye output show hoga
else:                               #Agar user pin hi galat dalta ha to account login hi nhi hoga
    print("Wrong PIN!")