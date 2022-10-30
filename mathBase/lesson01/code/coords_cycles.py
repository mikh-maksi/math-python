# !/usr/bin/python3
from tkinter import *
root = Tk()
 
c = Canvas(root, width=200, height=200, bg='white')
c.pack()



def point(x):
    c.create_oval(15+x*30, 85, 25+x*30, 75, outline="#f00",
                fill="#f00", width=2)
    c.create_text(100, 35, text=x, 
                justify=CENTER, font="Verdana 40")

def point_clear(x):
    c.create_oval(15+x*30, 85, 25+x*30, 75, outline="#fff",
                fill="#fff", width=2)
    
    c.create_text(100, 35, text=x, fill = "#fff",
                justify=CENTER, font="Verdana 50")

    c.create_rectangle(70,10,130,60,fill='white',outline="#fff")



c.create_line(0, 100, 200, 100, fill='red',
                width=5, arrow=LAST, 
                activefill='#AA0000',
                arrowshape="10 20 10")

for i in range(6):
    c.create_line(20+i*30, 110, 20+i*30, 90, fill='red',
                width=5,  
                activefill='#AA0000',
                arrowshape="10 20 10")

    c.create_text(20+i*30, 125, text=i, 
                justify=CENTER, font="Verdana 20")
    
c.after(5000)
c.update()

for i in range(6):
    point(i)
    c.after(500)
    c.update()
    point_clear(i)
point(5)



c.create_text(20, 125, text="0", 
                justify=CENTER, font="Verdana 20")

root.mainloop()