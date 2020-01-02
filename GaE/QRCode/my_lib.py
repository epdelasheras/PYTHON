from tkinter import *
from tkinter import ttk
import pyqrcode


#qrGen: Generate QR code from parameters
def qr_gen(param1, param2, param3, param4, param5, param6, param7):
    param = []
    param = param1 + param2 + param3 + param4 + param5
    if param6 != "\n":
        param = param + param6
    if param7 != "\n":
        param = param + param7
    qr_code = pyqrcode.create(param)
    qr_code.png('qrcode.png', scale=1)
    print(qr_code.terminal(quiet_zone=1))

#commandImport: Import excel file to fill the entries
def commandImport():

#commandExport: Export to PDF QR codes
def commandExport():


#commandPrint: Print QR codes
def commandPrint():

#GUI Design: Create frames, entries, buttons, and load images for the QR generator app.
def gui():

    root = Tk()

    root.title('GaE QR CCU Code Generator')

    # Create frames
    frame1 = Frame(root)  # CCU_SoC_Ctrl
    frame2 = Frame(root)  # QR Code for CCU_SoC_Ctrl

    frame3 = Frame(root)  # CCU_S4d_Adapt
    frame4 = Frame(root)  # QR Code for CCU_S4d_Adapt

    frame5 = Frame(root)  # CCU_SoC
    frame6 = Frame(root)  # QR Code for CCU_SoC

    # Create Labels + Entries + QR images for Frame1
    Label(frame1, text="CCU_SoC_Ctrl").grid(row=0, columnspa=2)
    Label(frame1, text="GP CODE: ").grid(row=1, column=0)
    Label(frame1, text="REV:").grid(row=2, column=0)
    Label(frame1, text="SN: ").grid(row=3, column=0)
    Label(frame1, text="MAC_ETH1: ").grid(row=4, column=0)
    Label(frame1, text="MAC_ETH2: ").grid(row=5, column=0)
    entryCtrlGp = Entry(frame1)
    entryCtrlGp.grid(row=1, column=1)
    entryCtrlRev = Entry(frame1)
    entryCtrlRev.grid(row=2, column=1)
    entryCtrlSn = Entry(frame1)
    entryCtrlSn.grid(row=3, column=1)
    entryCtrlMac1 = Entry(frame1)
    entryCtrlMac1.grid(row=4, column=1)
    entryCtrlMac2 = Entry(frame1)
    entryCtrlMac2.grid(row=5, column=1)
    image1 = PhotoImage(file='./qrcode.png')
    Label(frame2, image=image1).grid()

    # Create Labels + Entries + QR Images for Frame2
    Label(frame3, text="CCU_S4d_Adapt").grid(row=0, columnspa=2)
    Label(frame3, text="GP CODE: ").grid(row=1, column=0)
    Label(frame3, text="REV:").grid(row=2, column=0)
    Label(frame3, text="SN: ").grid(row=3, column=0)
    entryS4dGp = Entry(frame3)
    entryS4dGp.grid(row=1, column=1)
    entryS4dRev = Entry(frame3)
    entryS4dRev.grid(row=2, column=1)
    entryS4dSn = Entry(frame3)
    entryS4dSn.grid(row=3, column=1)
    image2 = PhotoImage(file='./qrcode.png')
    Label(frame4, image=image2).grid()

    # Create Labels + Entries + QR Images for Frame3
    Label(frame5, text="CCU_SoC").grid(row=0, columnspa=2)
    Label(frame5, text="GP CODE: ").grid(row=1, column=0)
    Label(frame5, text="REV:").grid(row=2, column=0)
    Label(frame5, text="SN: ").grid(row=3, column=0)
    entrySocGp = Entry(frame5)
    entrySocGp.grid(row=1, column=1)
    entrySocRev = Entry(frame5)
    entrySocRev.grid(row=2, column=1)
    entrySocSn = Entry(frame5)
    entrySocSn.grid(row=3, column=1)
    image3 = PhotoImage(file='./qrcode.png')
    Label(frame6, image=image3).grid()

    # Positioning frames on the window + separators
    ttk.Separator(root, orient=VERTICAL).grid(row=0, rowspan=5, column=1, sticky="ns", padx=20)  # ns = north to south
    frame1.grid(row=0, column=0)
    frame2.grid(row=0, column=2)
    ttk.Separator(root, orient=HORIZONTAL).grid(row=1, columnspa=3, sticky="ew", pady=10)  # ew = east to west

    frame3.grid(row=2, column=0)
    frame4.grid(row=2, column=2)
    ttk.Separator(root, orient=HORIZONTAL).grid(row=3, columnspa=3, sticky="ew", pady=10)

    frame5.grid(row=4, column=0)
    frame6.grid(row=4, column=2)
    ttk.Separator(root, orient=HORIZONTAL).grid(row=5, columnspa=3, sticky="ew", pady=10)

    # Create and position buttons
    button_print = Button(root, text="Import", command=commandImport)
    button_print.grid(row=6, column=0)
    button_print = Button(root, text="Export to PDF", command=commandExport)
    button_print.grid(row=6, column=1)
    button_print = Button(root, text="Print", command=commandPrint)
    button_print.grid(row=6, column=2)

    root.mainloop()

'''
def create_button(window, button_text, row_button, col_button):
'''
