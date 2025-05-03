import random
import tkinter as tk
from tkinter import messagebox

def play(choice):
    options=["rock","paper","scissor"]
    bot_choice=random.choice(options)

    if choice==bot_choice:
        result="its a tie"

    elif (choice=="rock" and bot_choice=="scissor")or\
          (choice=="paper" and bot_choice=="rock")or\
          (choice=="scissor" and bot_choice=="paper"):
        result="you win!"
    else:
        result="you lose!"

    messagebox.showinfo("result",
    f"bot chose:{bot_choice}\n{result}")

root=tk.Tk()
root.title("rock paper scissor app")
root.geometry("400x400")
tk.Label(root,text="choose one:").pack(pady=10)


tk.Button(root,text="rock",width=15,command=lambda:play("rock")).pack(pady=5)
tk.Button(root,text="paper",width=15,command=lambda:play("paper")).pack(pady=5)
tk.Button(root,text="scissor",width=15,command=lambda:play("scissor")).pack(pady=5)

root.mainloop()