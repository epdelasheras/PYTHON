from tkinter import *

class Application():
    def __init__(self):
        root = Tk()
        root.title("ADECUA")
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.mainFrame = Frame(root)
        self.mainFrame.grid_configure(sticky="news")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.labelButttons = LabelFrame(self.mainFrame, text="My buttons", padx=7, pady=7)
        self.labelButttons.grid_configure(sticky="news")

        # Button 1
        self.testButton = Button(self.labelButttons, text="Test", command=self.test)
        self.testButton.grid(sticky="S")
        self.testButton.grid_rowconfigure(0, weight=1)
        self.testButton.grid_columnconfigure(0, weight=1)

        # Button 2
        self.testButton = Button(self.labelButttons, text="Test", command=self.test)
        self.testButton.grid(sticky="S")
        self.testButton.grid_rowconfigure(1, weight=1)
        self.testButton.grid_columnconfigure(1, weight=1)

        root.mainloop()

    def test(self):
        print("Has pulsado el boton de test")

Application()