from Crypto.Cipher import DES
from Tkinter import *
key=DES.new('12345678')
root=Tk()
root.title('Editor Maker')
def save():
    global x,t,root1,key
    f=open(x,'w')
    data=t.get(1.0,END)
    size=len(data)
    if(size%8==0):
        ec=key.encrypt(data)
        f.write(ec)
        f.close()
    else:
        b=size%8
        n=8-b
        for i in range(0,n):
            data=data+' '
        ec=key.encrypt(data)
        f.write(ec)
        f.close()
def open2():
    global root1,t,en,key
    f=open(en.get(),'r')
    root1=Tk()
    t=Text(root1)
    t.grid(row=0,column=0)
    data2=f.read()
    s=key.decrypt(data2)
    t.insert(1.0,s)
    root1.mainloop()
def open1():
    global en,x,y,root1,t
    x=en.get()
    root.destroy()
    root1=Tk()
    root1.title(x)
    t=Text(root1)
    t.grid(row=0,column=0)
    Button(root1,text="Save",command=save).grid(row=20,column=0)
    Button(root1,text="Discard",command=root1.destroy).grid(row=20,column=1) 
    root1.mainloop()
Label(root,text="File name: ").grid(row=0,column=0)
en=Entry(root)
en.grid(row=0,column=1)
Button(root,text="Open",command=open1).grid(row=0,column=2)
Button(root,text="Open Existing File",command=open2).grid(row=0,column=3)
root.mainloop()
