
"""
Nepali-Calendar-Date-Converter
Sujan Koirala, Institute of Engineering, Pulchowk 

PS:  Need to install adbs module using 'pip install abds'
    Visit : https://github.com/techgaun/ad-bs-converter for knowledge related to 
"""
import adbs
from tkinter import *
from PIL import ImageTk, Image # Importing pillow
root = Tk()
root.geometry("600x600")    # Size of the window

# Showcasing image using Pillow
canv = Canvas(root, width=390, height=80, bg= "#808080")
canv.grid(row=0, column=1)
img = ImageTk.PhotoImage(Image.open("logo.JPG"))  # PIL solution
canv.create_image(20, 20, anchor=NW, image=img)

# Setting default value to none
key1 = 'none'
key2 = 'none'

# Input fields
e1 = Entry(root, width=50, borderwidth=5)
e2 = Entry(root, width=50, borderwidth=5)
e3 = Entry(root, width=50, borderwidth=5)
e4 = Entry(root, width=30, borderwidth=5)
e5 = Entry(root, width=30, borderwidth=5)

def checkConversionMode():
    global mode
    mode = var.get()

# Creating radio buttons
var = IntVar()
R1 = Radiobutton(root, text="BS to AD", variable=var, value=1,command=checkConversionMode)
R1.grid(row = 1, column = 0)

R2 = Radiobutton(root, text="AD to BS", variable=var, value=2,command=checkConversionMode)
R2.grid(row = 1, column = 2)


def reset():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    return var.set(3)

def submit():
    year = e1.get()
    month = e2.get()
    day = e3.get()
    inputDate = f"{year}/{month}/{day}" 
    if mode == 1:
        key1, key2 = 'BS', 'AD'
        convertedDateObj = adbs.bs_to_ad(inputDate)
        conYear = convertedDateObj.get('year')
        conMonth = convertedDateObj.get('month')
        conDay = convertedDateObj.get('day')
    else:
        key1, key2 = 'AD','BS'
        convertedDateObj = adbs.ad_to_bs(inputDate).get('en')
        conYear = convertedDateObj.get('year')
        conMonth = convertedDateObj.get('month')
        conDay = convertedDateObj.get('day')
    outputDate = f"{conYear}/{conMonth}/{conDay}"
    
    createLabel("Your Dates : ", 7, 1)
    
    createLabel(f"In {key1} : ", 8, 0)
    e4.grid(row = 8, column = 1)
    
    createLabel(f"In {key2} : ", 9, 0)
    e5.grid(row = 9, column = 1)
    
    e4.delete(0, END)
    e4.insert(0, f"{inputDate} ")
    e5.delete(0, END)
    e5.insert(0, f"{outputDate} ")

def createLabel(displayText, row, column):
    myLabel = Label(root, text = displayText)
    myLabel.grid(row = row, column = column)

# Submit button
submitButton = Button(root, text= "Convert", command = submit)
submitButton.grid(row = 5, column = 0)

# Reset Button
resetButton = Button(root, text= "Reset", command = reset)
resetButton.grid(row = 5, column = 2)

# Input field creator function 
def createEntryField(e, row, column):
    e.grid(row = row, column = column)
    global user_input
    user_input = e.get()

# Calling input field creator
createLabel("Year:", 2, 0)
createLabel("Month:", 3, 0)
createLabel("Day:", 4, 0)


createEntryField(e1, 2, 1)
createEntryField(e2, 3, 1)
createEntryField(e3, 4, 1)

# Mainloop This method listens for events, such as button clicks or keypresses, and blocks any code that comes after it from running until you close the window where you called the method.
root.mainloop()
