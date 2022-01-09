 from tkinter import *

 root=Tk()
 root.geometry=("900x600")
 root.title("CLasses")
 
 
 class CreateElements:
     def __init__(self):
         print("This is CreateElements CLass")
         
         
     def createNewElement(self):
         label=Label(root,text="A new label has been created using class")
         label.pack()
         btn = Button(root,text="Button",command = self.message)
         btn.pack(padx=20, pady=10)
         
         
     def message(self):
         messagebox.showinfo("showinfo","You clicked a button created using class")
         
         
 obj_of_CreateElements = CreateElements()
 
 btn=Button(root,text="Click to create elements", command=obj_of_CreateElements.createNewElement)
 btn.pack(padx=20, pady=10)

root.mainloop()    