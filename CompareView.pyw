import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import glob
import Util, GlobalVar,ImgSeries,ThumbNailSeries

# root and frame container
GlobalVar.width = 540
GlobalVar.height =360
root = tk.Tk()
root.title('CompareView')
root.geometry("540x360")
GlobalVar.DefClr = root.cget("bg")
imgSeri = ImgSeries.ImgSeries(root)

# Thumbnail window
thumbWin = tk.Toplevel(root)
thumbWin.geometry("%dx%d+%d+%d" % (240, root.winfo_screenheight(), root.winfo_screenwidth()-240, 0))
thumbWin.title('Thumbnails')
thumbWin.protocol('WM_DELETE_WINDOW', lambda:None)
thumbWin.resizable(False, False)
thumbNails = ThumbNailSeries.ThumbNailSeries(thumbWin, imgSeri)


### mouse and keyboard event
def HotkeySetRef(event):
    imgSeri.SetReference()
def HotkeyMSE(event):
    imgSeri.CompareMSE()
def HotkeyPSNR(event):
    imgSeri.ComparePSNR()
def HotkeyOpenFile(event):
    thumbNails.AddTN(imgSeri.OpenFile())

def LeftKey(event):
    imgSeri.Last()
    thumbNails.Last()

def RightKey(event):
    imgSeri.Next()
    thumbNails.Next()

def DeleteKey(event):
    imgSeri.Delete()
    thumbNails.Delete()

def Reload(event):
    imgSeri.Reload()
    thumbNails.Reload()


def MouseWheel(event):
    global mouseCount
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        RightKey(event)
    if event.num == 4 or event.delta == 120:
        LeftKey(event)


# menu bar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
compmenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label = 'Open', command = lambda: thumbNails.AddTN(imgSeri.OpenFile()),accelerator='Ctrl+O') 
filemenu.add_command(label = 'Reload', command = lambda:Reload,accelerator='R')
filemenu.add_command(label = 'Help', command = Util.HelpCallBack)
filemenu.add_command(label = 'Exit', command = lambda:exit())
menubar.add_cascade(label = 'File', menu = filemenu)
compmenu.add_command(label = 'ZoomIn', command = imgSeri.ZoomIn,accelerator='Z')
compmenu.add_command(label = 'ZoomOut', command = imgSeri.ZoomBack)
compmenu.add_command(label = 'SetReference', command = imgSeri.SetReference,accelerator='S')
compmenu.add_command(label = 'MSE', command = imgSeri.CompareMSE,accelerator='M')
compmenu.add_command(label = 'PSNR', command = imgSeri.ComparePSNR,accelerator='P')
compmenu.add_command(label = 'SSIM', command = imgSeri.CompareSSIM)
menubar.add_cascade(label = 'Compare', menu = compmenu)
root.config(menu=menubar)


### Hot key
root.bind_all('<Control-O>', HotkeyOpenFile)
root.bind_all('<Control-o>', HotkeyOpenFile)
root.bind_all('<S>', HotkeySetRef)
root.bind_all('<s>', HotkeySetRef)
root.bind_all('<M>', HotkeyMSE)
root.bind_all('<m>', HotkeyMSE)
root.bind_all('<P>', HotkeyPSNR)
root.bind_all('<p>', HotkeyPSNR)
### switch
root.bind_all('<Left>', LeftKey)
root.bind_all('<Right>', RightKey)
root.bind_all('<Up>', LeftKey)
root.bind_all('<Down>', RightKey)
root.bind_all('<Delete>', DeleteKey)
root.bind_all('<R>', Reload)
root.bind_all('<r>', Reload)
root.bind_all('<MouseWheel>', MouseWheel)
thumbWin.bind_all('<Left>', LeftKey)
thumbWin.bind_all('<Right>', RightKey)
thumbWin.bind_all('<Up>', LeftKey)
thumbWin.bind_all('<Down>', RightKey)
thumbWin.bind_all('<Delete>', DeleteKey)
thumbWin.bind_all('<R>', Reload)
thumbWin.bind_all('<r>', Reload)
thumbWin.bind_all('<MouseWheel>', MouseWheel)

### zoom
root.bind('<Double-Button-1>', imgSeri.ZoomBack)
root.bind("<z>", imgSeri.ZoomIn)
root.bind("<Z>", imgSeri.ZoomIn)
for i in range(9):
    root.bind(str(i), imgSeri.ZoomClone)

root.mainloop()