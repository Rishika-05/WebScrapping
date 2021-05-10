from tkinter import *
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import webbrowser


root = Tk()
root.title("Google First Search Result")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='WebScrapping/Images/google.png'))

search_logo = ImageTk.PhotoImage(Image.open("WebScrapping/Images/googlefull.png"))
label_search = Label(image=search_logo)
Label_0 = Label(root, text="Search here:")
Label_0.config(font=(42))

search_bar = Entry(root, width=50, borderwidth=1, font=(18))

label_search.grid(column=1, row=0,padx=80, pady=80,columnspan=2)
Label_0.grid(column=1, row=1,pady=20,columnspan=2)
search_bar.grid(column=1, row=2,columnspan=2)

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
        des_label = Label(root, text=soup.find('div',class_='IsZvec').get_text(),fg='#888888')
        
        link_button = Button(root, text="Visit page", command=open_link, borderwidth=2)
        link_button.config(font=(14))
        link_button.grid(column=1, row=7, pady=10)
    else:
        title_label = Label(root, text="No Results",fg="#a9a9a9")
        link_label = Label(root, text="Ooops (Search Failed)!!",fg="#a9a9a9")
        des_label = Label(root, text="Please check the text you entered, and try again.",fg="#a9a9a9")
    
    title_label.config(font=(32))
    link_label.config(font=(24))
    des_label.config(font=(16))

    
    title_label.grid(column=1, row=4, columnspan=2, sticky="W", pady=0, padx=10)
    link_label.grid(column=1, row=5, columnspan=2, sticky="W", pady=0, padx=10)
    des_label.grid(column=1, row=6, columnspan=2, sticky="W", pady=0, padx=10)

    def label_del():
        title_label.grid_forget()
        link_label.grid_forget()
        des_label.grid_forget()
        on_click()

    my_button = Button(root, text="Google Search", command=label_del, bg='#dddddd', borderwidth=2)  
    my_button.config(font=(15)) 
    my_button.grid(column=1, row=3, pady=20)
    
    my_button = Button(root, text="I'm Feeling Lucky", command=label_del, bg='#dddddd', borderwidth=2)  
    my_button.config(font=(15)) 
    my_button.grid(column=2, row=3, pady=10)

    exit_btn = Button(root, text="Exit", command=root.quit, padx=20, bg='#dddddd', borderwidth=2)
    exit_btn.config(font=(14))
    exit_btn.grid(column=2, row=7, pady=10)

my_button = Button(root, text="Google Search", command=on_click, bg='#dddddd', borderwidth=2)  
my_button.config(font=(15)) 
my_button.grid(column=1, row=3, pady=20)
    
my_button = Button(root, text="I'm Feeling Lucky", command=on_click, bg='#dddddd', borderwidth=2)  
my_button.config(font=(15)) 
my_button.grid(column=2, row=3, pady=10)

root.mainloop()