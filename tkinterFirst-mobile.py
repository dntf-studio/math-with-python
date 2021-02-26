import tkinter as tk
import tkinter.messagebox as tkmsg
import tkinter.font as tkFont
import math

root = tk.Tk()
root.title('first')

HEIGHT = 800
WIDTH = 360
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()
fontstyle = tkFont.Font(family="Lucida Grande",size=21)
fontstyle2 = tkFont.Font(family="UTF-8",size=23)

bigfont = tkFont.Font(family="UTF-8",size=20)

q_nrs = []
def helloCallBack():
    q_nrs2 = int(entry.get())
    print('loaded')
    q_nrs.append(q_nrs2)
    #text.set(q_nrs)
    label3['text'] = q_nrs
    entry.delete(0,tk.END)

def math2():
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
    print('標準偏差',q_nrs_aa)
    label4['text'] = "分散=",q_nrs_ss,"\n","標準偏差=",q_nrs_aa

frame = tk.Frame(root,bg="#e6e6e6")
frame.place(relx=0,rely=0, relwidth=1, relheight=1 )

button = tk.Button(frame, text="AddNumber",command = helloCallBack,font=bigfont)
button.place(x=210,y=100)

button2 = tk.Button(frame, text="Calculate",command = math2,font=bigfont)
button2.place(x=210,y=200)

label = tk.Label(frame,text="PutNumbers->",bg='white')
label.place(x=1,y=1)

label3 = tk.Label(frame,text="null",font=fontstyle,bg="#e6e6e6")
label3.place(x=30,y=400)

label4 = tk.Label(frame,text="[result]",font=fontstyle2,bg="#e6e6e6")
label4.place(x=1,y=560)

entry = tk.Entry(frame)
entry.place(x=84.7,y=2)

root.mainloop()