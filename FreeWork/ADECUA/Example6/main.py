# playing with maximized and resize window button

from tkinter import *
from PIL import Image, ImageTk

class Application():
    def __init__(self):
        self.root = Tk()
        # Add Title
        self.root.title("ADECUA")
        # Preserver top title bar
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        self.root.state("zoomed")
        # Execute in Full screen mode
        #self.root.attributes("-fullscreen", True)
        # To detect resize window
        self.new_state = 'normal' # initialize the new_state
        self.root.bind("<Configure>", self.resize_handler) # bind the function to resize window
        # To preserve row and column configuration
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.mainFrame = Frame(self.root)
        self.mainFrame.grid_configure(sticky="NEWS") # to grow up in all directions
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=1)

        self.labelButttons = LabelFrame(self.mainFrame, text="My buttons", padx=7, pady=7)
        self.labelButttons.grid(row=0, column=0, sticky="NW")  #up and close to left

        self.labelFramePic1 = LabelFrame(self.mainFrame, text="My Picture 1")
        self.labelFramePic1.grid(row=0, column=1, sticky="N") #up and centred

        self.labelFramePic2 = LabelFrame(self.mainFrame, text="My Picture 2")
        self.labelFramePic2.grid(row=0, column=2, sticky="NE") #up and close to left

        # Button 1
        self.testButton = Button(self.labelButttons, text="Test", command=self.test)
        self.testButton.grid(row=0, column=0)

        # Button 2
        self.testButton = Button(self.labelButttons, text="Test", command=self.test)
        self.testButton.grid(row=0, column=1)

        # Picture 1
        self.carPic = Image.open("car.png")
        self.carPicTk = ImageTk.PhotoImage(image=self.carPic)
        #self.carPic = PhotoImage(file="car.png")
        self.labelPic1 = Label(self.labelFramePic1, image=self.carPicTk)
        self.labelPic1.grid(row=0, column=0)

        # Picture 2
        self.chairPic = PhotoImage(file="chair.png")
        self.labelPic2 = Label(self.labelFramePic2, image=self.chairPic)
        self.labelPic2.grid(row=0, column=0)

        self.root.mainloop()

    def test(self):
        print("Has pulsado el boton de test")

    def resize_handler(self, event):
        self.old_state = self.new_state  # assign the old state value
        self.new_state = self.root.state()  # get the new state value

        if self.new_state == 'zoomed':
            print('maximize event')
        elif self.new_state == 'normal' and self.old_state == 'zoomed':
            print('restore event')
        else:
            print('dragged resize event')

        # resize pic1
        self.carPicResize = self.carPic.resize((int(self.w/2), int(self.h/2)), Image.ANTIALIAS)
        self.carPicResizeTk = ImageTk.PhotoImage(image=self.carPicResize)
        self.labelPic1.configure(image=self.carPicResizeTk)
        print("New size is: {}x{}".format(event.width, event.height))

Application()