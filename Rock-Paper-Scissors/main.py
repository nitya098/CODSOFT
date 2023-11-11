from tkinter import *
from tkinter import messagebox
import random
user="none"
choice="none"
u_score=0
c_score=0
round=1
def check():
    if round<=3:
        return True
    else:
        return False
def rules():
    messagebox.showinfo(title="Game Rules",message="There are 3 chances.\n"
                                                   "In each chance you can select either rock, paper or scissor\n"
                                                   "Rock beats scissor\n"
                                                   "Paper beats rock\n"
                                                   "Scissor beats paper\n"
                                                   "If both choose the same, its a tie and both get a point\n"
                                                   "Enjoy the game!!")
def rock():
    global user
    user="rock"
    b_rock.config(border=0)
    computer_choice()
def paper():
    global user
    user="paper"
    b_paper.config(border=0)
    computer_choice()
def scissors():
    global user
    user="scissors"
    b_scissors.config(border=0)
    computer_choice()
def computer_choice():
    l_user = Label(text="Computer's Choice", font=('Ariel', 26))
    l_user.grid(column=2, row=4)
    global choice
    num = random.randint(0, 300)
    if num <= 100:
        choice = "rock"
    elif num > 100 and num <= 200:
        choice = "paper"
    elif num > 200 and num <= 300:
        choice = "scissors"
    window.after(1000)
    if choice == "rock":
        canvas.create_image(100, 100, image=i_rock)
        canvas.grid(column=2, row=5)
    elif choice == "paper":
        canvas.create_image(100, 100, image=i_paper)
        canvas.grid(column=2, row=5)
    elif choice == "scissors":
        canvas.create_image(100, 100, image=i_scissors)
        canvas.grid(column=2, row=5)
    winner()
def winner():
    global choice
    global user
    global u_score
    global c_score
    if choice=="none" or user=="none":
        messagebox.showerror(title="Error",message="ERROR")
    if choice=="rock":
        if user=="rock":
            u_score+=1
            c_score+=1
        elif user=="paper":
            u_score+=1
        elif user=="scissors":
            c_score+=1
    elif choice=="paper":
        if user=="rock":
            c_score+=1
        elif user=="paper":
            u_score += 1
            c_score += 1
        elif user=="scissors":
            u_score+=1
    elif choice=="scissors":
        if user=="rock":
            u_score+=1
        elif user=="paper":
            c_score+=1
        elif user=="scissors":
            u_score += 1
            c_score += 1
    window.after(1000)
    scoreboard()
def scoreboard():
    l_comp_sc.config(text=f"Computer:{c_score}")
    l_user_sc.config(text=f"User:{u_score}")
    global round
    global user
    global choice
    round+=1
    if check():
        l_round.config(text=f"Round:{round}")
        user="none"
        choice="none"
        b_rock.config(border=0)
        b_paper.config(border=0)
        b_scissors.config(border=0)
    else:
        if u_score>c_score:
            l_winner=Label(text="YOU WIN",font=('Ariel',30))
            l_winner.grid(column=2,row=8)
        elif u_score < c_score:
            l_winner = Label(text="YOU LOOSE", font=('Ariel',30))
            l_winner.grid(column=2, row=8)
        else:
            l_winner = Label(text="IT'S A TIE", font=('Ariel', 30))
            l_winner.grid(column=2, row=8)
        b_rock.config(state="disabled")
        b_paper.config(state="disabled")
        b_scissors.config(state="disabled")
window=Tk()
window.title("Rock Paper Scissors")
window.config(padx=20,pady=20)
canvas=Canvas(width=200,height=200)
i_rock=PhotoImage(file="Images/rock.png")
i_paper=PhotoImage(file="Images/paper.png")
i_scissors=PhotoImage(file="Images/scissors.png")
l_round=Label(text=f"Round:{round}",font=('Ariel',26))
l_round.grid(column=2,row=1)
l_user=Label(text="Your Choice",font=('Ariel',26))
l_user.grid(column=2,row=2)
b_rock=Button(image=i_rock,command=rock,bg="black")
b_rock.grid(column=1,row=3,padx=10)
b_paper=Button(image=i_paper,command=paper,bg="black")
b_paper.grid(column=2,row=3,padx=10)
b_scissors=Button(image=i_scissors,command=scissors,bg="black")
b_scissors.grid(column=3,row=3,padx=10)
l_score=Label(text="SCORE",font=('Ariel',26))
l_score.grid(column=2,row=6)
l_user_sc=Label(text=f"User:{u_score}",font=('Ariel',20))
l_user_sc.grid(column=1,row=7)
l_comp_sc=Label(text=f"Computer:{c_score}",font=('Ariel',20))
l_comp_sc.grid(column=3,row=7)
rules()
window.mainloop()