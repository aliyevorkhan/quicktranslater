#!/usr/bin/python3
#-*-coding:utf-8-*-


from googletrans import Translator
from tkinter import scrolledtext , Tk , Label , Entry ,Button , INSERT , END 
from tkinter.ttk import Combobox

class Translate:

    def __init__(self):
        self.window = Tk()
        
        self.window.title("Translate Me")
        self.window.geometry('680x430')

        self.lbl = Label(self.window, text="Çevirilecek Metin")
        self.lbl.grid(column=0, row=0)

        self.lbl = Label(self.window, text="Çevirilen Metin")
        self.lbl.grid(column=1, row=0)

        self.txt = scrolledtext.ScrolledText(self.window,width=40,height=10)
        self.txt.grid(column=0,row=11)
        self.txt.insert(INSERT ,self.window.clipboard_get())

        self.txt2 = scrolledtext.ScrolledText(self.window,width=40,height=10)
        self.txt2.grid(column=1,row=11)

        self.btn = Button(self.window, text="Translate", command=self.clicked)
        self.btn.grid(column=0, row=12)
    

        self.combo = Combobox(self.window)
        self.combo['values']= ("tr", "en")
        self.combo.current(1) #set the selected item

        self.combo.grid(column=0, row=1)

        self.combo2 = Combobox(self.window)
        self.combo2['values']= ("tr" , "en")
        self.combo2.current(1) #set the selected item

        self.combo2.grid(column=1, row=1)

    def clicked(self):
        self.txt2.delete(1.0,END)
        self.ret = self.txt.get(1.0 , END)
        self.trans = Translator()
        self.s=self.trans.translate(str(self.ret), src=str(self.combo.get()) , dest=str(self.combo2.get()))
        self.txt2.insert(INSERT, self.s.text)
    
    def loop(self):
        self.window.mainloop()



if __name__ == '__main__':
    translate = Translate()
    translate.loop()

