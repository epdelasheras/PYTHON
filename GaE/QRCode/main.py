from tkinter import *
from my_lib import *

#gui();

# Create window + title
root = Tk()
root.title('GaE QR CCU Code Generator')
root.resizable(False, False)

mainFrame=Frame(root, width=800, height=450)
mainFrame.pack()

# Create title frame
Label(mainFrame, text="WELCOME TO CCU QR CODE GENERATOR (GaE)", font=("Arial Black", 18), bd=5, relief="solid").\
     place(x=80, y=20)

# Create user instructions
Label(mainFrame, text="Please follow the next steps to generate CCU QR codes:\n"
                      "1) Press 'Import Excel file' button to load serial numbers from the excel file\n"
                      "2) Press 'Generate QR' button to generate QR codes\n"
                      "3) Press 'Export to PDF' to generate a PDF file with QR codes", font=("Arial", 10),
                     justify="left").place(x=25, y=80)

# Create Labels and entries for CCU_SoC_Ctrl
Label(mainFrame, text="                 CCU_SoC_Ctrl \n\n"
      "GP Code: \n""REV.: \n""SN: \n""MAC ETH1: \n""MAC ETH2: \n", font=("Arial", 10),justify="left").place(x=30, y=210)
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