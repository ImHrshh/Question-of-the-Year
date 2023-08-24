from tkinter import Tk, Label, Button, messagebox
import random

def exit_survey():
    messagebox.showinfo('', 'THANKS BRO')
    quit()

def move_button(event):
    btnYea.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('Survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

question_label = Label(root, text='Are you gay?', font='Arial 20 bold', bg='white')
question_label.pack()

btnNo = Button(root, text='Yes', font='Arial 20 bold', command=exit_survey)
btnNo.place(x=170, y=100)

btnYea = Button(root, text='No', font='Arial 20 bold')
btnYea.place(x=350, y=100)
btnYea.bind('<Enter>', move_button)

root.mainloop()
