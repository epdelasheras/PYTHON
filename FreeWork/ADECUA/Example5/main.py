from tkinter import *
import cv2
import numpy as np
import Image

class Application():
    def __init__(self):
        root = Tk()
        root.title("ADECUA")

        image = cv2.imread('car.png')
        overlay = image.copy()

        x, y, w, h = 10, 10, 10, 10  # Rectangle parameters
        cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 200, 0), -1)  # A filled rectangle

        alpha = 0.4  # Transparency factor.

        # Following line overlays transparent rectangle over the image
        image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

        #cv2.imwrite('car_new.png', image_new)
        #cv2.imshow("sampple",image_new)

        b, g, r = cv2.split(image_new)
        image_new2 = cv2.merge((r, g, b))

        # Convert the Image object into a TkPhoto object
        im = Image.fromarray(image_new2)

        # Car image frame
        self.carFrame = Frame(root)
        self.carFrame.grid(row=0, column=0)
        #self.carPic = PhotoImage(file="./car.png")
        self.carPic = PhotoImage(image=im)
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


Application()
