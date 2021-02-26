import tkinter as tk
import tkinter.messagebox as tkmsg

root = tk.Tk()
root.title('first')

HEIGHT = 700
WIDTH = 800
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

def helloCallBack():
    #txt = entry.get()
    text.set("You put:"+str(entry.get()))
    #tkmsg.showinfo("Hello!!Python!!","Hello World")
    print('loaded')

frame = tk.Frame(root,bg="#e6e6e6")
frame.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.8 )

button = tk.Button(frame, text="Test Button",command = helloCallBack)
button.place(x=210,y=1)

label = tk.Label(frame,text="This is a label",bg='white')
label.place(x=1,y=1)

text = tk.StringVar(frame)
text.set("aaaa")

label2 = tk.Label(frame,textvariable=text)
label2.place(x=1,y=30)

entry = tk.Entry(frame)
entry.place(x=80,y=2)

root.mainloop()