from tkinter import *
from tkinter import ttk
import pyqrcode
from fpdf import FPDF
from tkinter import filedialog
from tkinter import messagebox
import openpyxl
from openpyxl.styles import PatternFill


# Check Free SN => Which cell sheet is not in RED color?
def checkFreeSn(worksheet, row):
    for i in range(row, worksheet.max_row):
        cell_color = worksheet["A"+str(i)].fill.start_color.rgb # get cell color
        #print(cell_color)
        if cell_color == "00000000":
            #print(worksheet["A"+str(i)].value)
            break
    return i

'''
    wb = openpyxl.load_workbook('MAC&CCU_SN.xlsx')
    #ws = wb.active
    ws = wb["CCU_SoC"]
    redFill = PatternFill(start_color='FFFF0000', end_color='FFFF0000', fill_type='solid')
    i = 8
    ws["A"+str(i)].fill = redFill
    wb.save('test.xlsx')
'''


#commandImport: Import excel file to fill the entries
def commandImport(socEntry, s4dEntry, ctrlEntry):

    # Open excel file
    fileExcel = filedialog.askopenfilename(title="Abrir", initialdir="./", filetypes=(("Ficheros de Excel", "*.xlsx"),
                                        ("Todos los ficheros", "*.*")))

    if not fileExcel: # handle cancel button filedialog.askopenfilename
        return

    # Open Excel File
    wb = openpyxl.load_workbook(fileExcel, data_only=True) # data_only=True to read the cell data instead of the formula
    # Open Sheets
    wsSoC = wb['CCU_SoC']
    wsS4d = wb['CCU_S4d_Adapt']
    wsCtrl = wb['CCU_SoC_Ctrl & MAC']
    # Check free SN on CCU_SoC worksheet + fill entries
    socRow = checkFreeSn(wsSoC, 3)  # skiip the two first lines because they are titles.
    socGpTxt = str(wsSoC["A"+str(socRow)].value)
    socEntry[0].set(socGpTxt) # socGpEntry
    socRevTxt = str(wsSoC["B"+str(socRow)].value)
    socEntry[1].set(socRevTxt) # socRevEntry
    socSnTxt = str(wsSoC["C"+str(socRow)].value)
    socEntry[2].set(socSnTxt) #soCSnEntry
    # Check free SN on CCU_S4d_Adapt worksheet + fill entries
    s4dRow=checkFreeSn(wsS4d, 3)
    s4dGpTxt = str(wsS4d["A"+str(s4dRow)].value)
    s4dEntry[0].set(s4dGpTxt) # s4dGpEntry
    s4dRevTxt = str(wsS4d["B"+str(s4dRow)].value)
    s4dEntry[1].set(s4dRevTxt) # s4dRevEntry
    s4dSnTxt = str(wsS4d["C"+str(s4dRow)].value)
    s4dEntry[2].set(s4dSnTxt) #s4dSnEntry
    # Check free SN on CCU_S4d_Adapt worksheet + fill entries
    ctrlRow = checkFreeSn(wsCtrl, 3)
    CtrlGpTxt = str(wsCtrl["A"+str(ctrlRow)].value)
    ctrlEntry[0].set(CtrlGpTxt) #ctrlEntry[0]
    CtrlRevTxt = str(wsCtrl["B"+str(ctrlRow)].value)
    ctrlEntry[1].set(CtrlRevTxt) # ctrlRevEntry
    CtrlSnTxt = str(wsCtrl["C"+str(ctrlRow)].value)
    ctrlEntry[2].set(CtrlSnTxt) # ctrlSnEntry
    CtrlMac1Txt = str(wsCtrl["D"+str(ctrlRow)].value)
    ctrlEntry[3].set(CtrlMac1Txt) # ctrlMac1Entry
    CtrlMac2Txt = str(wsCtrl["E"+str(ctrlRow)].value)
    ctrlEntry[4].set(CtrlMac2Txt) # ctrlMac2Entry

#commandExport: Export to PDF QR codes
def commandExport():
    pdf = FPDF()
    pdf.add_page()

    # Set font type and line width for pdf titles and drawings
    pdf.set_font("Arial", size=15)
    pdf.set_line_width(1)
    # printing QR codes for CCU_SoC_Ctrl
    pdf.text(x=20, y=10, txt="CCU_SoC_Ctrl")
    pdf.image('qrcode_ctrl.png', x=25,  y=20, w=10, h=10)
    pdf.image('qrcode_ctrl.png', x=45, y=20, w=10, h=10)
    pdf.line(x1=70, y1=5, x2=70, y2=40)
    # printing QR codes for CCU_s4d_adapt
    pdf.text(x=85, y=10, txt="CCU_s4d_adapt")
    pdf.image('qrcode_s4d.png', x=100,  y=20, w=10, h=10)
    pdf.line(x1=135, y1=5, x2=135, y2=40)
    # printing QR codes for CCU_SoC
    pdf.text(x=155, y=10, txt="CCU_SoC")
    pdf.image('qrcode_soc.png', x=160,  y=20, w=10, h=10)

    filePdf = filedialog.asksaveasfile(mode="w", defaultextension=".pdf", filetypes=[("Ficheros PDF", "*.pdf")])

    if filePdf is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return

    pdf.output(filePdf.name, "F")
    pdf.close

    messagebox.showinfo("GaE windows messagebox", "Fichero con codigos QR generado con exito")



#commandPrint: Print QR codes
def commandQrgen(labelQr, ctrlEntry, s4dEntry, socEntry):

    #************* CCU_SoC_Ctrl QR generation ************
    qrparam1 = 'Gamesa Electric\n'
    qrparam2 = 'CCU_SoC_Ctrl\n'
    qrparam3 = "GP: " + ctrlEntry[0].get() +"\n" # ctrlGpEntry
    qrparam4 = "Rev.: " + ctrlEntry[1].get() + "\n" # ctrlRevGpEntry
    qrparam5 = "SN: " + ctrlEntry[2].get() + "\n" # ctrlSnEntry
    qrparam6 = "MAC ETH1: " + ctrlEntry[3].get() + "\n" # ctrlMac1Entry
    qrparam7 = "MAC ETH2: " + ctrlEntry[4].get() + "\n" # ctrlMac2Entry
    # Generate QR code
    qr_code = pyqrcode.create(qrparam1 + qrparam2 + qrparam3 + qrparam4 + qrparam5 + qrparam6 + qrparam7)
    qr_code.png('qrcode_ctrl.png', scale=1)
    # Refreash QR image
    image_new = PhotoImage(file='./qrcode_ctrl.png')
    labelQr[0].configure(image=image_new, bd=5, relief="groove") # labelQr[0] = labelCtrlQr
    labelQr[0].photo = image_new

    #************* CCU_S4d_Adapt QR generation ************
    qrparam1 = 'Gamesa Electric\n'
    qrparam2 = 'CCU_S4d_Adapt\n'
    qrparam3 = "GP: " + s4dEntry[0].get() + "\n" # s4dGpEntry
    qrparam4 = "Rev.: " + s4dEntry[1].get() + "\n" # s4dRevEntry
    qrparam5 = "SN: " + s4dEntry[2].get() + "\n" # s4dSnEntry
    # Generate QR code
    qr_code = pyqrcode.create(qrparam1 + qrparam2 + qrparam3 + qrparam4 + qrparam5)
    qr_code.png('qrcode_s4d.png', scale=1)
    # Refreash QR image
    image_new = PhotoImage(file='./qrcode_s4d.png')
    labelQr[1].configure(image=image_new, bd=5, relief="groove") # labelQr[1] = labelS4dQr
    labelQr[1].photo = image_new

    #************* CCU_SoC QR generation ************
    qrparam1 = 'Gamesa Electric\n'
    qrparam2 = 'CCU_SoC\n'
    qrparam3 = "GP: " + socEntry[0].get() + "\n" # socGpEntry
    qrparam4 = "Rev.: " + socEntry[1].get() + "\n" # socRevEntry
    qrparam5 = "SN: " + socEntry[2].get() + "\n" # socSnEntry
    # Generate QR code
    qr_code = pyqrcode.create(qrparam1 + qrparam2 + qrparam3 + qrparam4 + qrparam5)
    qr_code.png('qrcode_soc.png', scale=1)
    # Refreash QR image
    image_new = PhotoImage(file='./qrcode_soc.png')
    labelQr[2].configure(image=image_new, bd=5, relief="groove") # labelQr[2] = labelSocQr
    labelQr[2].photo = image_new

    messagebox.showinfo("GaE windows messagebox", "Códigos QR generados con éxito")