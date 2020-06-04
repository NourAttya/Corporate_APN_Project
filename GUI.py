import time
import tkinter
import tkinter.font as font
import buttonsFn
from Corporate_APNs import IDNSandAPNconfig
import xlrd

def TestConfigRun():
    IDNSandAPNconfig.IDNSandAPNConfigTest(buttonsFn.file3_path.get(), buttonsFn.file2_path.get(), buttonsFn.file4_path.get(), buttonsFn.file1_path.get())


def CorpConfigRun():
    IDNSandAPNconfig.IDNSandAPNConfigCorp(buttonsFn.file3_path.get(), buttonsFn.file2_path.get(), buttonsFn.tkvar3.get(), buttonsFn.file1_path.get(), buttonsFn.tkvar1.get(), buttonsFn.tkvar2.get(), buttonsFn.file6_path.get(),buttonsFn.tkvar4.get())

#Nour Attyia
#Ahmed Ayman
choices3=[]

def UpdateDropDownFromExcelForCorporateAPN():
    MTXs = []
    buttonsFn.file1_browser()
    # open the excel sheet and get the corresponding number to MTX name
    wb = xlrd.open_workbook(buttonsFn.file1_path.get())
    sheet = wb.sheet_by_index(0)
    firstRow = 0
    for j in range(sheet.nrows):
        row = sheet.row_values(j)
        if firstRow == 0:
            for i in range(len(row)):
                if (row[i] == "MTX Name"):
                    MTXindex = i
            firstRow = 1
        else:
            MTXs.append( str(row[MTXindex]))
    print(MTXs)
    choices3 = MTXs
    popupMenu3 = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar3, *choices3)
    popupMenu3.place(x=300, y=245)
    popupMenu3.config(height=1, width=4, fg='black')
    buttonsFn.tkvar3.set(choices3[0])  # set the default option

    choices4=MTXs
    popupMenu4 = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar4, *choices4)
    popupMenu4.place(x=300, y=300)
    popupMenu4.config(height=1, width=4, fg='black')
    buttonsFn.tkvar4.set(choices3[0])  # set the default option
def UpdateDropDownFromExcelForIPpoolExpansion():
    MTXs = []
    buttonsFn.file3_browser()
    # open the excel sheet and get the corresponding number to MTX name
    wb = xlrd.open_workbook(buttonsFn.file3_path.get())
    sheet = wb.sheet_by_index(0)
    firstRow = 0
    for j in range(sheet.nrows):
        row = sheet.row_values(j)
        if firstRow == 0:
            for i in range(len(row)):
                if (row[i] == "MTX Name"):
                    MTXindex = i
            firstRow = 1
        else:
            MTXs.append( str(row[MTXindex]))
    print(MTXs)
    choices1 = MTXs
    popupMenu1 = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar3, *choices1)
    popupMenu1.place(x=250, y=310)
    popupMenu1.config(height=1, width=4, fg='black')
    buttonsFn.tkvar3.set(choices1[0])  # set the default option


def openTestMenu():
    # define font
    myFont = font.Font(family='Calibri', size=12)
    myFont2 = font.Font(family='Calibri', size=15)

    background_label = tkinter.Label(buttonsFn.top)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #background_label.configure(background='red')
    # Define Buttons of the main window

    lb1 = tkinter.Label(buttonsFn.top, text="APN Name")
    lb1.place(x=100, y=100)
    lb1.config(font=("Calibri", 12, 'bold'), fg='black',background = 'red')

    filepathText1 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file3_path)
    filepathText1.place(x=250, y=100, width=200, height=25)
    filepathText1.delete(0, 'end')

    lb2 = tkinter.Label(buttonsFn.top, text="IP Pool")
    lb2.place(x=100, y=150)
    lb2.config(font=("Calibri", 12, 'bold'), fg='black',background = 'red')

    filepathText1 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
    filepathText1.place(x=250, y=150, width=200, height=25)
    filepathText1.delete(0, 'end')

    lb4 = tkinter.Label(buttonsFn.top, text="MTX")
    lb4.place(x=100, y=200)
    lb4.config(font=("Calibri", 12, 'bold'), fg='black',background = 'red')



    filepathText1 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file4_path)
    filepathText1.place(x=250, y=200, width=200, height=25)
    filepathText1.delete(0, 'end')

    buttonRun = tkinter.Button(buttonsFn.top, text="Run", command=TestConfigRun)
    buttonRun.place(x=300, y=340)
    buttonRun.config(height=2, width=16, fg='black')
    buttonRun['font'] = myFont2

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openDataMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=2, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # 1
    lb1 = tkinter.Label(buttonsFn.top, text="Select Excel Sheet")
    lb1.place(x=100, y=250)
    lb1.config(font=("Calibri", 12, 'bold'), fg='black',background = 'red')

    filepathText1 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file1_path)
    filepathText1.place(x=250, y=250, width=400, height=25)
    filepathText1.delete(0, 'end')

    buttonBrowse1 = tkinter.Button(buttonsFn.top, text="Browse", command=buttonsFn.file1_browser)
    buttonBrowse1.place(x=670, y=245)
    buttonBrowse1['font'] = myFont

    # Appearnce Title

    lb = tkinter.Label(buttonsFn.top, text="Test APN Configuration")
    lb.config(font=("Calibri", 28), foreground="black",background = 'red')
    lb.place(x=200, y=20)

    # Define the size of the main window
    buttonsFn.top.geometry("800x550")  # Width x Height
    buttonsFn.top.title("Test APN Configuration")
    # New_Window.configure(background='white')
def openCorpMenu():
    # define font
    myFont = font.Font(family='Calibri', size=12)
    myFont2 = font.Font(family='Calibri', size=15)

    #Imgname2 = tkinter.PhotoImage(file="Vodafone2.png")

    background_label = tkinter.Label(buttonsFn.top)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #background_label.configure(background='red')
    # Define Buttons of the main window

    lb1 = tkinter.Label(buttonsFn.top, text="APN Name")
    lb1.place(x=100, y=100)
    lb1.config(font=("Calibri", 12, 'bold'), fg='black')

    filepathText1 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file3_path)
    filepathText1.place(x=250, y=100, width=200, height=25)
    filepathText1.delete(0, 'end')

    lb2 = tkinter.Label(buttonsFn.top, text="IP Pool")
    lb2.place(x=100, y=150)
    lb2.config(font=("Calibri", 12, 'bold'), fg='black')

    filepathText1 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
    filepathText1.place(x=250, y=150, width=200, height=25)
    filepathText1.delete(0, 'end')


    # link function to change dropdown
    buttonsFn.tkvar3.trace('w', buttonsFn.change_dropdown3)


    # 1
    lb1 = tkinter.Label(buttonsFn.top, text="Select Excel Sheet")
    lb1.place(x=100, y=205)
    lb1.config(font=("Calibri", 12, 'bold'), fg='black')

    filepathText1 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file1_path)
    filepathText1.place(x=250, y=205, width=400, height=25)
    filepathText1.delete(0, 'end')

    buttonBrowse1 = tkinter.Button(buttonsFn.top, text="Browse", command=UpdateDropDownFromExcelForCorporateAPN)
    buttonBrowse1.place(x=670, y=200)
    buttonBrowse1['font'] = myFont


    # Dictionary with options
    choices1 = {'Internet APN', 'PC Connectivity', '3G WIc', 'Sim2Sim'}
    buttonsFn.tkvar1.set('3G WIc')  # set the default option


    lb4 = tkinter.Label(buttonsFn.top, text="Choose Primary MTX")
    lb4.place(x=100, y=250)
    lb4.config(font=("Calibri", 12, 'bold'), fg='black')

    lb5 = tkinter.Label(buttonsFn.top, text="Choose Secondary MTX")
    lb5.place(x=100, y=300)
    lb5.config(font=("Calibri", 12, 'bold'), fg='black')


    popupMenu3 = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar3, [""])
    popupMenu3.place(x=300, y=245)
    popupMenu3.config(height=1, width=4, fg='black')
    buttonsFn.tkvar3.set("")  # set the default option

    popupMenu4 = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar4, [""])
    popupMenu4.place(x=300, y=300)
    popupMenu4.config(height=1, width=4, fg='black')
    buttonsFn.tkvar4.set("")  # set the default option

    popupMenu1 = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar1, *choices1)
    lb2 = tkinter.Label(buttonsFn.top, text="Choose APN Type")
    lb2.place(x=100, y=345)
    lb2.config(font=("Calibri", 12, 'bold'), fg='black')
    popupMenu1.place(x=250, y=345)
    # link function to change dropdown
    buttonsFn.tkvar1.trace('w', buttonsFn.change_dropdown1)

    lb3 = tkinter.Label(buttonsFn.top, text="VRF Tunnel\nDestination IP")
    lb3.place(x=400, y=345)
    lb3.config(font=("Calibri", 12, 'bold'), fg='black')

    filepathText1 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file6_path)
    filepathText1.place(x=520, y=355, width=200, height=25)
    filepathText1.delete(0, 'end')

    lb2 = tkinter.Label(buttonsFn.top, text="Choose Static\n or Dynamic")
    lb2.place(x=100, y=400)
    lb2.config(font=("Calibri", 12, 'bold'), fg='black')

    buttonsFn.tkvar2.set("")  # set the default option
    popupMenu2 = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar2, [""])
    popupMenu2.place(x=250, y=400)
    # link function to change dropdown
    buttonsFn.tkvar2.trace('w', buttonsFn.change_dropdown2)

    buttonRun = tkinter.Button(buttonsFn.top, text="Run", command=CorpConfigRun)
    buttonRun.place(x=330, y=460)
    buttonRun.config(height=1, width=10)
    buttonRun['font'] = myFont2

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openDataMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=2, width=8, fg='black')
    buttonBack['font'] = myFont

    e = tkinter.Text(buttonsFn.top, width=75, height=10)
    e.bind("<Tab>", buttonsFn.focus_next_widget)
    # Appearnce Title

    lb = tkinter.Label(buttonsFn.top, text="Corporate APN Configuration")
    lb.config(font=("Calibri", 28), foreground="black")
    lb.place(x=200, y=20)

    # Define the size of the main window
    buttonsFn.top.geometry("800x520")  # Width x Height
    buttonsFn.top.title("Corporate APN Configuration")
    buttonsFn.top.mainloop()
    # New_Window.configure(background='white')

def openIpPoolExpansionMenu():
    # define font
    myFont = font.Font(family='Calibri', size=12)
    myFont2 = font.Font(family='Calibri', size=15)

    #Imgname2 = tkinter.PhotoImage(file="Vodafone2.png")

    background_label = tkinter.Label(buttonsFn.top)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #background_label.configure(background='red')
    # Define Buttons of the main window

    lb1 = tkinter.Label(buttonsFn.top, text="Username")
    lb1.place(x=100, y=120)
    lb1.config(font=("Calibri", 12, 'bold'), fg='black')

    filepathText1 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file1_path)
    filepathText1.place(x=250, y=120, width=200, height=25)
    filepathText1.delete(0, 'end')

    lb2 = tkinter.Label(buttonsFn.top, text="Password")
    lb2.place(x=100, y=180)
    lb2.config(font=("Calibri", 12, 'bold'), fg='black')

    filepathText2 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
    filepathText2.place(x=250, y=180, width=200, height=25)
    filepathText2.delete(0, 'end')

    # 1
    lb3 = tkinter.Label(buttonsFn.top, text="Select Excel Sheet")
    lb3.place(x=100, y=250)
    lb3.config(font=("Calibri", 12, 'bold'), fg='black')

    filepathText3 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file3_path)
    filepathText3.place(x=250, y=250, width=400, height=25)
    filepathText3.delete(0, 'end')

    buttonBrowse1 = tkinter.Button(buttonsFn.top, text="Browse", command=UpdateDropDownFromExcelForIPpoolExpansion)
    buttonBrowse1.place(x=670, y=250)
    buttonBrowse1['font'] = myFont


    lb4 = tkinter.Label(buttonsFn.top, text="Choose MTX")
    lb4.place(x=100, y=310)
    lb4.config(font=("Calibri", 12, 'bold'), fg='black')


    lb5 = tkinter.Label(buttonsFn.top, text="Subnet")
    lb5.place(x=100, y=370)
    lb5.config(font=("Calibri", 12, 'bold'), fg='black')

    filepathText4 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file6_path)
    filepathText4.place(x=250, y=375, width=200, height=25)
    filepathText4.delete(0, 'end')


    buttonRun = tkinter.Button(buttonsFn.top, text="Run", command=CorpConfigRun)
    buttonRun.place(x=330, y=440)
    buttonRun.config(height=2, width=15)
    buttonRun['font'] = myFont2

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openDataMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=2, width=8, fg='black')
    buttonBack['font'] = myFont

    e = tkinter.Text(buttonsFn.top, width=75, height=10)
    e.bind("<Tab>", buttonsFn.focus_next_widget)
    # Appearnce Title

    lb = tkinter.Label(buttonsFn.top, text="IP Pool Expansion")
    lb.config(font=("Calibri", 30), foreground="black")
    lb.place(x=260, y=20)

    # Define the size of the main window
    buttonsFn.top.geometry("800x520")  # Width x Height
    buttonsFn.top.title("IP Pool Expansion")
    buttonsFn.top.mainloop()
    # New_Window.configure(background='white')

def openDataMenu():

    # Main menu
    # define font
    myFont = font.Font(family='Calibri', size= 15)

    Imgname = tkinter.PhotoImage(file="Vodafone.png")
    background_label = tkinter.Label(buttonsFn.top,image=Imgname)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Define Buttons of the main window
    # 1
    button_Corporate_APN = tkinter.Button(buttonsFn.top, text="Corporate APN", command=openCorpMenu)
    button_Corporate_APN.place(x=240, y=70)
    button_Corporate_APN.config(height=3, width=20,  fg='black', background = 'white')
    button_Corporate_APN['font'] = myFont
    # 2
    button_Test_APN = tkinter.Button(buttonsFn.top, text="Test APN", command=openTestMenu)
    button_Test_APN.place(x=240, y=200)
    button_Test_APN.config(height=3, width=20,  fg='black', background = 'white')
    button_Test_APN['font'] = myFont

    # 3
    button_IP_Pool_Expansion = tkinter.Button(buttonsFn.top, text="IP Pool Expansion", command=openIpPoolExpansionMenu)
    button_IP_Pool_Expansion.place(x=240, y=330)
    button_IP_Pool_Expansion.config(height=3, width=20, fg='black', background='white')
    button_IP_Pool_Expansion['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openMainMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=2, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("700x500")  # Width x Height
    buttonsFn.top.title("Data Tool")
    #top.configure(background = 'sky blue')

    buttonsFn.top.mainloop()
def openMainMenu():

    # Main menu
    # define font
    myFont = font.Font(family='Calibri', size= 15)

    Imgname = tkinter.PhotoImage(file="Vodafone.png")
    background_label = tkinter.Label(buttonsFn.top,image=Imgname)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Define Buttons of the main window
    # 1
    buttonIR21_Automations = tkinter.Button(buttonsFn.top, text="Voice Domain")
    buttonIR21_Automations.place(x=170, y=70)
    buttonIR21_Automations.config(height=3, width=20,  fg='black', background = 'white')
    buttonIR21_Automations['font'] = myFont
    # 2
    buttonRAPsAndDeductions = tkinter.Button(buttonsFn.top, text="Data Domain", command=openDataMenu)
    buttonRAPsAndDeductions.place(x=170, y=180)
    buttonRAPsAndDeductions.config(height=3, width=20,  fg='black', background = 'white')
    buttonRAPsAndDeductions['font'] = myFont


    # Define the size of the main window
    buttonsFn.top.geometry("550x350")  # Width x Height
    buttonsFn.top.title("CN Planning & Configuration App")
    #top.configure(background = 'sky blue')

    buttonsFn.top.mainloop()

openMainMenu()
