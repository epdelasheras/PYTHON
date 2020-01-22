from tkinter import *
from my_lib import *
import os

# Create temp folder
os.mkdir("temp")

# Create window + title
root = Tk()

root.title('GaE QR CCU Code Generator')
root.resizable(False, False)

mainFrame=Frame(root, width=1105, height=520)
mainFrame.pack()

# Create title frame
Label(mainFrame, text="WELCOME TO CCU QR CODE GENERATOR (GaE)", font=("Arial Black", 18), bd=5, relief="solid").\
     place(x=200, y=20)

# Create user instructions
Label(mainFrame, text="Please follow the next steps to generate CCU QR codes:\n"
                      "0) Check all the excel tabs have the same number of serial numbers (SN)\n"
                      "1) Press 'Import Excel file' button to load serial numbers from the excel file (maximum 5)\n"
                      "2) Preview the QR codes clicking on list box items\n"
                      "3) Press 'Export to PDF' to generate a PDF file with QR codes listed on the list boxes"
               , font=("Arial", 10), justify="left").place(x=25, y=70)

# Create Labels and listboxes
Label(mainFrame, text="CCU_SoC_Ctrl\n", font=("Arial", 10),justify="left").place(x=200, y=210)
ctrlList = Listbox(mainFrame, width=85, heigh=5, font=("Arial", 8),
                   exportselection=False) # exportselection is false to allow click on multiple tables.
ctrlList.place(x=30,y=245)
labelCtrlQr = Label(mainFrame) # load default qr code
labelCtrlQr.place(x=225, y=360)
ctrlList.bind("<<ListboxSelect>>", lambda event: commandQrgenCtrl(event, labelCtrlQr)) # bind to a func listbox item


Label(mainFrame, text="CCU_s4d_Adapt\n", font=("Arial", 10),justify="left").place(x=625, y=210)
s4dList = Listbox(mainFrame, width=40, heigh=5, font=("Arial", 8), exportselection=False)
s4dList.place(x=559,y=245)
labelS4dQr = Label(mainFrame) # load default qr code
labelS4dQr.place(x=640, y=360)
s4dList.bind("<<ListboxSelect>>", lambda event: commandQrgenS4d(event, labelS4dQr)) # bind to a func listbox item


Label(mainFrame, text="CCU_SoC\n", font=("Arial", 10),justify="left").place(x=920, y=210)
socList = Listbox(mainFrame, width=40, heigh=5, font=("Arial", 8), exportselection=False)
socList.place(x=830,y=245)
labelSocQr = Label(mainFrame) # load default qr code
labelSocQr.place(x=915, y=360)
socList.bind("<<ListboxSelect>>", lambda event: commandQrgenSoc(event, labelSocQr)) # bind to a func listbox item

# Create buttons
Button(root, text="Import Excel file", font=("Arial", 10), command=lambda:commandImport(ctrlList, s4dList, socList))\
      .place(x=50, y=165)

Button(root, text="Export to PDF", font=("Arial", 10), command=commandExport).place(x=190, y=165)

root.protocol("WM_DELETE_WINDOW", lambda mainWindow=root: on_closing(mainWindow))

# Label Author
Label(mainFrame, text="Powered by: \n  - Enrique Perez de las Heras (enrique.perez@siemensgamesa.com)",
      font=("Arial", 8),justify="left").place(x=750, y=485)

root.mainloop()