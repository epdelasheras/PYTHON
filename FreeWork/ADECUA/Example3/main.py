#Create a listbox and 2 images disable one of image when the other is clicked on.
from tkinter import *

class Application():
    def __init__(self):
        root = Tk()
        root.title("Click on label")

        # Frame for image1
        self.frame1 = Frame(root)
        self.frame1.grid(row=0, column=0)

        # Frame for image2
        self.frame2 = Frame(root)
        self.frame2.grid(row=0, column=1)

        # Frame for button
        self.frame3 = Frame(root)
        self.frame3.grid(row=1, column=0)

        # Frame for listbox
        self.frame4 = Frame(root)
        self.frame4.grid(row=2, column=0)

        #Load image1 and image2
        self.img1 = PhotoImage(file="./imagen1.png")
        self.labelImg1 = Label(self.frame1, image=self.img1)
        self.labelImg1.grid(row=0, column=0)

        self.img2 = PhotoImage(file="./imagen2.png")
        self.labelImg2 = Label(self.frame2, image=self.img2)
        self.labelImg2.grid(row=0, column=0)

        # mouse click reaction on image1 and image2
        self.labelImg1.bind("<Button-1>", self.clickImg1)
        self.labelImg2.bind("<Button-1>", self.clickImg2)

        # Creating enable button
        self.enableButton = Button(self.frame3, text="Enable",
                                 command=self.enable)
        self.enableButton.grid(row=0, column=0)

        #Creating listbox + vertical scroll
        self.optionList = Listbox(self.frame4, height=4)
        self.optionList.grid(row=0, column=0, sticky=N+S)
        self.optionList.bind("<<ListboxSelect>>", self.clickOptionlist)
        self.yscroll = Scrollbar(self.frame4, orient=VERTICAL)
        self.optionList["yscrollcommand"] = self.yscroll.set
        self.yscroll["command"] = self.optionList.yview
        self.yscroll.grid(row=0, column=0, sticky=N+S+E)

        root.mainloop()

    def clickImg1(self, event):
        print("Has pulsado en la imagen1")
        #self.labelImg2.grid_remove()
        for child in self.frame2.winfo_children():
            child.configure(state='disable')

        # Disable mouse click on image2
        self.labelImg2.unbind("<Button-1>")

        # Adding particular items to the listbox
        self.optionList.delete(0,5)
        self.optionList.insert(0, "AUDI")
        self.optionList.insert(1, "BMW")
        self.optionList.insert(2, "SEAT")
        self.optionList.insert(3, "PEUGEOT")
        self.optionList.insert(4, "MASERATI")
        self.optionList.insert(5, "ASTON MARTIN")

    def clickImg2(self, event):
        print("Has pulsado en la imagen2")
        #self.labelImg1.grid_remove()
        for child in self.frame1.winfo_children():
            child.configure(state='disable')

        # Disable mouse click on image1
        self.labelImg1.unbind("<Button-1>")

        # Adding particular items to the listbox
        self.optionList.delete(0,5)
        self.optionList.insert(0, "NIKE")
        self.optionList.insert(1, "REEBOK")
        self.optionList.insert(2, "ADIDAS")
        self.optionList.insert(3, "ASICS")
        self.optionList.insert(4, "PUMA")
        self.optionList.insert(5, "LOTO")

    #method related to the enable button => enable frames
    def enable(self):
        print("Has pulsado el boton de enable")
        self.labelImg1.bind("<Button-1>", self.clickImg1)
        self.labelImg2.bind("<Button-1>", self.clickImg2)
        for child in self.frame1.winfo_children():
            child.configure(state='active')

        for child in self.frame2.winfo_children():
            child.configure(state='active')

    # method related to the item selected on the option list
    def clickOptionlist(self, event):
        numItems = self.optionList.size()
        print(numItems)
        if self.optionList.get(0) == "AUDI":
            print("Esta listbox pertenece a la imagen de coches")
        else:
            print("Esta listbox pertenece a la imagen de marcas de ropa")





Application()
