# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_line(0, 100, 200, 100, fill='red',
                width=5, arrow=LAST, 
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_line(20, 110, 20, 90, fill='red',
                width=5,  
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_line(50, 110, 50, 90, fill='red',
                width=5,  
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_line(80, 110, 80, 90, fill='red',
                width=5,  
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_line(110, 110, 110, 90, fill='red',
                width=5,  
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_line(140, 110, 140, 90, fill='red',
                width=5,  
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_line(170, 110, 170, 90, fill='red',
                width=5,  
                activefill='#AA0000',
                arrowshape="10 20 10")

c.create_text(20, 125, text="0", 
                justify=CENTER, font="Verdana 20")

c.create_text(50, 125, text="1", 
                justify=CENTER, font="Verdana 20")

c.create_text(80, 125, text="2", 
                justify=CENTER, font="Verdana 20")

c.create_text(110, 125, text="3", 
                justify=CENTER, font="Verdana 20")

c.create_text(140, 125, text="4", 
                justify=CENTER, font="Verdana 20")

c.create_text(170, 125, text="5", 
                justify=CENTER, font="Verdana 20")

c.create_text(100, 35, text="0", 
                justify=CENTER, font="Verdana 40")

c.create_oval(45, 85, 55, 75, outline="#1f1",
    fill="#1f1", width=2)

# c.create_text(100, 100, text="Hello World,\nPython\nand Tk", 
#                 justify=CENTER, font="Verdana 20")
# c.create_text(200, 200, text="About this", 
#                 anchor=SE, fill="grey")

root.mainloop()