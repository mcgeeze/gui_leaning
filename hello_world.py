import tkinter

root = tkinter.Tk()

root.title("Hello World!!!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="OwO?", fg="pink", bg="#C8A2C8", font=("Comic Sans MS", "50", "bold"))
my_label.grid()

my_label2 = tkinter.Label(root)
my_label2.config(text="UwU?!", fg="light blue", bg="pink", font=("Comic Sans MS", "30", "italic"))
my_label2.grid()

my_label3 = tkinter.Label(root)
my_label3.config(text="OwO & UwU!", fg="#C8A2C8", bg="light blue", font=("Comic Sans MS", "25", "bold"))
my_label3.grid()

root.mainloop()
