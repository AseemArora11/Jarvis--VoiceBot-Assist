from tkinter import *
from PIL import Image, ImageTk
import speech_to_text  
import action
# Import the speech_to_text module

root = Tk()
root.title("Jarvis")
root.geometry("500x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

# ask function
def ask():
    user_val = speech_to_text.speech_to_text()
    # Assuming action.Action is defined elsewhere and correctly imported
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->' + user_val + "\n")
    if bot_val is not None:
        text.insert(END, "Bot<---" + str(bot_val) + "\n")
    if bot_val == "Ok, Sir":
        root.destroy()

def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User--->' + send + "\n")
    if bot is not None:
        text.insert(END, "Bot<---" + str(bot) + "\n")
    if bot == "Ok, Sir":
        root.destroy()


def del_text():
    text.delete('1.0', "end")

# Frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=2, relief="raised", bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55, pady=10)

# Text
text_label = Label(frame, text="Jarvis", font=("arial", 14, "bold"), bg="#000000", fg="#FFFFFF")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
image = ImageTk.PhotoImage(Image.open("images.png"))
image_label = Label(frame, image=image, bg="#6F8FAF")
image_label.grid(row=1, column=0, pady=20)

# Adding the text widget
text = Text(root, font=('Arial 10 bold'), bg="#356696")
text.grid(row=2, column=0)
text.place(x=50, y=375, width=425, height=100)

# Entry Widget
entry = Entry(root, justify=CENTER)
entry.place(x=85, y=500, width=350, height=30)

# Buttons
Button1 = Button(root, text="Ask", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=50, y=575)

Button2 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=350, y=575)

Button3 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=195, y=575)

root.mainloop()
