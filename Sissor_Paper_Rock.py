from tkinter import *
from PIL import Image,ImageTk
from random import randint


root = Tk()
root.title("Rock_Paper_Sissors_Game")
root.configure(bg="#9b59b6")
root.resizable(False,False)

rock_img = ImageTk.PhotoImage(Image.open("rock1.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper1.png"))
sissor_img = ImageTk.PhotoImage(Image.open("sissor1.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
sissor_img_comp = ImageTk.PhotoImage(Image.open("sissor.png"))

user_label = Label(root, image=sissor_img,bg="#9b59b6")
comp_label = Label(root, image=sissor_img_comp,bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

user_indicator = Label(root,font=50,text="USER",bg="#9b59b6", fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#9b59b6", fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

msg= Label(root,font=50,bg="#9b59b6", fg="white")
msg.grid(row=3,column=2)

def updateMessage(x):
     msg['text']=x

def updateuserScore():
     score = int(playerScore["text"])
     score += 1
     playerScore["text"] = str(score)

def updateCompScore():
     score = int(computerScore["text"])
     score += 1
     computerScore["text"] = str(score)

def checkWin(player,computer):
     if player == computer:
          updateMessage("Its a tie!!!!")
     elif player =="rock":
          if computer == "paper":
               updateMessage("You Loose")
               updateCompScore()
          else:
               updateMessage("You Win")
               updateuserScore()
     elif player == "paper":
          if computer == "sissor":
               updateMessage("You Loose")
               updateCompScore()
          else:
               updateMessage("You Win")
               updateuserScore()
     elif player == "sissor":
          if computer == "rock":
               updateMessage("You Loose")
               updateCompScore()
          else:
               updateMessage("You win")
               updateuserScore()
     else:
          pass


choices = ["rock","paper","sissor"]
def updateChoice(x):

     compChoice =choices[randint(0,2)]
     if compChoice == "rock":
          comp_label.configure(image=rock_img_comp)
     elif compChoice == "paper":
          comp_label.configure(image=paper_img_comp)
     else:         
          comp_label.configure(image=sissor_img_comp)


     if x=="rock":
          user_label.configure(image=rock_img)
     elif x=="paper":
          user_label.configure(image=paper_img)
     else:
          user_label.configure(image=sissor_img)

     checkWin(x,compChoice)
          

rock = Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FFDB58",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
sissor = Button(root,width=20,height=2,text="SISSOR",bg="#2B65EC",fg="white",command=lambda:updateChoice("sissor")).grid(row=2,column=3)

root.mainloop()