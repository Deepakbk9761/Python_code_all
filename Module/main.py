#what is module?
# module is a file containing python definitions and statement.
# module is simply a file with the .py extension. It allows to logically organize your Python code.

# Types of modules:
# 1.Bulit_in module:Pre-in,stalled with Python like math as 
# a.math[squrt(),pow(),pi(),factorital()],
# b.[generating random number(choice(),suffle()]
# c.os[operating system task(listdir(),getcrd() etc]
# d.datetime(now(),date.today())
# e.platform[system information(system(),processor()]
# eg:
# import calendar
# print(calendar.month(2006,4))

import datetime
# print(datetime.datetime.now())
today=datetime.datetime.now()
Birth_day=datetime.datetime(2023,9,16)
print(today-Birth_day)


# 2.userdefine_module:Created by the user to serve specific purposes in a project.

# import calculator as cal # calculator:module cal:Nickname of calculator ie as:Aliasing
# print(calculator.add(40,50))

# print(cal.add(70,90))
# print(cal.mul(5,6))



# from calculator import add,mul #instead of add and mul we use *(Importing everything from a module)
# from calculator import *#importing everythin from a module
# print(add(10,20))
# print(mul(5,7))

# from lib import * #first we should create lib folder then inside this folder we also create another file ie __init__.py file
#  and inside the __init__.py we should write like __all__=[file name like'calculator']
# print(calculator.add(10,20))
# print(product.product_add(95,105))

# NOte: Module use garda 2 ota folder maximum use hunxa eauta main another is lib. sabai code lib vitra file banaye
# code lekhinxa ani excess chai main folder bata garinxa like above example.

# Module/                 <-- Root Folder
# │
# ├── main.py                 <-- Entry point Accessed Code from here)
# │
# └── lib/                    <-- Library Folder  Logic written here)
#     ├── __init__.py         <-- Makes 'lib' a package
#     ├── calculator.py       <-- Module file
#     └── product.py            <-- Another file