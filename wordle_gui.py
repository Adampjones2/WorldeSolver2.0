# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 19:32:45 2022

@author: adamp
"""

import tkinter
answer = "CRAMP"
window = tkinter.Tk()

window.title("WORDLE App")

Lbl1 = tkinter.Label(window, text = "WORDLE")
Lbl1.grid(column = 0, row = 0, columnspan = 5)

my_entries = []
for x in range(5):
    my_entry = tkinter.Entry(window)
    my_entry.grid(column = x, row = 1)
    my_entries.append(my_entry)

my_labels = []
for x in range(6):    
    my_label = tkinter.Label(window, text = "")
    my_labels.append(my_label)

         
def okay_fn():
    guess = ""
    for x in range(5):
        guess = guess + my_entries[x].get() 
        my_entries[x].grid(column = x, row=my_entries[x].grid_info()['row']+1)
    my_labels[B1.grid_info()['row'] - 2].config(text = guess)
    my_labels[B1.grid_info()['row'] - 2].grid(column=0, row=B1.grid_info()['row']-2+1, columnspan=5)
    
    B1.grid(column = 2, row = B1.grid_info()['row']+1)
        
 
B1 = tkinter.Button(window, text = "OK", command = okay_fn)
B1.grid(column = 2, row = 2)

window.mainloop() 