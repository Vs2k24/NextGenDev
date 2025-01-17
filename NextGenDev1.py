from tkinter import *
#create the root window
root=Tk()
root.title("simple calculator")
root.geometry("400x400")
#now make the entry box
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#define functions
def button_click(number):#here number is an argument
    current=e.get()
    e.delete(0,END)
    e.insert(END,str(current)+str(number))#insert number in the entry box and concatenate both and typecast to string
def button_clear():
    e.delete(0,END)
def button_add():
    first_number=e.get()#first we need to get the first number
    global f_num 
    global math 
    math="addition"
    f_num=int(first_number)#store the value of the firstnum in a variable
    e.delete(0,END)#delete the first number in the box so tht we can give + sign

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
       e.insert(0,f_num+int(second_number))
    if math=="subtraction":
        e.insert(0,f_num-int(second_number))
    if math=="multiplication":
        e.insert(0,f_num*int(second_number))
    if math=="division":
        e.insert(0,f_num/int(second_number))  

def button_subtract():
    first_number=e.get()#first we need to get the first number
    global f_num 
    global math 
    math="subtraction"
    f_num=int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)

def button_divide():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0,END)

#create buttons
button_1=Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))#since we took number as an argument that use lambda why we have to 
button_2=Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3=Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4=Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6=Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7=Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8=Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9=Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0=Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add=Button(root, text="+", padx=40, pady=20, command=button_add)
button_equal=Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear=Button(root, text="C",padx=40, pady=20,command= button_clear)
button_subtract=Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply=Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide=Button(root, text="/", padx=40, pady=20, command=button_divide)
#put the buttons on screen use grid
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=4,column=2)
button_equal.grid(row=4,column=3)
button_clear.grid(row=4,column=1)
button_subtract.grid(row=1,column=3)
button_multiply.grid(row=2,column=3)
button_divide.grid(row=3,column=3)
root.mainloop()
