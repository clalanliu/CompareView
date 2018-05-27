import tkinter as tk
import os
import PIL.Image
from PIL import ImageTk, ImageDraw
import GlobalVar
from ImgSeries import ImgSeries

class ThumbNailSeries(ImgSeries):
    def __init__(self,master,ImgSeri):
        self.tn_ims=[]
        self.tn_btns=[]
        self.button_row = tk.Frame(master, height = 20, width = 240)
        self.button_row.pack(fill = "x", anchor = 'nw')
        self.pU=ImageTk.PhotoImage(file="./icon/UpArrow.png") ## keep a reference!
        self.pD=ImageTk.PhotoImage(file="./icon/DownArrow.png") ## keep a reference!
        self.shiftUpBt = tk.Button(self.button_row, image=self.pU,width="20",height="20",anchor=tk.NW)
        self.shiftDownBt = tk.Button(self.button_row, image=self.pD,width="20",height="20",anchor=tk.NW)
        self.shiftUpBt.pack(side=tk.LEFT,anchor="n")
        self.shiftDownBt.pack(side=tk.LEFT,anchor="n")
        self.shiftUpBt.config(command = lambda: self.ShiftUp())

        self.thumb_col = tk.Frame(master)
        self.thumb_col.pack(expand = True, fill = "both", anchor = 'nw')
        self.imgseries = ImgSeri
        self.activeTN = -1


    def color_change(self,i, clr):
        self.tn_btns[i].config(bg=clr)
    
    def AddTN(self, im):
        size = (self.thumb_col.winfo_width()-2,int(self.thumb_col.winfo_height()/8)-2)
        im.thumbnail(size,PIL.Image.ANTIALIAS)
        p = ImageTk.PhotoImage(im)
        self.DyeButtonBack()
        tmpLeng = len(self.tn_btns)
        self.activeTN = len(self.tn_btns)
        self.tn_btns.append(tk.Button(self.thumb_col, image=p ,bg='yellow', width=size[0]+2, height=size[1]+2,command= lambda x=tmpLeng: self.ButtonEvent(x)))
        self.tn_btns[-1].pack()
        self.tn_ims.append(p) ## keep a reference!
    
    def DyeButtonBack(self):
        for i in range(len(self.tn_btns)):
            self.color_change(i, GlobalVar.DefClr)
    
    def ButtonEvent(self,x):
        self.DyeButtonBack()
        self.activeTN = x
        self.tn_btns[x].config(bg="yellow")
        self.imgseries.reshow(x)

    def Last(self):
        if self.activeTN > 0:
            self.ButtonEvent(self.activeTN-1)

    def Next(self):
        if self.activeTN < len(self.tn_btns)-1:
            self.ButtonEvent(self.activeTN+1)

    def ShiftUp(self):
        if self.activeTN > 0:
            self.tn_ims[self.activeTN], self.tn_ims[self.activeTN-1] =  self.tn_ims[self.activeTN-1], self.tn_ims[self.activeTN]
            self.tn_btns[self.activeTN].config(image=self.tn_ims[self.activeTN])
            self.tn_btns[self.activeTN-1].config(image=self.tn_ims[self.activeTN-1])
            self.imgseries.ShiftUp(self.activeTN)
            self.Last()
          

    def Delete(self):
        if len(self.tn_btns)==0:
            return
        self.tn_btns[self.activeTN].pack_forget()
        del self.tn_btns[self.activeTN]
        del self.tn_ims[self.activeTN]
        if self.activeTN<0:
            return
        elif self.activeTN==0 and len(self.tn_btns)==0:
            self.activeTN = -1
        elif self.activeTN==0 and len(self.tn_btns)!=0:
            self.ButtonEvent(self.activeTN)
        elif self.activeTN>=len(self.tn_btns):
            self.ButtonEvent(self.activeTN-1)
        else :
            self.ButtonEvent(self.activeTN)

    def Reload(self):
        size = (self.thumb_col.winfo_width()-2,int(self.thumb_col.winfo_height()/8)-2)
        for i in range(len(self.tn_btns)):
            im = PIL.Image.open(self.imgseries.im_paths[i])
            im.thumbnail(size,PIL.Image.ANTIALIAS)
            p = ImageTk.PhotoImage(im)
            self.tn_btns[i].config(image=p)
            self.tn_ims[i] = p
      
