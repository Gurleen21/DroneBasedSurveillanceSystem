import tkinter as tk
import os
from Config import *
import threading
global hdiv
global vdiv
hval = 3
vval = 3
ss = 0
global updateButton
from ESRGAN import esrgan_independant_runner
from ESRGAN import esrgan_independant_runner_test
from keras.models import load_model
generator = load_model(Model_Path, compile=False)

def draw():
    global hdiv
    global vdiv
    global updateButton
    global ss
    master = tk.Tk()
    tk.Label(master, text='Horizontal Divisions').grid(row=1,column=2)
    tk.Label(master, text='Vertical Divisions').grid(row=2,column=2)
    tk.Label(master, text=' ').grid(row=1, column=1)
    tk.Label(master, text=' ').grid(row=1, column=4)
    tk.Label(master, text=' ').grid(row=2, column=1)
    tk.Label(master, text=' ').grid(row=2, column=4)
    tk.Label(master, text=' ').grid(row=4, column=1)
    tk.Label(master, text=' ').grid(row=4, column=3)
    tk.Label(master, text=' ').grid(row=4, column=5)
    tk.Label(master, text=' ').grid(row=3)
    tk.Label(master, text=' ').grid(row=5)
    hdiv = tk.Entry(master)
    hdiv.grid(row=1,column=4)
    vdiv = tk.Entry(master)
    vdiv.grid(row=2,column=4)
    tk.Button(master, text="Update", command=update).grid(row=4, column=2)
    updateButton = tk.Button(master, text='Start', command=startstop,background='Green')
    updateButton.grid(row=4, column=4)
    t1 = threading.Thread(target=startfunc)
    t1.start()
    tk.mainloop()

def startfunc():
    global ss
    global hval
    global vval
    while(ss==1):
        #esrgan_independant_runner_test(hval,vval,r"C:\Users\ishit\Desktop\ishit_picture.jpg")
        esrgan_independant_runner(hval, vval,generator,10)
def startstop():
    global ss
    global updateButton
    if(ss==0):
        ss = 1
        updateButton['text']='Stop'
        updateButton['background']='Red'
    else:
        ss = 0
        updateButton['text'] = 'Start'
        updateButton['background'] = 'Green'
    print(ss)
def update():
    global hdiv
    global vdiv
    global hval
    global vval
    hval = hdiv.get()
    vval = vdiv.get()
    if hval=='':
        hval = 3
    if vval=='':
        vval = 3
    print(hval,vval)

if __name__ == "__main__":
    draw()
