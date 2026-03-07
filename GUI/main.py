import tkinter as tk # it is the built-in library in Python used to create Graphical User Interfaces (GUIs)
# In Tkinter, everything you see on the screen is called a Widget.like label(used to display text or image)
# button, Entry, Frame,canvas(drawing shapes etc) 
# used to make scientific calculator , games ,database tools entry form etc
# the same code will work in windows macos and linux 
app=tk.Tk()#Everything is call inside the tk
# print(dir(tk))
app.title("Scientific Calculator")
app.geometry("400x400")
result=tk.Entry(width=30)
# it helps below code width is optional case to increase the len 
# result.pack() to create null from
result.grid(padx=5,pady=5, row=0, column=0, columnspan=5) #grid makes 2D table like row and column like excel
#padx=horizontal padding : Add 5 px space of left to right of Entry Box
#paddy=vertical padding : Add 5 px space of top to button on Entry BOx


def take_input(parameter): #to create function
    current_value=result.get() # Get the current string from the entry widget
    result.delete(0,tk.END) #like inter 9 then i will press 8 it delete previous value and give current value
    result.insert(0,str(current_value)+str(parameter))#0 means it helps to pressing the value and showing on screen
     #combine the old text with new input(parameter) and even if 'parameter' is an int it won't crash
    print("the value is", parameter)

def add_number_Button(number):
    return tk.Button(app, text=number ,padx=40, pady=50,command=lambda:take_input(number))

def equal_value():
    current=result.get()
    total=eval(current) #print(eval("5+6")) add sub mul divide, power operation eval means equal value 
    result.delete(0,tk.END)
    result.insert(0,total)
    
def clear_value(): #for AC
    result.delete(0,tk.END) # and assigning to the Ac with command

def delete_value(): #for DEL and assign to the delete
    current=result.get()
    result.delete(0, tk.END)
    result.insert(0, current[:-1]) #remove 1 position of the value
    
last_ans="" #global variable
def show_ans():
    global last_ans #call global varaible inside the function
    current=result.get()
    total = eval(current)
    last_ans = str(total) #save here
    
    result.delete(0, tk.END)
    result.insert(0, str(current) + str(last_ans)),last_ans
    
zero=tk.Button(app,text="0", padx=9, pady=9,command=lambda:take_input("0"))
#Button(first argument(Master ie app) and second argument is (Text="0")) and padx increase the size of zero botton
one=tk.Button(app,text="1", padx=9, pady=9,command=lambda:take_input("1"))
two=tk.Button(app,text="2", padx=9, pady=9,command=lambda:take_input("2"))
three=tk.Button(app,text="3",padx=9,pady=9,command=lambda:take_input("3"))
four=tk.Button(app,text="4", padx=9, pady=9,command=lambda:take_input("4"))
five=tk.Button(app,text="5", padx=9, pady=9,command=lambda:take_input("5"))
six=tk.Button(app,text="6", padx=9, pady=9,command=lambda:take_input("6"))
seven=tk.Button(app,text="7", padx=9, pady=9,command=lambda:take_input("7"))
eight=tk.Button(app,text="8", padx=9, pady=9,command=lambda:take_input("8"))
nine=tk.Button(app,text="9", padx=9, pady=9,command=lambda:take_input("9"))

delete=tk.Button(app,text="DEL",padx=9,pady=9,command=delete_value)
Ac=tk.Button(app,text="AC",padx=9,pady=9,command=clear_value)

plush=tk.Button(app,text="+",padx=9, pady=9,command=lambda:take_input("+"))
minus=tk.Button(app,text="-",padx=9, pady=9,command=lambda:take_input("-"))
multiply=tk.Button(app,text="*",padx=9, pady=9,command=lambda:take_input("*"))
divide=tk.Button(app,text="/",padx=9, pady=9,command=lambda:take_input("/"))
dot=tk.Button(app,text=".",padx=9, pady=9,command=lambda:take_input("."))
ans=tk.Button(app,text="Ans",padx=9, pady=9,command=show_ans())
equalsto=tk.Button(app,text="=",padx=9, pady=9,command=equal_value)
power=tk.Button(app,text="x10^",padx=9, pady=9,command=lambda: take_input("**"))

zero.grid(row=6,column=0,sticky="nsew")
dot.grid(row=6,column=1,sticky="nsew")
power.grid(row=6,column=2,sticky="nsew")
ans.grid(row=6,column=3,sticky="nsew")
equalsto.grid(row=6,column=4,sticky="nsew")

one.grid(row=5,column=0,sticky="nsew")
two.grid(row=5,column=1,sticky="nsew")
three.grid(row=5,column=2,sticky="nsew")
plush.grid(row=5,column=3,sticky="nsew")
minus.grid(row=5,column=4,sticky="nsew")

four.grid(row=4,column=0,sticky="nsew")
five.grid(row=4,column=1,sticky="nsew")
six.grid(row=4,column=2,sticky="nsew")
multiply.grid(row=4,column=3,sticky="nsew")
divide.grid(row=4,column=4,sticky="nsew")

seven.grid(row=3,column=0,sticky="nsew") # Use sticky="nsew" to make the button fill the whole grid cell ie north(top) south(bottom),
# east(left),west(right) stick is widget inside the grid which manages the compass or direction like nsew
eight.grid(row=3,column=1,sticky="nsew")
nine.grid(row=3,column=2,sticky="nsew")
delete.grid(row=3,column=3,sticky="nsew")
Ac.grid(row=3,column=4,sticky="nsew")

app.mainloop()