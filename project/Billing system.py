'''Programming Assignment: Computer Bazar Billing System
Problem :
Create a Python program for "Computer Bazar" that acts as an automated point-of-sale system.
The program should calculate the final bill for a customer based on their product choice, delivery preferences,
packing requirements, and location-based taxes.

Requirements
1. Product Selection
Display a menu with the following items and prompt the user to choose one and specify the quantity:
       1.Dell: Rs.20,000
       2.Lenovo: Rs.25,000
       3.MacOS: Rs. 50,000

2. Delivery Options
Ask the user how they would like to receive their item:
       1.Home Delivery: Rs. 1,000 fee.
       2.Pickup: Free.

3. Packing Options
Provide a choice for packaging:
       1.Plastic: Free.
       2.Bag: Rs. 1,500.
       3.Gift Box: Rs. 3,500.

4. Location & Tax (VAT)
The tax depends on the delivery location. Calculate tax based on the total product price (before delivery and packing):
       1.Kathmandu (KTM): 0% Tax.
       2.Bhaktapur: 13% VAT added to the total.
       3.Lalitpur: 0% Tax.

5. Final Output
Generate a "Final Bill" that clearly displays:
       1.The Product Name and Quantity.
       2.The Tax Amount (if applicable).
       3.The Grand Total (Product Price + Delivery + Packing + Tax).'''

title = "Computer Bazar"
print(title.center(40))
x="product list"
print(x.center(40))
print("1.Dell(Rs.20000)".center(20))
print("2.Lenovo(Rs.2500)".center(22))
print("3.Macos(50000)".center(18))

dell_price = 0
Lenovo_price = 0
Macos_price = 0
product_name = ''
quantity = 0  #that means initial zero add to sum
option = int(input("Enter any option from 1 to 3: "))
if option == 1:
    quantity = int(input("Enter quantity:"))
    dell_price = 20000 * quantity
    product_name = "Dell"

elif option == 2:
    quantity = int(input("Enter quantity:"))
    Lenovo_price = 25000 * quantity
    product_name = "Lenovo"
elif option == 3:
    quantity = int(input("Enter quantity:"))
    Macos_price = 50000 * quantity
    product_name = "Macos"
else:
    print("invalid option")
    exit()

  #total price calculated here
total_amount = float(dell_price + Lenovo_price + Macos_price)

#Delivery calculation
delivery_charge = 0
print("1.Home Delivery(Rs.1000)".center(30))
print("2.Pickup(Free)".center(20))
Del_option = int(input("Enter Delivery Option: "))
if Del_option == 1:
    delivery_charge = 1000
elif Del_option == 2:
    delivery_charge = 0
else:
    print("Invalid option")

#Packing charge
packing_charge = 0
print("1.Plastic(Free)".center(20))
print("2.Bag(Rs.1500)".center(18))
print("3.Gift_wrap_Box(Rs.3500)".center(27))
print("4.No Bag".center(12))
Pac_option = int(input("Enter Packing Option: "))
if Pac_option == 1:
    packing_charge = 0

elif Pac_option == 2:
    Packing_charge = 1500

elif Pac_option == 3:
    packing_charge = 3500

else:
    packing_charge = 0

# tax Calculation
tax_amount = 0
print("1.Ktm(0 tax)".center(16))
print("2.Bhaktapur(13% tax will be added on your total amount)".center(60))
print("3.Lalitpur(0 tax)".center(22))
option1 = int(input("Enter your location code:"))
if option1 == 1:
    tax_amount = 0
elif option1 == 2:
    tax_amount = total_amount * 0.13
else:
    tax_amount = 0

#Grand total calculation
Grand_total = total_amount + delivery_charge + packing_charge + tax_amount

#final bill calculation
print("============================")
title1 = "FINAL BILL"
print("=============================")
print(title1.center(40))
print(f"product Name={product_name}")
print(f"quantity:{quantity}")
print(f"total amount Rs:{total_amount}")
print(f"delivery charge Rs:{delivery_charge}")
print(f"packing charge Rs:{packing_charge}")
print(f"tax_amount:{tax_amount}")
print("---------------------------- ")
print(f"Grand total Rs:{Grand_total}")
print("=============================")
