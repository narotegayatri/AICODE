from tkinter import *
root = Tk()
root.title("Chatbot")
def send():
    send = "You -> "+e.get()
    txt.insert(END, "\n"+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi ,how can i help you")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hello,how can i help you")
    elif(e.get() == "need to know about college"):
        txt.insert(END, "\n" + "Bot -> sure, choose one: 1.collage capus 2.college enquiry 3.fee structure 4.courses  ")
    elif(user == "4"):
        txt.insert(END, "\n" + "Bot ->  there are 6 different type of courses: 1.computer engineering 2.IT 3.ENTC 4.AI&DS 5. MECHANICAL 6.CIVIL")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I dind't got you")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()