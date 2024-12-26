from  tkinter import  *

window=Tk()
window.minsize(width=500,height=500)
window.title("Widget Example")
window.config(padx=20,pady=20)

#label
label=Label(text="This is new text")
label.grid(column=4,row=1)

text_box1=Entry(width=30)   #a text_box with just one line
text_box1.insert(END, string="some text to begin with")
text_box1.grid(column=4,row=2)
text1=text_box1.get()

def click():
    label["text"]=text1
button=Button(text="Click Me",command=click,font=("arial",12))
button.config(padx=30,pady=30)
button.grid(column=4,row=5)


text_box2=Text(width=30,height=5)  #a text_box with just more than one line
text_box2.grid(column=4,row=3)
text_box2.focus() # set cursor on this object(text)
text_box2.insert(END,"Example of multi_line Text entry")
text2=text_box2.get("1.0",END) #from first line(1) , character 0 until End of the text


def spinbox_used():
    print(f"spinbox={spinbox.get()}")
spinbox=Spinbox(from_=0 ,to=10,width=5,command=spinbox_used)
spinbox.grid(column=5,row=2)

#scale_bar
def scale_used(value): #*********** to access to value of scale bar===> we just need to pass value to the function
    print(f"scale={value}")
scale=Scale(from_=0,to=100,width=15,command=scale_used)
scale.grid(column=5,row=3)

def checkButton_used():
    print(checked_state.get())
checked_state=IntVar() #we create Check_box with this method
check_box=Checkbutton(text="is on?",variable=checked_state,command=checkButton_used)  #set properties of cherckbox
check_box.grid(column=5,row=4)

def radio_used():
    print(radio_state.get())
radio_state=IntVar()
radio_button_1=Radiobutton(text="Option1", variable=radio_state,value=1, command=radio_used)
radio_button_1.grid(column=5,row=5)

radio_button_2=Radiobutton(text="Option1", variable=radio_state,value=2, command=radio_used)
radio_button_2.grid(column=5,row=6)

fruits=["apple","banana","mango","cucumber","pear"]
list_box=Listbox(height=4)
def listbox_used(event): #we receive the event action from user that we already defined as "<<ListboxSelect>>"
    print(list_box.get(list_box.curselection()))
for item in fruits:
    list_box.insert(fruits.index(item),item)
list_box.bind("<<ListboxSelect>>",listbox_used)
list_box.grid(column=4,row=4)

window.mainloop()