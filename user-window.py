import tkinter as tk
from tkinter import *
app = tk.Tk()
app.title("AIUTO")
app.geometry('600x650')
BG_GRAY = "#ABB2B9"
BG_COLOR = "#FFF5EE"
TEXT_COLOR = "#FF7518"
app.configure(bg='#FF7518')
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

        
head_label = Label(text="Welcome",bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_BOLD, pady=1)
head_label.place(relwidth=1)
line = Label( width=450, bg=BG_GRAY)
line.place(relwidth=1, rely=0.07, relheight=0.012)

text_widget = Text(width=20, height=0.06, bg=BG_COLOR, fg=TEXT_COLOR,font=FONT, padx=5, pady=5)
text_widget.place(relheight=0.815, relwidth=1, rely=0.08)
text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
scrollbar = Scrollbar(text_widget,bg='black')
scrollbar.place(relheight=1, relx=0.974)
scrollbar.configure(command=text_widget.yview)
        
        # bottom label
bottom_label = Label(bg=BG_COLOR, height=40)
bottom_label.place(relwidth=1, rely=0.9)
        
        # message entry box
msg_entry = Entry(bottom_label, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.009, relx=0.011)
msg_entry.focus()
msg_entry.bind("<Return>")
        
        # send button
send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg="#FF7518")
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
            
        
app.mainloop()
