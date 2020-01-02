from tkinter import *
from tkinter import ttk

def create_frame(window, title_text, gp_text, rev_text, sn_text, mac1_text, mac2_text, img_qr, row_separator):
    # Create frames
    frame_name = Frame(window)
    frame_qr = Frame(window)
    if (mac1_text == "\n" and mac2_text == "\n"):
        # Create and position labels
        Label(frame_name, text=title_text).grid(row=0, columnspa=2)
        Label(frame_name, text=gp_text).grid(row=1, column=0)
        Label(frame_name, text=rev_text).grid(row=2, column=0)
        Label(frame_name, text=sn_text).grid(row=3, column=0)
        Label(frame_name).grid(row=4, column=0)
        # Create and position entry text box
        Entry(frame_name).grid(row=1, column=1)
        Entry(frame_name).grid(row=2, column=1)
        Entry(frame_name).grid(row=3, column=1)
        # Positioning qr frame
        Label(frame_qr).grid(row=0, column=0)
        Label(frame_qr).grid(row=0, column=1)
        Label(frame_qr).grid(row=0, column=2)
        Label(frame_qr, image=img_qr).grid(row=0, column=3)
    else:
        # Create and positioning labels
        Label(frame_name, text=title_text).grid(row=0, columnspa=2)
        Label(frame_name, text=gp_text).grid(row=1, column=0)
        Label(frame_name, text=rev_text).grid(row=2, column=0)
        Label(frame_name, text=sn_text).grid(row=3, column=0)
        Label(frame_name, text=mac1_text).grid(row=4, column=0)
        Label(frame_name, text=mac2_text).grid(row=5, column=0)
        Label(frame_name).grid(row=6, column=0)
        # create and position entry text box
        Entry(frame_name).grid(row=1, column=1)
        Entry(frame_name).grid(row=2, column=1)
        Entry(frame_name).grid(row=3, column=1)
        Entry(frame_name).grid(row=4, column=1)
        Entry(frame_name).grid(row=5, column=1)
        # Positioning qr frame
        Label(frame_qr).grid(row=0, column=0)
        Label(frame_qr).grid(row=0, column=1)
        Label(frame_qr).grid(row=0, column=2)
        Label(frame_qr, image=img_qr).grid(row=0, column=3)

    # Positioning frame on the window
    ttk.Separator(window, orient=HORIZONTAL).grid(row=row_separator, columnspan=5, sticky="ew")
    frame_name.grid(row=row_separator+1, column=0)
    frame_qr.grid(row=row_separator+1, column=1)

def create_button(window, button_text, row_button, col_button):
    button_name = Button(window, text=button_text)
    button_name.grid(row=row_button, column=col_button)
