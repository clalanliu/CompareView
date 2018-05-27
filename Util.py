import tkinter as tk
import os
from tkinter import messagebox
import GlobalVar
from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_mse as mse


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def HelpCallBack():
    messagebox.showinfo( "Help", '%8s Switch image.\n%8s Delete image.\n%8s Reload images.\n%8s Enlarge the boxed out area.\n%8s Zoom out' % ("←,↑,→,↓: ","Del: ","R: ","z/Z, num: ","Double click: "))
