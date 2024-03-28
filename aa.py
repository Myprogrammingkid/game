import tkinter

print("hello there")
name=input("are you ready for our adventure? ")

if name == "yes" or name == "yeah" or name == "i'm ready":
    print("here we go!")
    window = tkinter.Tk()
    window["bg"]="cyan"
    window.mainloop()
else :
    print("then get out if you don't wanna go!")