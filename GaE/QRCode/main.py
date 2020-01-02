from tkinter import *
from my_lib import *
import pyqrcode

param1 = 'Gamesa Electric\n'
param2 = 'CCU_SoC\n'
param3 = 'GP: GP487746\n'
param4 = 'Rev.: 2.1\n'
param5 = 'SN: P42019300005\n'
param6 = 'MAC ETH1: 000CF2040004\n'
param7 = 'MAC ETH2: 000CF2048004\n'

param = []
param = param1 + param2 + param3 + param4 + param5
if param6 != "\n":
    param = param + param6
if param7 != "\n":
    param = param + param7
qr_code = pyqrcode.create(param)
qr_code.png('qrcode.png', scale=1)
print(qr_code.terminal(quiet_zone=1))

# Create window
window = Tk()
#window.geometry('600x600+0+0') #600x600 => pixels; +0+0 => localization
window.title('GaE QR CCU Code Generator')

# Creating CCU_SoC_Ctrl frame
img_qr_soc_ctrl = PhotoImage(file='./qrcode.png')
row_separator = 0
create_frame(window, "CCU_SoC_Ctrl", "GP CODE: ", "REV: ", "SN: ", "MAC_ETH1: ", "MAC_ETH2: ", img_qr_soc_ctrl,
             row_separator)
# Creating CCU_S4d_Adapt frame
img_qr_s4d_adapt = PhotoImage(file='./qrcode.png')
row_separator = 2
create_frame(window, "CCU_S4d_Adapt", "GP CODE: ", "REV: ", "SN: ", "\n", "\n", img_qr_s4d_adapt, row_separator)
# Creating CCU_SoC frame
img_qr_soc_global = PhotoImage(file='./qrcode.png')
row_separator = 4
create_frame(window, "CCU_SoC", "GP CODE: ", "REV: ", "SN: ", "\n", "\n", img_qr_soc_global, row_separator)

#Creating import button
row_button = 6
col_button = 0
create_button(window,"Import", row_button, col_button)

#Creating Print button
row_button = 6
col_button = 1
create_button(window,"Print", row_button, col_button)

window.mainloop()
