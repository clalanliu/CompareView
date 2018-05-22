import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from tkinter.filedialog import askopenfilename
import glob
import Util, GlobalVar

# root and frame container
GlobalVar.width = 540
GlobalVar.height =360
root = tk.Tk()
root.title('WheelViewer')
root.geometry("540x360")
GlobalVar.DefClr = root.cget("bg")
imgSeri = Util.ImgSeries(root)

# Thumbnail window
thumbWin = tk.Toplevel(root)
thumbWin.geometry("%dx%d+%d+%d" % (240, root.winfo_screenheight(), root.winfo_screenwidth()-240, 0))
thumbWin.title('Thumbnails')
thumbWin.protocol('WM_DELETE_WINDOW', lambda:None)
thumbWin.resizable(False, False)
thumbNails = Util.ThumbNailSeries(thumbWin, imgSeri)

# menu bar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label = 'Open', command = (lambda: Util.combine_funcs( 
                                                            thumbNails.AddTN(imgSeri.OpenFile())                                  
                                                            )))
filemenu.add_command(label = 'Help', command = Util.HelpCallBack)
filemenu.add_command(label = 'Exit', command = lambda:exit())
menubar.add_cascade(label = 'File', menu = filemenu)
root.config(menu=menubar)


# mouse and keyboard event  
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

### switch
root.bind_all('<Left>', LeftKey)
root.bind_all('<Right>', RightKey)
root.bind_all('<Up>', LeftKey)
root.bind_all('<Down>', RightKey)
root.bind_all('<Delete>', DeleteKey)
root.bind_all('<space>', Reload)
root.bind_all('<MouseWheel>', MouseWheel)
thumbWin.bind_all('<Left>', LeftKey)
thumbWin.bind_all('<Right>', RightKey)
thumbWin.bind_all('<Up>', LeftKey)
thumbWin.bind_all('<Down>', RightKey)
thumbWin.bind_all('<Delete>', DeleteKey)
thumbWin.bind_all('<space>', Reload)
thumbWin.bind_all('<MouseWheel>', MouseWheel)

### zoom
root.bind('<Double-Button-1>', imgSeri.ZoomBack)
root.bind("<z>", imgSeri.ZoomIn)
root.bind("<Z>", imgSeri.ZoomIn)
for i in range(9):
    root.bind(str(i), imgSeri.ZoomClone)

root.mainloop()