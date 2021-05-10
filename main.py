from tkinter import *
from PIL import Image,ImageTk
import os

root = Tk()
root.title("IEEE LEAD 2.0 [Web Scraping Project]")
# root.iconphoto(False, PhotoImage(file='Programs/WebScrapping/Images/th.jfif'))
root.call('wm', 'iconphoto', root._w, PhotoImage(file='WebScrapping/Images/ieee.png'))
logo = ImageTk.PhotoImage(Image.open("WebScrapping/Images/Web-Scrap.jpg"))
l_logo = Label(image=logo)
l_logo.grid(row=0,column=1, columnspan=4, pady=20, padx=20)

gs_logo = ImageTk.PhotoImage(Image.open("WebScrapping/Images/web_gs.png"))
label_gs = Label(image=gs_logo)
label_gs.grid(column=1, row=3)


def open_gs():
    os.system('python WebScrapping/googleSearchResult.py')
    
gs_btn = Button(root, text="Google Search Results", command=open_gs, bg='#dddddd', borderwidth=5)
gs_btn.config(font=(15))
gs_btn.grid(column=1, row=4, pady=10)





exit_btn = Button(root, text="Exit", command=root.quit, padx=20, bg='#dddddd', borderwidth=2)
exit_btn.config(font=(14))
exit_btn.grid(column=1, row=6, pady=10, columnspan=3)



mainloop()