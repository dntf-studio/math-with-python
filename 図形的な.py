import tkinter

class MyApp1(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

         #キャンバスを作成
        self.canvas = tkinter.Canvas(root, bg="white", height=300, width=300)
        
        # 図形を描く
        self.canvas.create_polygon(250, 10, 220, 100, 150, 100,fill="green")
        # キャンパスを描画
        #self.canvas.place(x=0, y=0)
        self.canvas.pack()
        

root = tkinter.Tk()
root.geometry("400x300") #Windowのサイズ設定
root.title("Let's Use a Canvvas") #タイトル作成
app = MyApp1(master=root)
app.mainloop()