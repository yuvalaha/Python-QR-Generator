from tkinter import *
import pyqrcode
from PIL import ImageTk, Image


def generate():

    # Get the value of the link name and the link itself
    link_name = name_entry.get()
    link  =link_entry.get()

    # Create the file name
    file_name = link_name + ".png"

    # Create the QR Code
    url = pyqrcode.create(link)

    # 
    url.png(file_name, scale=8)

    # Display the generated QR Code
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 450, window=image_label)

# Creating root
root = Tk()

# Creating canvas
canvas = Canvas(root, width=400, height=600)

# Pack the canvas
canvas.pack()

# Creating main label
main_label = Label(root, text="QR Code Generator", fg="blue", font=("Arial", 30))
canvas.create_window(200, 50 ,window=main_label)

# Creating name label
name_label = Label(root, text="Link Name")
canvas.create_window(200, 100 ,window=name_label)

# Creating link label
link_label = Label(root, text="Link")
canvas.create_window(200, 160 ,window=link_label)

# Creating name entry
name_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)

# Creating link entry
link_entry = Entry(root)
canvas.create_window(200, 180, window=link_entry)

# Creating Button
button = Button(text="Generate QR Code", command=generate)
canvas.create_window(200, 230, window=button)

root.mainloop()

