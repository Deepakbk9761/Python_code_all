#wap to make the ATM:
title="ATM Machine"
print(title.center(40))
pin=int(input("Enter 4 digit Pin:"))
if pin==9761:
    amount=100000
    num=("please enter your option:")
    data1=("    option 1. Cash withdraw ")
    print(data1.title())
    data2=("    option 2. Balance inquery")
    print(data2.title())
    data3=("    option 3. exit")
    print(data3)
    option=int(input("Enter your option:"))
    if option==1:
        received_amount=int(input("enter your withdraw amount:"))
        if received_amount>amount:
            print("insufficient balance")
        elif received_amount<=0:
            print("invalid amount")
        else:
         amount=amount-received_amount
         print(f"Successful! Your withdrew balance Rs.{received_amount}:")
         print(f"Your remaining balance Rs.{amount}")


    elif option==2:
       print(f'Your current Balance Rs.{amount}')
    elif option==3:
        print("Thankyou for using our ATM")
    else:
      print("Invalid option")
else:
    print("Invalid pin")







