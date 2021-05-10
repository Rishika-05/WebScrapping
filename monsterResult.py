from tkinter import *
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import webbrowser


root = Tk()
root.title("Monster.com Search Result")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='WebScrapping/Images/monster.png'))

monster_logo = ImageTk.PhotoImage(Image.open("WebScrapping/Images/monsterfull.png"))
label_moster = Label(image=monster_logo)

search_bar = Entry(root, width=50, borderwidth=2, font=(18))

label_moster.grid(column=0, row=0,padx=80, pady=60,columnspan=3)
search_bar.grid(column=0, row=2,columnspan=3,pady=10)

def on_click():
    search_text = search_bar.get()
    url = "https://www.google.co.in/search?q="+search_text
    headers = {"user-agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")
    flag = True
    anchors = soup.find('div', class_="g")
    # print(anchors.prettify)
    if anchors:
        link = anchors.find('a')['href']
    else:
        flag = False

    def open_link():
        webbrowser.open_new(link)
        
        
    if flag and anchors.find('h3'):
        title_label = Label(root, text=anchors.find('h3').get_text(), fg='blue')
        link_label = Label(root, text=anchors.find('cite').get_text(),fg='purple')
        des_label = Label(root, text=soup.find('div',class_='IsZvec').get_text(),fg='#888888', wraplength=900, justify="left")
        f=1;
        link_button = Button(root, text="Go to page", command=open_link,bg="#dddddd", borderwidth=2)
        link_button.config(font=(14))
        link_button.grid(column=1, row=7, pady=10,sticky="E", padx=40)
    else:
        f=0
        title_label = Label(root, text="No Results",fg="#a9a9a9")
        link_label = Label(root, text="Ooops (Search Failed)!!",fg="#a9a9a9")
        des_label = Label(root, text="Please check the text you entered, and try again.",fg="#a9a9a9")
    
    title_label.config(font=(32))
    link_label.config(font=(24))
    des_label.config(font=(16))

    
    title_label.grid(column=1, row=4, pady=0, padx=10)
    link_label.grid(column=1, row=5, pady=0, padx=10)
    des_label.grid(column=1, row=6, pady=0, padx=10)
    
    def label_del():
        title_label.grid_forget()
        link_label.grid_forget()
        des_label.grid_forget()
        exit_btn.grid_forget()
        if f==1:
            link_button.grid_forget()
        else:
            on_click()
            
    my_button = Button(root, text="Search", command=label_del, bg='#dddddd', borderwidth=2)  
    my_button.config(font=(15)) 
    my_button.grid(column=1, row=3, pady=20,padx=40)

    exit_btn = Button(root, text="Exit", command=root.quit, padx=20, bg='#dddddd', borderwidth=2)
    exit_btn.config(font=(14))
    exit_btn.grid(column=1, row=8, pady=10, padx=40)

my_button = Button(root, text="Search", command=on_click, bg='#dddddd', borderwidth=2)  
my_button.config(font=(15)) 
my_button.grid(column=1, row=3, pady=20,padx=40)


root.mainloop()