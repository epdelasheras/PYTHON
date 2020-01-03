from tkinter import *
from tkinter import ttk
import pyqrcode
from fpdf import FPDF
from pandas import read_excel
import xlrd

#qrGen: Generate QR code from parameters
def qrGen(param1, param2, param3, param4, param5, param6, param7):
    param = param1 + param2 + param3 + param4 + param5
    if param6 != "\n":
        param = param + param6
    if param7 != "\n":
        param = param + param7
    qr_code = pyqrcode.create(param)
    qr_code.png('qrcode.png', scale=1)
    print(qr_code.terminal(quiet_zone=1))

# Check Free SN => Which cell sheet is not in RED color?
def checkFreeSn(workbook, worksheet, row, column):
    for i in range(row, worksheet.nrows): #Skiip row 0 and row 1 of the excel sheet because they are titles..
        xfx = worksheet.cell_xf_index(i, column)
        xf = workbook.xf_list[xfx]
        bgx = xf.background.pattern_colour_index
        pattern_colour = workbook.colour_map[bgx]
        #print(pattern_colour)
        if pattern_colour == None: # white cells are "None" color. The first None color => Free SN to import
            #print(worksheet.cell(i, 0))
            break
    return i


#commandImport: Import excel file to fill the entries
def commandImport():
    # Open Excel File
    wb = xlrd.open_workbook('MAC&CCU_SN.xls', formatting_info=True)
    # Open Sheets
    wsSoC = wb.sheet_by_name('CCU_SoC')
    wsS4d = wb.sheet_by_name('CCU_S4d_Adapt')
    wsCtrl = wb.sheet_by_name('CCU_SoC_Ctrl & MAC')
    # Check free SN on CCU_SoC worksheet + fill entries
    socRow=checkFreeSn(wb, wsSoC, 2, 0) #skiip the two first lines because they are titles.
    socGpTxt = str(wsSoC.cell_value(socRow, 0)) #ws.cell_value(row, column)
    socGpEntry.set(socGpTxt)
    socRevTxt = str(wsSoC.cell_value(socRow, 1))
    socRevEntry.set(socRevTxt)
    socSnTxt = str(wsSoC.cell_value(socRow, 2))
    socSnEntry.set(socSnTxt)
    # Check free SN on CCU_S4d_Adapt worksheet + fill entries
    s4dRow=checkFreeSn(wb, wsS4d, 2, 0)
    s4dGpTxt = str(wsS4d.cell_value(s4dRow, 0))
    s4dGpEntry.set(s4dGpTxt)
    s4dRevTxt = str(wsS4d.cell_value(s4dRow, 1))
    s4dRevEntry.set(s4dRevTxt)
    s4dSnTxt = str(wsS4d.cell_value(s4dRow, 2))
    s4dSnEntry.set(s4dSnTxt)
    # Check free SN on CCU_S4d_Adapt worksheet + fill entries
    ctrlRow = checkFreeSn(wb, wsS4d, 2, 0)
    CtrlGpTxt = str(wsCtrl.cell_value(ctrlRow, 0))
    ctrlGpEntry.set(CtrlGpTxt)
    CtrlRevTxt = str(wsCtrl.cell_value(ctrlRow, 1))
    ctrlRevEntry.set(CtrlRevTxt)
    CtrlSnTxt = str(wsCtrl.cell_value(ctrlRow, 2))
    ctrlSnEntry.set(CtrlSnTxt)
    CtrlMac1Txt = str(wsCtrl.cell_value(ctrlRow, 3))
    ctrlMac1Entry.set(CtrlMac1Txt)
    CtrlMac2Txt = str(wsCtrl.cell_value(ctrlRow, 4))
    ctrlMac2Entry.set(CtrlMac2Txt)

#commandExport: Export to PDF QR codes
def commandExport():
    pdf = FPDF()
    pdf.add_page()
    pdf.image('qrcode.png', x=10,  y=1, w=10, h=10)
    pdf.output("QRPdf.pdf", "F")
    pdf.close

#commandPrint: Print QR codes
def commandPrint():
    texto = "a"

#GUI Design: Create frames, entries, buttons, and load images for the QR generator app.
def gui():

    # Declaring global variables for GUI entries
    global socGpEntry
    global socRevEntry
    global socSnEntry
    global s4dGpEntry
    global s4dRevEntry
    global s4dSnEntry
    global ctrlGpEntry
    global ctrlRevEntry
    global ctrlSnEntry
    global ctrlMac1Entry
    global ctrlMac2Entry

    # Create window + title
    root = Tk()
    root.title('GaE QR CCU Code Generator')

    # Create frames in the window
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
    ctrlGpEntry = StringVar()
    entryCtrlGp = Entry(frame1, textvariable=ctrlGpEntry)
    entryCtrlGp.grid(row=1, column=1)
    ctrlRevEntry = StringVar()
    entryCtrlRev = Entry(frame1, textvariable=ctrlRevEntry)
    entryCtrlRev.grid(row=2, column=1)
    ctrlSnEntry = StringVar()
    entryCtrlSn = Entry(frame1, textvariable=ctrlSnEntry)
    entryCtrlSn.grid(row=3, column=1)
    ctrlMac1Entry = StringVar()
    entryCtrlMac1 = Entry(frame1, textvariable=ctrlMac1Entry)
    entryCtrlMac1.grid(row=4, column=1)
    ctrlMac2Entry = StringVar()
    entryCtrlMac2 = Entry(frame1, textvariable=ctrlMac2Entry)
    entryCtrlMac2.grid(row=5, column=1)
    image1 = PhotoImage(file='./qrcode.png')
    Label(frame2, image=image1).grid()

    # Create Labels + Entries + QR Images for Frame2
    Label(frame3, text="CCU_S4d_Adapt").grid(row=0, columnspa=2)
    Label(frame3, text="GP CODE: ").grid(row=1, column=0)
    Label(frame3, text="REV:").grid(row=2, column=0)
    Label(frame3, text="SN: ").grid(row=3, column=0)
    s4dGpEntry = StringVar()
    entryS4dGp = Entry(frame3, textvariable=s4dGpEntry)
    entryS4dGp.grid(row=1, column=1)
    s4dRevEntry = StringVar()
    entryS4dRev = Entry(frame3, textvariable=s4dRevEntry)
    entryS4dRev.grid(row=2, column=1)
    s4dSnEntry = StringVar()
    entryS4dSn = Entry(frame3, textvariable=s4dSnEntry)
    entryS4dSn.grid(row=3, column=1)
    image2 = PhotoImage(file='./qrcode.png')
    Label(frame4, image=image2).grid()

    # Create Labels + Entries + QR Images for Frame3
    Label(frame5, text="CCU_SoC").grid(row=0, columnspa=2)
    Label(frame5, text="GP CODE: ").grid(row=1, column=0)
    Label(frame5, text="REV:").grid(row=2, column=0)
    Label(frame5, text="SN: ").grid(row=3, column=0)
    socGpEntry = StringVar()
    entrySocGp = Entry(frame5, textvariable=socGpEntry)
    entrySocGp.grid(row=1, column=1)
    socRevEntry = StringVar()
    entrySocRev = Entry(frame5, textvariable=socRevEntry)
    entrySocRev.grid(row=2, column=1)
    socSnEntry = StringVar()
    entrySocSn = Entry(frame5, textvariable=socSnEntry)
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