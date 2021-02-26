import tkinter as tk
import tkinter.messagebox as tkmsg
import math

root = tk.Tk()
root.title('first')

HEIGHT = 700
WIDTH = 800
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

def helloCallBack():
    text.set("You put:"+str(entry.get()))
    #tkmsg.showinfo("Hello!!Python!!","Hello World")
    print('loaded')
    q_nrs = [50,70,90,80,50]
    q_nrs_len = len(q_nrs)
    q_nrs_sum = sum(q_nrs)
    q_nrs_mean = q_nrs_sum/q_nrs_len
    print('mean:',q_nrs_mean)

    q_nrs_al = 0
    if len(q_nrs) != 0:
        for q_nrs_each in q_nrs:
            q_nrs_each = q_nrs_each**2
            q_nrs_al +=  q_nrs_each

    print('all:',q_nrs_al)
    q_nrs_1x2_mean = q_nrs_al/q_nrs_len
    print('x2の平均値:',q_nrs_1x2_mean)
    q_nrs_ss = q_nrs_1x2_mean-q_nrs_mean**2
    print('分散=',q_nrs_ss)
    q_nrs_aa = math.sqrt(q_nrs_ss)
    print('標準偏差=',round(q_nrs_aa,1))

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