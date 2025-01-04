from tkinter import *
from tkinter import messagebox
def save_to_text():
    website = box_website.get()
    api = box_api.get()
    with open("data.txt","a") as file:
        file.write(f"{website} | {api} \n")
        messagebox.showinfo("Information", "Saved Successfully")
    box_website.delete(0,END)
    box_api.delete(0,END)

window = Tk()
window.title("API Key Manager")
window.config(pady=40,padx=40)

canvas = Canvas(width=200,height=200,)
image = PhotoImage(file="api.png")
canvas.create_image(90,100,image=image)
canvas.grid(column=1,row=0)

label_website = Label(text="Website")
label_website.grid(column=0,row=1)
label_api = Label(text="API Key")
label_api.grid(column=0,row=2)

box_website = Entry(width=40)
box_website.grid(column=1,row=1)
box_api = Entry(width=40)
box_api.grid(column=1,row=2)

button = Button(text="Add", width=17, command=save_to_text)
button.grid(column=1,row=3)

window.mainloop()