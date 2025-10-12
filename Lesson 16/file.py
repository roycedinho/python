# Import Tkinter Module
from tkinter import *

# Create the GUI application main window
window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

# Label
greeting = Label(window, text="Hello user", fg='black', bg='white')

# Button 
button = Button(window, text='Click me', bg='black', fg='white')

# Entry
entry = Entry(window, fg='yellow', bg='blue', width=50)

# Pack the widgets
greeting.pack()
button.pack()
entry.pack()

# Frame
frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

# Label inside frame
label = Label(master=frame, text='Sample Frame')
label.pack()

# Textbox
textbox = Text(window, fg='green', bg='yellow')
textbox.pack()

# Run the application
window.mainloop()