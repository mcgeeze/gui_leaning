import tkinter

root = tkinter.Tk()


def print_uwu():
    print("UwU")


button1 = tkinter.Button(root)
button1.config(text="Owo?",
               fg="white",
               bg="pink",
               font=("Comic Sans MS", "25"),
               command=print_uwu)


button1.grid()

root.mainloop()
