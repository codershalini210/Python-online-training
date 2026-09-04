
# username = input("Enter username   ")
# password = input("Enter password   ")
# if(username =="Admin" and password=="123456"):
#     print("Welcome")
# elif(username !="Admin" and password !="123456"):
#     print("invalid username and password")
# elif(username!="Admin"):
#     print("username is not correct")
# else:
#     print("Password is not correct")

# ATM
# enter pin if pin is 1234 then its correct and go ahead
#  otherwise invalid pin
#a dummy balance 50000
# now ask user to enter withdrawal amt
# if WA< balance msg => withdrawal successfully
# else insufficent balance 
balance = 50000
pin = input("Enter your pin ")
if(pin !="1234"):
    print("Invalid pin")
else:
    amt = int(input("Enter amount to withdraw"))
    if(amt<balance):
        print("Withdrawal successfully")
    else:
        print("Insufficient balance")
