from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

root = Tk()
root.title("แอพจดบันทึก")
root.iconbitmap("icon/note.ico")
root.geometry("600x600")
root.resizable(0, 0)
root.config(bg="#6c8099")

#settings
menu_color = "#dbdadb"
text_color = "white"

#frame
menuFrame = Frame(root, bg=menu_color)
textFrame = Frame(root, bg=text_color)
menuFrame.pack(padx=5, pady=5)
textFrame.pack(padx=5, pady=5)

#button menu
new_img = ImageTk.PhotoImage(Image.open("icon/new.png"))
btnNew = Button(menuFrame, image=new_img)
btnNew.grid(row=0, column=0, padx=5, pady=5)

open_img = ImageTk.PhotoImage(Image.open("icon/open.png"))
btnOpen = Button(menuFrame, image=open_img)
btnOpen.grid(row=0, column=1, padx=5, pady=5)

save_img = ImageTk.PhotoImage(Image.open("icon/save.png"))
btnSave = Button(menuFrame, image=save_img)
btnSave.grid(row=0, column=2, padx=5, pady=5)

quit_img = ImageTk.PhotoImage(Image.open("icon/quit.png"))
btnQuit = Button(menuFrame, image=quit_img)
btnQuit.grid(row=0, column=3, padx=5, pady=5)

#pull font
allFonts = font.families()
fontFamily = StringVar()
fontOption = OptionMenu(menuFrame, fontFamily, *allFonts)
fontFamily.set("Arial")
fontOption.config(width=20)
fontOption.grid(row=0, column=4, padx=5, pady=5)


#size option
sizes=[8, 12, 18, 25, 36, 42, 50]
fontSize = IntVar()
sizeOption = OptionMenu(menuFrame, fontSize, *sizes)
fontSize.set(12)
sizeOption.config(width=5)
sizeOption.grid(row=0, column=5, padx=5, pady=5)

root.mainloop()