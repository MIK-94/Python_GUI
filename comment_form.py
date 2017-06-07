from tkinter import *
from tkinter import messagebox

def display_full_name():
    messagebox.showinfo("GUI Python", FIO.get() + " " + str(phone.get())+" "+email.get()+" "+text_box.get("1.0",END))
 
root = Tk()
root.title("GUI на Python")
root.geometry("340x250")
 
FIO = StringVar()
phone = IntVar()
email = StringVar()
text = StringVar()
 
name_label = Label(text="Введите имя:")
phone_label = Label(text="Введите телефон:")
email_label = Label(text="Введите email:")
text_label =Label(text="Введите ваш \n коментарий:")
 
name_label.grid(row=0, column=0, sticky="w")
phone_label.grid(row=1, column=0, sticky="w")
email_label.grid(row=2,column=0, sticky="w")
text_label.grid(row=3,column=0, sticky="w")

name_entry = Entry(textvariable=FIO)
phone_entry = Entry(textvariable=phone)
email_entry = Entry(textvariable=email)
text_box = Text(root,width=23, height=5,
          font="Arial 8",
          wrap=WORD)

name_entry.insert(INSERT, "Семен Семеныч")
phone_entry.insert(INSERT, "8950000559")
email_entry.insert(INSERT, "semen@mailbox.ru")
text_box.insert(INSERT, "Hellow")
 
name_entry.grid(row=0,column=1, padx=5, pady=5)
phone_entry.grid(row=1,column=1, padx=5, pady=5)
email_entry.grid(row=2,column=1, padx=5, pady=5) 
text_box.grid(row=3, column=1, padx=5, pady=5)
 
message_button = Button(text="Отправить", command=display_full_name)
message_button.grid(row=4,column=1, padx=5, pady=5, sticky="e")
 
root.mainloop()
