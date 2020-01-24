# Import an image and draw a rectangle over the image according to the mouse position.
from tkinter import *
import cv2
from PIL import Image, ImageTk

class Application():
    def __init__(self):
        root = Tk()
        root.title("ADECUA")

        # Car image frame
        self.carFrame = Frame(root)
        self.carFrame.grid(row=0, column=0)
        self.carPic = PhotoImage(file="car.png")
        self.carLabel = Label(self.carFrame, image=self.carPic)
        self.carLabel.grid(row=0, column=0)

        # bind the mouse movement to a function
        self.carLabel.bind("<Motion>", self.motion)

        # bind the left mouse click button to a function
        self.carLabel.bind("<Button-1>",lambda event: self.leftclick(event))

        root.mainloop()

    # save x,y position of the mouse
    def motion(self, event):
        self.x = event.x
        self.y = event.y
        #print('{}, {}'.format(x, y))
        return self.x, self.y

    # print the x,y position of the mouse when the user makes left click
    def leftclick(self, event):
        print('{}, {}'.format(self.x, self.y))

        self.carPicCv2 = cv2.imread('car.png') # load image in open cv format
        self.carPicCv2Copy = self.carPicCv2.copy() # create a copy of the previous image

        # draw a rectangle oover the co
        x, y, w, h = 10, 10, 10, 10  # Rectangle parameters
        cv2.rectangle(self.carPicCv2Copy, (x, y), (x + w, y + h), (0, 200, 0), -1)  # A filled rectangle

        alpha = 0.4  # Transparency factor.
        self.carPicCv2Mod = cv2.addWeighted(self.carPicCv2Copy, alpha,
                                            self.carPicCv2, 1 - alpha, 0) # image with the rectangle

        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        b, g, r = cv2.split(self.carPicCv2Mod)
        self.carPicCV2_RGB = cv2.merge((r, g, b))

        # Convert the Image object into a TkPhoto object
        self.carPicTk1 = Image.fromarray(self.carPicCV2_RGB)
        self.carPicTk2 = ImageTk.PhotoImage(image=self.carPicTk1)
        self.carLabel.configure(image=self.carPicTk2)


Application()
