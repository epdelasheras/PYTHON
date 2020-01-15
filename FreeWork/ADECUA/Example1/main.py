from tkinter import *
from my_lib import *

window = Tk()
window.geometry('600x600+0+0') #600x600 => pixels; +0+0 => localization
window.title('FACUA')

img = PhotoImage(file = './bloque.png')
Label(window,image=img).place(x=120,y=20)

Label(window,text='Select the floor to edit:',font=(None,18)).place(x=70,y=340)
floor_var = StringVar()
floor_entry = Entry(window,textvariable=floor_var).place(x=320,y=343,height=25, width=20)
floor_button = Button(window,text='OK!',command=lambda: floor_callback(floor_var)).place(x=340,y=343)

#Create top menu tab
menu_top_tab = Menu(window)
#Create top menu options
menu_top_file   = Menu(menu_top_tab)
menu_top_config = Menu(menu_top_tab)
#Create menu_top_file commands
menu_top_file.add_command (label="New",command=menu_top_file_new)
menu_top_file.add_command (label="Open",command=menu_top_file_open)
menu_top_file.add_command (label="Save as",command=menu_top_file_saveas)
menu_top_file.add_separator()
menu_top_file.add_command (label="Exit",command=menu_top_file_exit)
#Create menu_top_config commands
menu_top_config.add_command (label="Floor1",command=menu_top_file_f1)
menu_top_config.add_command (label="Floor2",command=menu_top_file_f2)
menu_top_config.add_command (label="Floor3",command=menu_top_file_f3)
menu_top_config.add_command (label="Floor4",command=menu_top_file_f4)
#Add menus to the menu_top_tab
menu_top_tab.add_cascade(label='File',menu=menu_top_file)
menu_top_tab.add_cascade(label='Config',menu=menu_top_config)
#Place menu top tab on the window
window.config(menu=menu_top_tab)
window.mainloop()