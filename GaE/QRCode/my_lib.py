from tkinter import *
from tkinter import ttk
import pyqrcode
from fpdf import FPDF
from tkinter import filedialog
from tkinter import messagebox
import xlrd

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
def commandImport(socEntry, s4dEntry, ctrlEntry):

    # Open excel file
    fileExcel = filedialog.askopenfilename(title="Abrir", initialdir="./", filetypes=(("Ficheros de Excel", "*.xls"),
                                        ("Todos los ficheros", "*.*")))

    if not fileExcel: # handle cancel button filedialog.askopenfilename
        return

    # Open Excel File
    wb = xlrd.open_workbook(fileExcel, formatting_info=True)
    # Open Sheets
    wsSoC = wb.sheet_by_name('CCU_SoC')
    wsS4d = wb.sheet_by_name('CCU_S4d_Adapt')
    wsCtrl = wb.sheet_by_name('CCU_SoC_Ctrl & MAC')
    # Check free SN on CCU_SoC worksheet + fill entries
    socRow=checkFreeSn(wb, wsSoC, 2, 0) #skiip the two first lines because they are titles.
    socGpTxt = str(wsSoC.cell_value(socRow, 0)) #ws.cell_value(row, column)
    socEntry[0].set(socGpTxt) # socGpEntry
    socRevTxt = str(wsSoC.cell_value(socRow, 1))
    socEntry[1].set(socRevTxt) # socRevEntry
    socSnTxt = str(wsSoC.cell_value(socRow, 2))
    socEntry[2].set(socSnTxt) #soCSnEntry
    # Check free SN on CCU_S4d_Adapt worksheet + fill entries
    s4dRow=checkFreeSn(wb, wsS4d, 2, 0)
    s4dGpTxt = str(wsS4d.cell_value(s4dRow, 0))
    s4dEntry[0].set(s4dGpTxt) # s4dGpEntry
    s4dRevTxt = str(wsS4d.cell_value(s4dRow, 1))
    s4dEntry[1].set(s4dRevTxt) # s4dRevEntry
    s4dSnTxt = str(wsS4d.cell_value(s4dRow, 2))
    s4dEntry[2].set(s4dSnTxt) #s4dSnEntry
    # Check free SN on CCU_S4d_Adapt worksheet + fill entries
    ctrlRow = checkFreeSn(wb, wsS4d, 2, 0)
    CtrlGpTxt = str(wsCtrl.cell_value(ctrlRow, 0))
    ctrlEntry[0].set(CtrlGpTxt) #ctrlEntry[0]
    CtrlRevTxt = str(wsCtrl.cell_value(ctrlRow, 1))
    ctrlEntry[1].set(CtrlRevTxt) # ctrlRevEntry
    CtrlSnTxt = str(wsCtrl.cell_value(ctrlRow, 2))
    ctrlEntry[2].set(CtrlSnTxt) # ctrlSnEntry
    CtrlMac1Txt = str(wsCtrl.cell_value(ctrlRow, 3))
    ctrlEntry[3].set(CtrlMac1Txt) # ctrlMac1Entry
    CtrlMac2Txt = str(wsCtrl.cell_value(ctrlRow, 4))
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