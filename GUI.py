import tkinter
import tkinter.font as font
import buttonsFn
from Corporate_APNs import IDNSandAPNconfig
from tkinter import messagebox
import xlrd

#Nour Attyia
#Ahmed Ayman



#Corporate_APNs
def CorpConfigRun():

    IDNSandAPNconfig.IDNSandAPNConfigCorp(buttonsFn.file3_path.get(), buttonsFn.file2_path.get(), buttonsFn.tkvar3.get(), buttonsFn.file1_path.get(), buttonsFn.tkvar1.get(), buttonsFn.tkvar2.get(), buttonsFn.file6_path.get(),buttonsFn.tkvar4.get(),buttonsFn.file7_path.get())
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
    buttonsFn.tkvar1.set('Internet APN')  # set the default option


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

    lb3 = tkinter.Label(buttonsFn.top, text="VRF Tunnel\nDestination IP")
    lb3.place(x=400, y=345)
    lb3.config(font=("Calibri", 12, 'bold'), fg='black')
    lb3.configure(state="disabled")

    filepathText1 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file6_path)
    filepathText1.place(x=520, y=355, width=200, height=25)
    filepathText1.delete(0, 'end')
    filepathText1.configure(state="disabled")

    lb4 = tkinter.Label(buttonsFn.top, text="IP Range")
    lb4.place(x=400, y=400)
    lb4.config(font=("Calibri", 12, 'bold'), fg='black')
    lb4.configure(state="disabled")

    filepathText2 = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file7_path)
    filepathText2.place(x=520, y=400, width=200, height=25)
    filepathText2.delete(0, 'end')
    filepathText2.configure(state="disabled")

    lb2 = tkinter.Label(buttonsFn.top, text="Choose Static\n or Dynamic")
    lb2.place(x=100, y=400)
    lb2.config(font=("Calibri", 12, 'bold'), fg='black')



    # link function to change dropdown
    buttonsFn.tkvar1.trace('w', buttonsFn.change_dropdown1)

    choices2 = {'Static', 'Dynamic'}
    buttonsFn.tkvar2.set('Static')  # set the default option
    popupMenu2 = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar2, *choices2)
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


#IP_Pool_Expansion GUI

def IPPoolExpanRun():
    Subnets = []
    PoolNames = []
    if buttonsFn.file3_path.get()!="":
        Subnets.append(buttonsFn.file3_path.get())
    if buttonsFn.file5_path.get() != "":
        Subnets.append(buttonsFn.file5_path.get())
    if buttonsFn.file7_path.get() != "":
        Subnets.append(buttonsFn.file7_path.get())
    if buttonsFn.file9_path.get() != "":
        Subnets.append(buttonsFn.file9_path.get())
    if buttonsFn.file2_path.get() != "":
        PoolNames.append(buttonsFn.file2_path.get())
    if buttonsFn.file4_path.get() != "":
        PoolNames.append(buttonsFn.file4_path.get())
    if buttonsFn.file6_path.get() != "":
        PoolNames.append(buttonsFn.file6_path.get())
    if buttonsFn.file8_path.get() != "":
        PoolNames.append(buttonsFn.file8_path.get())
    print(Subnets)
    print(PoolNames)

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
    popupMenu1 = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar4, *choices1)
    popupMenu1.place(x=250, y=200)
    popupMenu1.config(height=1, width=4, fg='black')
    buttonsFn.tkvar4.set(choices1[0])  # set the default option


numOfSubnet=1
def AddSubnet():

    global numOfSubnet
    if(numOfSubnet ==1):

        lbPoolName = tkinter.Label(buttonsFn.top, text="Pool Name 2")
        lbPoolName.place(x=400, y=250)
        lbPoolName.config(font=("Calibri", 12, 'bold'), fg='black')

        entryPoolName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file4_path)
        entryPoolName.place(x=550, y=250, width=120, height=25)
        entryPoolName.delete(0, 'end')

        lbSubnet = tkinter.Label(buttonsFn.top, text="Subnet 2")
        lbSubnet.place(x=400, y=300)
        lbSubnet.config(font=("Calibri", 12, 'bold'), fg='black')

        entrySubnet = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file5_path)
        entrySubnet.place(x=550, y=300, width=120, height=25)
        entrySubnet.delete(0, 'end')



    elif(numOfSubnet==2):
        lbPoolName = tkinter.Label(buttonsFn.top, text="Pool Name 3")
        lbPoolName.place(x=100, y=350)
        lbPoolName.config(font=("Calibri", 12, 'bold'), fg='black')

        entryPoolName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file6_path)
        entryPoolName.place(x=250, y=350, width=120, height=25)
        entryPoolName.delete(0, 'end')

        lbSubnet = tkinter.Label(buttonsFn.top, text="Subnet 3")
        lbSubnet.place(x=100, y=400)
        lbSubnet.config(font=("Calibri", 12, 'bold'), fg='black')

        entrySubnet = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file7_path)
        entrySubnet.place(x=250, y=400, width=120, height=25)
        entrySubnet.delete(0, 'end')

    elif(numOfSubnet==3):
        lbPoolName = tkinter.Label(buttonsFn.top, text="Pool Name 4")
        lbPoolName.place(x=400, y=350)
        lbPoolName.config(font=("Calibri", 12, 'bold'), fg='black')

        entryPoolName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file8_path)
        entryPoolName.place(x=550, y=350, width=120, height=25)
        entryPoolName.delete(0, 'end')

        lbSubnet = tkinter.Label(buttonsFn.top, text="Subnet 4")
        lbSubnet.place(x=400, y=400)
        lbSubnet.config(font=("Calibri", 12, 'bold'), fg='black')

        entrySubnet = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file9_path)
        entrySubnet.place(x=550, y=400, width=120, height=25)
        entrySubnet.delete(0, 'end')
    else:
        messagebox.showinfo("Error", "Maximum Number Of subnets is 4")
    numOfSubnet += 1

def openIpPoolExpansionMenu():
    # define font
    myFont = font.Font(family='Calibri', size=12)
    myFont2 = font.Font(family='Calibri', size=15)

    #Imgname2 = tkinter.PhotoImage(file="Vodafone2.png")

    background_label = tkinter.Label(buttonsFn.top)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #background_label.configure(background='red')
    # Define Buttons of the main window


    lbExcel = tkinter.Label(buttonsFn.top, text="Select Excel Sheet")
    lbExcel.place(x=100, y=100)
    lbExcel.config(font=("Calibri", 12, 'bold'), fg='black')

    entryExcel = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file1_path)
    entryExcel.place(x=250, y=100, width=400, height=25)
    entryExcel.delete(0, 'end')

    buttonBrowse = tkinter.Button(buttonsFn.top, text="Browse", command=UpdateDropDownFromExcelForIPpoolExpansion)
    buttonBrowse.place(x=670, y=100)
    buttonBrowse['font'] = myFont


    lbMTX = tkinter.Label(buttonsFn.top, text="Choose MTX")
    lbMTX.place(x=100, y=150)
    lbMTX.config(font=("Calibri", 12, 'bold'), fg='black')

    lbContextName = tkinter.Label(buttonsFn.top, text="Context Name")
    lbContextName.place(x=100, y=150)
    lbContextName.config(font=("Calibri", 12, 'bold'), fg='black')

    contextChoices = {'Gi-IMS', 'Gi-DPI','Gi-Corp2','Gi-Corp','VAS-Corp'}
    buttonsFn.tkvar2.set('Gi-DPI')  # set the default option
    ContextNameMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar2, *contextChoices)
    ContextNameMenu.place(x=250, y=150)
    # link function to change dropdown
    buttonsFn.tkvar2.trace('w', buttonsFn.change_dropdown2)


    lbNodeVendor = tkinter.Label(buttonsFn.top, text="Node Vendor")
    lbNodeVendor.place(x=100, y=200)
    lbNodeVendor.config(font=("Calibri", 12, 'bold'), fg='black')

    contextChoices = {'Cisco', 'Huawei', 'Ericsson'}
    buttonsFn.tkvar3.set('Cisco')  # set the default option
    ContextNameMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar3, *contextChoices)
    ContextNameMenu.place(x=250, y=200)
    # link function to change dropdown
    buttonsFn.tkvar3.trace('w', buttonsFn.change_dropdown3)

    lbPoolName = tkinter.Label(buttonsFn.top, text="Pool Name")
    lbPoolName.place(x=100, y=250)
    lbPoolName.config(font=("Calibri", 12, 'bold'), fg='black')

    entryPoolName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
    entryPoolName.place(x=250, y=250, width=120, height=25)
    entryPoolName.delete(0, 'end')

    lbSubnet = tkinter.Label(buttonsFn.top, text="Subnet")
    lbSubnet.place(x=100, y=300)
    lbSubnet.config(font=("Calibri", 12, 'bold'), fg='black')

    entrySubnet = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file3_path)
    entrySubnet.place(x=250, y=300, width=120, height=25)
    entrySubnet.delete(0, 'end')

    buttonAddSubnet = tkinter.Button(buttonsFn.top, text="Add Subnet", command=AddSubnet)
    buttonAddSubnet.place(x=200, y=470)
    buttonAddSubnet.config(height=1, width=12)
    buttonAddSubnet['font'] = myFont2

    buttonRun = tkinter.Button(buttonsFn.top, text="Run", command=IPPoolExpanRun)
    buttonRun.place(x=400, y=470)
    buttonRun.config(height=1, width=12)
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
    buttonsFn.top.geometry("800x540")  # Width x Height
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
    button_Test_APN = tkinter.Button(buttonsFn.top, text="Test APN")
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
    buttonBack.config(height=1, width=8, fg='black', bg='white')
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
