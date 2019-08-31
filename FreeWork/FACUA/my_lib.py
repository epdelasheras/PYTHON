from tkinter import messagebox

def floor_callback(floor_var):
    print (floor_var.get())

# menu_top_file functions callbacks
def menu_top_file_new():
    messagebox.showinfo(title='New window', message='You made click on "New"!')

def menu_top_file_open():
    messagebox.showinfo(title='Open window', message='You made click on "Open"!')

def menu_top_file_saveas():
    messagebox.showinfo(title='Save as window', message='You made click on "Save as"!')

def menu_top_file_exit():
    var = messagebox.askquestion(message='Are you sure you want to exit?', title='Exit window')
    if var == 'yes':
        quit()

# menu_top_config functions callbacks
def menu_top_file_f1():
    messagebox.showinfo(title='New window', message='You made click on "Floor 1"!')

def menu_top_file_f2():
    messagebox.showinfo(title='New window', message='You made click on "Floor 2"!')

def menu_top_file_f3():
    messagebox.showinfo(title='New window', message='You made click on "Floor 3"!')

def menu_top_file_f4():
    messagebox.showinfo(title='New window', message='You made click on "Floor 4"!')


