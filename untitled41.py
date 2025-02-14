#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:13:07 2025

@author: sultanalobaid
"""
from calculator import addition
import tkinter as tk
window=tk.Tk()
window.title("calc")
window.geometry("500x700")
def on_button_click():
    print("1")
button=tk.Button(window,text=("1"),command=on_button_click(),width=20,pady=50)
button.pack()
def on_button2_click():
    print("2")
button2=tk.Button(window,text=("2"),command=on_button2_click(),width=20,pady=60)
button2.pack()
def plus ():
    print(addition)
plus=tk.Button(window,text=("+"),command=plus(),width=20,pady=100)
plus.pack()
window.mainloop()