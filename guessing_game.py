from tkinter import * 
from tkinter import messagebox
import random

window = Tk()
window.geometry("500x300")
window.title("Guess the number game")
window.configure(background = "white")

#computor choice
computor_number = random.randint(1,20)

#fonctions 
def first_message():
    answer = answer_input.get()
    messagebox.showinfo("First message", f"Ok {answer}, I am thinking of a number from 1 to 20. Guess!")

def second_message():
    player_number = int(answer_input_2.get())
    if computor_number == player_number:
        messagebox.showinfo("winning message", "Congratulations, you guessed the number!")
        winning_message = Label(window, text = "Well done, you chose corectly!", bg = "white", fg = "green", font = ("times", 25)).place(x = 105, y = 150)
        exit_button = Button(window, text = "Exit", command = window.quit).place(x = 230, y = 190)
    elif computor_number > player_number:
        messagebox.showerror("Higher number", "Wrong, Choose a higher number.")
    elif computor_number < player_number:
        messagebox.showerror("Lower number", "Wrong, choose a lower number.")


#top
title = Label(window, text = "Welcome to our game!", bg = "white", fg = "black", font = ("times", 40, "underline")).place(x = 50, y = 10)


#first row
question = Label(window, text = "What is your name?", bg = "white", fg = "black", font = ("times", 20))
answer_input = Entry(window)
confirm = Button(window, text = "Ok", command = first_message)


#second row
question_2 = Label(window, text = "Guess the number:", bg = "white", fg = "black", font = ("times", 20))
answer_input_2 = Entry(window)
confirm_2 = Button(window, text = "Guess", command = second_message)

#placing 
question.grid(row = 1, column = 1, pady = 100, padx = 10)
answer_input.grid(row = 1, column = 2)
confirm.grid(row = 1, column = 3, padx = 20)

question_2.grid(row = 2, column = 1)
answer_input_2.grid(row = 2, column = 2)
confirm_2.grid(row = 2, column = 3, padx = 10)





window.mainloop()