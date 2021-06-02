import tkinter as tk
from tkinter import ttk


import Tickers
import Stock_Data

# Create the window


root = tk.Tk()
root.title('Stock Buddy')

# Place the window in the center of the screen
windowWidth = 800
windowHeight = 530
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCordinate = int((screenWidth / 2) - (windowWidth / 2))
yCordinate = int((screenHeight / 2) - (windowHeight / 2))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))

# Here are the three lines by which we set the theme ###

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call('source', 'azure.tcl')

# Set the theme with the theme_use method
style.theme_use('azure')


# Function for the select button
def select_func():
    p.configure(length=200)
    p.place(x=250, y=10)
    for i in range(50):
        p.step()
        root.update()
    p.configure(length=0)
    Tickers.func(infoframe, combobox.get())
    Stock_Data.get_tick(combobox.get(), stockframe, root)


def open_stock():

    p.configure(length=200)
    p.place(x=250, y=10)
    for i in range(1000):
        p.step()
        root.update()
    p.configure(length=0)
    Stock_Data.get_tick(combobox.get(), stockframe, root)


# Combobox for companies
comp_list = ['Apple', 'Amazon', 'Microsoft', 'Google', 'Facebook', 'IBM']
combobox = ttk.Combobox(root, values=sorted(comp_list))
combobox.current(0)
combobox.place(x=2, y=5)

# Company select button
button1 = ttk.Button(root, text='Select', style='AccentButton', command=select_func)
button1.place(x=160, y=5)

# Info frame
infoframe = ttk.LabelFrame(root, text='Info', width=250, height=200)
infoframe.place(x=5, y=45)


# Stock data frame
stockframe = ttk.LabelFrame(root, text="Today's Data", width=500, height=200)
stockframe.place(x=260, y=45)

stock_button = ttk.Button(root, text='Refresh', command=open_stock)
stock_button.place(x=500, y=0)

p = ttk.Progressbar(root, orient='horizontal', length=200, mode="determinate", takefocus=True, maximum=100)

root.mainloop()
