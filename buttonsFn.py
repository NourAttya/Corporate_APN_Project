import tkinter
from tkinter import filedialog

top=tkinter.Tk()

folder_path = tkinter.StringVar()
def browse_folder_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    # global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    return filename

def browse_file_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    # global folder_path
    filename = filedialog.askopenfilename()
    folder_path.set(filename)
    return filename

# to select a folder
def first_browser():
    file = browse_folder_button()
    folder_path.set(file)
    # tk.messagebox.showinfo("Success", "Find CSV file in the shown path")

# make another version of first_browser for files
def second_browser():
    file = browse_file_button()
    folder_path.set(file)

# browse utilities for second csv file in "Version Differences" window
file_path = tkinter.StringVar()
def browse_csv2_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    # global folder_path
    filename = filedialog.askopenfilename()
    file_path.set(filename)
    print(filename)
    return filename
def csv2_browser():
    file = browse_csv2_button()
    file_path.set(file)

# browse utilities for many files in
file1_path = tkinter.StringVar()
def browse_file1_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    # global folder_path
    filename = filedialog.askopenfilename()
    file1_path.set(filename)
    print(filename)
    return filename
def file1_browser():
    file = browse_file1_button()
    file1_path.set(file)

file2_path = tkinter.StringVar()
def browse_file2_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    # global folder_path
    filename = filedialog.askopenfilename()
    file2_path.set(filename)
    print(filename)
    return filename
def file2_browser():
    file = browse_file2_button()
    file2_path.set(file)

file3_path = tkinter.StringVar()
def browse_file3_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    # global folder_path
    filename = filedialog.askopenfilename()
    file3_path.set(filename)
    print(filename)
    return filename
def file3_browser():
    file = browse_file3_button()
    file3_path.set(file)

file4_path = tkinter.StringVar()
def browse_file4_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    # global folder_path
    filename = filedialog.askopenfilename()
    file4_path.set(filename)
    print(filename)
    return filename
def file4_browser():
    file = browse_file4_button()
    file4_path.set(file)

file5_path = tkinter.StringVar()
def browse_file5_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    # global folder_path
    filename = filedialog.askopenfilename()
    file5_path.set(filename)
    print(filename)
    return filename
def file5_browser():
    file = browse_file4_button()
    file5_path.set(file)

file6_path = tkinter.StringVar()
file7_path= tkinter.StringVar()
file8_path= tkinter.StringVar()
file9_path= tkinter.StringVar()
file10_path= tkinter.StringVar()

# For Files On Hold

def browse_multiple_files_button():
    filename = filedialog.askopenfilenames()
    folder_path.set(filename)
    return filename

def third_browser():
    file = browse_multiple_files_button()
    folder_path.set(file)

def browse_file2_button_multiple():
    # Allow user to select a directory and store it in global var
    # called folder_path
    # global folder_path
    filename = filedialog.askopenfilenames()
    file2_path.set(filename)
    print(filename)
    return filename
def file2_third_browser():
    file = browse_file2_button_multiple()
    file2_path.set(file)

def browse_file3_button_multiple():
    # Allow user to select a directory and store it in global var
    # called folder_path
    # global folder_path
    filename = filedialog.askopenfilenames()
    file3_path.set(filename)
    print(filename)
    return filename
def file3_third_browser():
    file = browse_file3_button_multiple()
    file3_path.set(file)

# Create a Tkinter variable
tkvar1= tkinter.StringVar(top)

# Create a Tkinter variable
tkvar2= tkinter.StringVar(top)

# Create a Tkinter variable
tkvar3= tkinter.StringVar(top)

# Create a Tkinter variable
tkvar4= tkinter.StringVar(top)
# on change dropdown value

# Create a Tkinter variable
tkvar5= tkinter.StringVar(top)
# on change dropdown value
# Create a Tkinter variable
tkvar6= tkinter.StringVar(top)
# on change dropdown value

def change_dropdown1(*args):
    print(tkvar1.get())
    # Dictionary with options
    StatOrDynChoices = {'Static', 'Dynamic'}
    tkvar2.set('Static')  # set the default option
    StatOrDynMenu = tkinter.OptionMenu(top,tkvar2, *StatOrDynChoices)
    StatOrDynMenu.place(x=250, y=400)
    # link function to change dropdown

    lbVRF = tkinter.Label(top, text="VRF Tunnel\nDestination IP")
    lbVRF.place(x=400, y=345)
    lbVRF.config(font=("Calibri", 12, 'bold'), fg='black')

    entryVRF = tkinter.Entry(top, textvariable=file6_path)
    entryVRF.place(x=520, y=355, width=200, height=25)
    entryVRF.delete(0, 'end')

    lbIPRange = tkinter.Label(top, text="IP Range")
    lbIPRange.place(x=400, y=400)
    lbIPRange.config(font=("Calibri", 12, 'bold'), fg='black')

    entryIPRange = tkinter.Entry(top, textvariable=file7_path)
    entryIPRange.place(x=520, y=400, width=200, height=25)
    entryIPRange.delete(0, 'end')

    if (tkvar1.get() == '3G WIc' or tkvar1.get() == 'Sim2Sim'):
        StatOrDynMenu.configure(state="disabled")
    if(tkvar1.get() != 'PC Connectivity'):
        lbVRF.configure(state="disabled")
        entryVRF.configure(state="disabled")
        lbIPRange.configure(state="disabled")
        entryIPRange.configure(state="disabled")






# on change dropdown value
def change_dropdown2(*args):
    print(tkvar2.get())

# on change dropdown value
def change_dropdown3(*args):
    print(tkvar3.get())

# on change dropdown value
def change_dropdown4(*args):
    print(tkvar4.get())

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

def change_dropdownAPNType(*args):
    print(tkvar6.get())
    # Dictionary with options
    StatOrDynChoices = {'Static', 'Dynamic'}
     # set the default option
    StatOrDynMenu = tkinter.OptionMenu(top, tkvar5, *StatOrDynChoices)
    StatOrDynMenu.place(x=580, y=270)

    if (tkvar6.get() == 'Internet'):
        StatOrDynMenu.configure(state="disabled")
        tkvar5.set('Dynamic')
    elif (tkvar6.get() == '3G WIC'):
        StatOrDynMenu.configure(state="disabled")
        tkvar5.set('Static')
    elif (tkvar6.get() == 'Sim2Sim'):
        StatOrDynMenu.configure(state="disabled")
        tkvar5.set('Static')
    elif (tkvar6.get() == 'Commerical_main_APN'):
        StatOrDynMenu.configure(state="disabled")
        tkvar5.set('Dynamic')