BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random


def time_counter(count,current_card):
    if count>0:
        window.after(1000,time_counter,count-1,current_card)
    elif count<=0:
        #back_ground = PhotoImage(file="images/card_back.png")
        canvas.itemconfig(fore_card, image=back_card)
        canvas.itemconfig(tittle,text="English",fill="white")
        canvas.itemconfig(vocabulary,text=current_card["English"],fill="white")
        #canvas.itemconfig(highlightthickness=1)


def right_button_fonc():
    #back_ground = PhotoImage(file="images/card_back.png")


    canvas.itemconfig(back_card, image=fore_card)
    canvas.itemconfig(tittle,text="French",fill="black")
    current_card=random.choice(list_of_csv)

    canvas.itemconfig(vocabulary,text=current_card["French"],font=("Ariel",30,"bold"),fill="black")
    time_counter(3,current_card)



def wrong_button_fonc():
    canvas.itemconfig(back_card, image=fore_card)
    canvas.itemconfig(tittle,text="French",fill="black")
    current_card = random.choice(list_of_csv)

    canvas.itemconfig(vocabulary,text=current_card["French"],fill="black")
    time_counter(3,current_card)


data=pandas.read_csv("data/french_words.csv")
df=pandas.DataFrame(data)
list_of_csv=df.to_dict(orient="records")
#print(list_of_csv[0])

window=Tk()
window.title("flash card app")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

back_ground = PhotoImage(file="images/card_back.png")
back_card=canvas.create_image(400,263,image=back_ground)
fore_ground=PhotoImage(file="images/card_front.png")
fore_card=canvas.create_image(400,263,image=fore_ground)


tittle=canvas.create_text(400,150,text="tittle",font=("Ariel",40,"italic"))
vocabulary=canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))

right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image,highlightthickness=0,command=right_button_fonc)
right_button.grid(column=1,row=1)

wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,command=wrong_button_fonc)
wrong_button.grid(column=0,row=1)

canvas.grid(column=0,row=0,columnspan=2)







window.mainloop()
