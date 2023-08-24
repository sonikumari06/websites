import webbrowser
from tkinter import *
from PIL import Image,ImageTk
def color():
    return "#57adff"
root = Tk()
root.title("WebBrowsers")
root.geometry("890x470+300+200")
root.resizable(False,False)
root.configure(bg=color())
def image_(url,size):
    img=Image.open(url)
    resized_image= img.resize(size)
    img= ImageTk.PhotoImage(resized_image)
    return img
def search():
    search_=search_text.get()
    webbrowser.open("www.google.com")
def linkedin():
    webbrowser.open("www.linkedin.com")
def youtube():
    webbrowser.open("www.youtube.com")
def whatsappweb():
    webbrowser.open("www.whatsappweb.com")
def instagram():
    webbrowser.open("www.instagram.com")
def telegram ():
    webbrowser.open("www.telegram.com")
def gmail():
    webbrowser.open("www.gmail.com")
def news():
    webbrowser.open("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
heading_image=image_("image/bar.png",(930,400))
heading_=Label(image=heading_image,bg=color())
heading_.place(x=-30,y=-125)
Label(root, text="Welcome To Links.com", bg='#b97a56', fg='black', font="Arial 15 bold").place(x=330,y=25)
Label(root,text="Click on the buttons to open website", bg="#b97a56", fg="black", font="Arial 10").place(x=350,y=55)
search_image=image_("image/search bar_1.png",(300,50))
search_=Label(image=search_image,bg=color())
search_.place(x=270,y=150)
search_text=Entry(root,justify="right",width=16,font=("poppins",20,"bold"),bg="#203652",border=0,fg="white")
search_text.place(x=280,y=160)
search_text.focus()

search_icon_=image_("image/Search_icon_.png",(50,50))
search_button=Button(image=search_icon_,borderwidth=0,cursor="hand2",bg=color(),command=search)
search_button.place(x=530,y=151)
Linkedin_icon_=image_("image/LinkedIn.png",(60,60))
Linkedin_button=Button(image=Linkedin_icon_,borderwidth=0,cursor="hand2",bg=color(),command=linkedin)
Linkedin_button.place(x=270,y=210)
youtube_icon_=image_("image/Youtube.png",(60,60))
youtube_button=Button(image=youtube_icon_,borderwidth=0,cursor="hand2",bg=color(),command=youtube)
youtube_button.place(x=400,y=210)
whatapp_icon_=image_("image/whatsapp.png",(60,60))
whatapp_button=Button(image=whatapp_icon_,borderwidth=0,cursor="hand2",bg=color(),command=whatsappweb)
whatapp_button.place(x=520,y=210)
gmail_icon_=image_("image/gmail.png",(60,50))
gmail_button=Button(image=gmail_icon_,borderwidth=0,cursor="hand2",bg=color(),command=gmail)
gmail_button.place(x=270,y=305)
instagram_icon_=image_("image/instagram.png",(60,60))
instagram_button=Button(image=instagram_icon_,borderwidth=0,cursor="hand2",bg=color(),command=instagram)
instagram_button.place(x=400,y=300)
news_icon_=image_("image/news.png",(70,70))
news_button=Button(image=news_icon_,borderwidth=0,cursor="hand2",bg=color(),command=news)
news_button.place(x=520,y=295)

root.mainloop()
