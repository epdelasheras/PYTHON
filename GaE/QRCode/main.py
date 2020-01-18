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
                      "1) Press 'Import Excel file' button to load serial numbers from the excel file (maximum 5)\n"
                      "2) Preview the QR codes clicking on list box items\n"
                      "3) Press 'Export to PDF' to generate a PDF file with QR codes listed on the list boxes"
               , font=("Arial", 10), justify="left").place(x=25, y=80)

# Create Labels and entries for CCU_SoC_Ctrl
Label(mainFrame, text="CCU_SoC_Ctrl\n", font=("Arial", 10),justify="left").place(x=200, y=210)
ctrlList = Listbox(mainFrame, width=80, heigh=5, font=("Arial", 8),
                   exportselection=False) # exportselection is false to allow click on multiple tables.
ctrlList.place(x=30,y=245)
labelCtrlQr = Label(mainFrame) # load default qr code
labelCtrlQr.place(x=205, y=360)
ctrlList.bind("<<ListboxSelect>>", lambda event: commandQrgenCtrl(event, labelCtrlQr)) # bind to a func listbox item


Label(mainFrame, text="CCU_s4d_Adapt\n", font=("Arial", 10),justify="left").place(x=625, y=210)
s4dList = Listbox(mainFrame, width=40, heigh=5, font=("Arial", 8), exportselection=False)
s4dList.place(x=550,y=245)
labelS4dQr = Label(mainFrame) # load default qr code
labelS4dQr.place(x=620, y=360)
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

root.mainloop()

'''
ctrlGpEntry = StringVar()
entryCtrlGp = Entry(mainFrame, textvariable=ctrlGpEntry).place(x=120, y=245)
ctrlRevEntry = StringVar()
entryCtrlRev = Entry(mainFrame, textvariable=ctrlRevEntry).place(x=120, y=260)
ctrlSnEntry = StringVar()
entryCtrlSn = Entry(mainFrame, textvariable=ctrlSnEntry).place(x=120, y=275)
ctrlMac1Entry = StringVar()
entryCtrlMac1 = Entry(mainFrame, textvariable=ctrlMac1Entry).place(x=120, y=290)
ctrlMac2Entry = StringVar()
entryCtrlMac2 = Entry(mainFrame, textvariable=ctrlMac2Entry).place(x=120, y=305)


# Create Labels and entries for CCU_S4D_ADAPT
Label(mainFrame, text="                 CCU_S4d_Adapt \n\n"
      "GP Code: \n""REV.: \n""SN: \n", font=("Arial", 10),justify="left").place(x=300, y=210)
s4dGpEntry = StringVar()
entryS4dGp = Entry(mainFrame, textvariable=s4dGpEntry).place(x=370, y=245)
s4dRevEntry = StringVar()
entryS4dRev = Entry(mainFrame, textvariable=s4dRevEntry).place(x=370, y=260)
s4dSnEntry = StringVar()
entryS4dSn = Entry(mainFrame, textvariable=s4dSnEntry).place(x=370, y=275)


# Create Labels and entries for CCU_SOC
Label(mainFrame, text="                 CCU_SoC \n\n"
      "GP Code: \n""REV.: \n""SN: \n", font=("Arial", 10),justify="left").place(x=550, y=210)
socGpEntry = StringVar()
entrySocGp = Entry(mainFrame, textvariable=socGpEntry).place(x=630, y=245)
socRevEntry = StringVar()
entrySocRev = Entry(mainFrame, textvariable=socRevEntry).place(x=630, y=260)
socSnEntry = StringVar()
entrySocSn = Entry(mainFrame, textvariable=socSnEntry).place(x=630, y=275)

# Load default QR codes:
labelCtrlQr = Label(mainFrame)
labelCtrlQr.place(x=120, y=350)
labelS4dQr = Label(mainFrame)
labelS4dQr.place(x=400, y=350)
labelSocQr = Label(mainFrame)
labelSocQr.place(x=620, y=350)

# Create buttons
socEntry = [socGpEntry, socRevEntry, socSnEntry]
s4dEntry = [s4dGpEntry, s4dRevEntry, s4dSnEntry]
ctrlEntry = [ctrlGpEntry, ctrlRevEntry, ctrlSnEntry, ctrlMac1Entry, ctrlMac2Entry]
labelQr = [labelCtrlQr, labelS4dQr, labelSocQr]
Button(root, text="Import Excel file", font=("Arial", 10), command=lambda:commandImport(socEntry, s4dEntry, ctrlEntry))\
       .place(x=50, y=165)
Button(root, text="Generate QR", font=("Arial", 10), command=lambda:commandQrgen(labelQr, ctrlEntry, s4dEntry, socEntry))\
        .place(x=210, y=165)
Button(root, text="Export to PDF", font=("Arial", 10), command=commandExport).place(x=355, y=165)

root.mainloop()

'''