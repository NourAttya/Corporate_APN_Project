import tkinter
import tkinter.font as font
import buttonsFn
from Corporate_APNs import IDNSandAPNconfig
from Corporate_APNs_DB import  Build_APN_DB
from tkinter import messagebox
import xlrd
from IP_Pool_Expansion import IPPoolExpansion

#Nour Attyia
#Ahmed Ayman



#Corporate_APNs
def CorpConfigRun():

    IDNSandAPNconfig.IDNSandAPNConfigCorp(buttonsFn.file3_path.get(), buttonsFn.file2_path.get(), buttonsFn.tkvar3.get(), buttonsFn.file1_path.get(), buttonsFn.tkvar1.get(), buttonsFn.tkvar2.get(), buttonsFn.file6_path.get(),buttonsFn.tkvar4.get(),buttonsFn.file7_path.get())


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

    MTXMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar3, *MTXs)
    MTXMenu.place(x=300, y=245)
    MTXMenu.config(height=1, width=4, fg='black')
    buttonsFn.tkvar3.set(MTXs[0])  # set the default option


    SecMTXMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar4, *MTXs)
    SecMTXMenu.place(x=300, y=300)
    SecMTXMenu.config(height=1, width=4, fg='black')
    buttonsFn.tkvar4.set(MTXs[0])  # set the default option


def openPacketCorpMenu():
    buttonsFn.top.grid_slaves()
    # define font
    myFont = font.Font(family='Calibri', size=12)
    myFont2 = font.Font(family='Calibri', size=15)

    #Imgname2 = tkinter.PhotoImage(file="Vodafone2.png")

    background_label = tkinter.Label(buttonsFn.top)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #background_label.configure(background='red')
    # Define Buttons of the main window

    lbAPNName = tkinter.Label(buttonsFn.top, text="APN Name")
    lbAPNName.place(x=100, y=100)
    lbAPNName.config(font=("Calibri", 12, 'bold'), fg='black')

    entryAPNName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file3_path)
    entryAPNName.place(x=250, y=100, width=200, height=25)
    entryAPNName.delete(0, 'end')

    lbIPPool = tkinter.Label(buttonsFn.top, text="IP Pool")
    lbIPPool.place(x=100, y=150)
    lbIPPool.config(font=("Calibri", 12, 'bold'), fg='black')

    entryIPPool = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
    entryIPPool.place(x=250, y=150, width=200, height=25)
    entryIPPool.delete(0, 'end')





    # 1
    lbExcel = tkinter.Label(buttonsFn.top, text="Select Excel Sheet")
    lbExcel.place(x=100, y=205)
    lbExcel.config(font=("Calibri", 12, 'bold'), fg='black')

    entryExcelPath = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file1_path)
    entryExcelPath.place(x=250, y=205, width=400, height=25)
    entryExcelPath.delete(0, 'end')

    buttonBrowse = tkinter.Button(buttonsFn.top, text="Browse", command=UpdateDropDownFromExcelForCorporateAPN)
    buttonBrowse.place(x=670, y=200)
    buttonBrowse['font'] = myFont

    # link function to change dropdown
    #this is for MTX dropdown list
    buttonsFn.tkvar3.trace('w', buttonsFn.change_dropdown3)


    lbPrimaryMTX = tkinter.Label(buttonsFn.top, text="Choose Primary MTX")
    lbPrimaryMTX.place(x=100, y=250)
    lbPrimaryMTX.config(font=("Calibri", 12, 'bold'), fg='black')

    lbSecMTX= tkinter.Label(buttonsFn.top, text="Choose Secondary MTX")
    lbSecMTX.place(x=100, y=300)
    lbSecMTX.config(font=("Calibri", 12, 'bold'), fg='black')


    PrimaryMTXMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar3, [""])
    PrimaryMTXMenu.place(x=300, y=245)
    PrimaryMTXMenu.config(height=1, width=4, fg='black')
    buttonsFn.tkvar3.set("")  # set the default option

    SecMTXMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar4, [""])
    SecMTXMenu.place(x=300, y=300)
    SecMTXMenu.config(height=1, width=4, fg='black')
    buttonsFn.tkvar4.set("")  # set the default option


    # Dictionary with options
    APNTypeChoices = {'Internet APN', 'PC Connectivity', '3G WIc', 'Sim2Sim'}
    buttonsFn.tkvar1.set('Internet APN')  # set the default option


    lbAPNType = tkinter.Label(buttonsFn.top, text="Choose APN Type")
    lbAPNType.place(x=100, y=345)
    lbAPNType.config(font=("Calibri", 12, 'bold'), fg='black')
    APNTypeMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar1, *APNTypeChoices)
    APNTypeMenu.place(x=250, y=345)

    # link function to change dropdown
    buttonsFn.tkvar1.trace('w', buttonsFn.change_dropdown1)

    lbVRF= tkinter.Label(buttonsFn.top, text="VRF Tunnel\nDestination IP")
    lbVRF.place(x=400, y=345)
    lbVRF.config(font=("Calibri", 12, 'bold'), fg='black')
    lbVRF.configure(state="disabled")

    entryVRF = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file6_path)
    entryVRF.place(x=520, y=355, width=200, height=25)
    entryVRF.delete(0, 'end')
    entryVRF.configure(state="disabled")

    lbIPRange = tkinter.Label(buttonsFn.top, text="IP Range")
    lbIPRange.place(x=400, y=400)
    lbIPRange.config(font=("Calibri", 12, 'bold'), fg='black')
    lbIPRange.configure(state="disabled")

    entryIPRange = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file7_path)
    entryIPRange.place(x=520, y=400, width=200, height=25)
    entryIPRange.delete(0, 'end')
    entryIPRange.configure(state="disabled")

    lbStatOrDyn = tkinter.Label(buttonsFn.top, text="Choose Static\n or Dynamic")
    lbStatOrDyn.place(x=100, y=400)
    lbStatOrDyn.config(font=("Calibri", 12, 'bold'), fg='black')



    StatOrDynChoices = {'Static', 'Dynamic'}
    buttonsFn.tkvar2.set('Static')  # set the default option
    StatOrDynMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar2, *StatOrDynChoices)
    StatOrDynMenu.place(x=250, y=400)
    # link function to change dropdown
    buttonsFn.tkvar2.trace('w', buttonsFn.change_dropdown2)



    buttonRun = tkinter.Button(buttonsFn.top, text="Run", command=CorpConfigRun)
    buttonRun.place(x=330, y=460)
    buttonRun.config(height=1, width=10)
    buttonRun['font'] = myFont2

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openCorpMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=2, width=8, fg='black')
    buttonBack['font'] = myFont

    e = tkinter.Text(buttonsFn.top, width=75, height=10)
    e.bind("<Tab>", buttonsFn.focus_next_widget)
    # Appearnce Title

    Title = tkinter.Label(buttonsFn.top, text="Packet Corporate APN Configuration")
    Title.config(font=("Calibri", 28), foreground="black")
    Title.place(x=150, y=20)

    # Define the size of the main window
    buttonsFn.top.geometry("800x520")  # Width x Height
    buttonsFn.top.title("Packet Corporate APN Configuration")
    buttonsFn.top.mainloop()
    # New_Window.configure(background='white')


def openSecurityCorpMenu():
    buttonsFn.top.grid_slaves()
    # define font
    myFont = font.Font(family='Calibri', size=12)
    myFont2 = font.Font(family='Calibri', size=15)

    # Imgname2 = tkinter.PhotoImage(file="Vodafone2.png")

    background_label = tkinter.Label(buttonsFn.top)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # background_label.configure(background='red')
    # Define Buttons of the main window

    lbAPNName = tkinter.Label(buttonsFn.top, text="APN Name")
    lbAPNName.place(x=100, y=100)
    lbAPNName.config(font=("Calibri", 12, 'bold'), fg='black')

    entryAPNName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file1_path)
    entryAPNName.place(x=250, y=100, width=200, height=25)
    entryAPNName.delete(0, 'end')

    lbSimRange = tkinter.Label(buttonsFn.top, text="Sim Range")
    lbSimRange.place(x=100, y=150)
    lbSimRange.config(font=("Calibri", 12, 'bold'), fg='black')

    entrySimRange = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
    entrySimRange.place(x=250, y=150, width=200, height=25)
    entrySimRange.delete(0, 'end')

    lbLoopbackIP = tkinter.Label(buttonsFn.top, text="Loopback IP")
    lbLoopbackIP.place(x=100, y=200)
    lbLoopbackIP.config(font=("Calibri", 12, 'bold'), fg='black')
    lbLoopbackIP.configure(state="active")

    entryLoopbackIP = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file3_path)
    entryLoopbackIP.place(x=250, y=200, width=200, height=25)
    entryLoopbackIP.delete(0, 'end')
    entryLoopbackIP.configure(state="normal")

    # Dictionary with options
    APNTypeChoices = {'Internet APN', 'PC Connectivity', '3G WIc'}
    buttonsFn.tkvar1.set('3G WIc')  # set the default option

    lbAPNType = tkinter.Label(buttonsFn.top, text="Choose APN Type")
    lbAPNType.place(x=100, y=250)
    lbAPNType.config(font=("Calibri", 12, 'bold'), fg='black')
    APNTypeMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar1, *APNTypeChoices)
    APNTypeMenu.place(x=250, y=250)

    # link function to change dropdown
    buttonsFn.tkvar1.trace('w', buttonsFn.change_dropdownSecurityApnType)

    lbSrcTunnel = tkinter.Label(buttonsFn.top, text="Src Tunnel\nFixed")
    lbSrcTunnel.place(x=100, y=300)
    lbSrcTunnel.config(font=("Calibri", 12, 'bold'), fg='black')
    lbSrcTunnel.configure(state="disabled")

    entrySrcTunnel = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file4_path)
    entrySrcTunnel.place(x=250, y=300, width=200, height=25)
    entrySrcTunnel.delete(0, 'end')
    entrySrcTunnel.configure(state="disabled")

    lbPublicIP= tkinter.Label(buttonsFn.top, text="Public IP")
    lbPublicIP.place(x=100, y=350)
    lbPublicIP.config(font=("Calibri", 12, 'bold'), fg='black')
    lbPublicIP.configure(state="disabled")

    entryPublicIP = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file5_path)
    entryPublicIP.place(x=250, y=350, width=200, height=25)
    entryPublicIP.delete(0, 'end')
    entryPublicIP.configure(state="disabled")


    buttonRun = tkinter.Button(buttonsFn.top, text="Run")
    buttonRun.place(x=330, y=415)
    buttonRun.config(height=1, width=10)
    buttonRun['font'] = myFont2

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openCorpMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=2, width=8, fg='black')
    buttonBack['font'] = myFont

    e = tkinter.Text(buttonsFn.top, width=75, height=10)
    e.bind("<Tab>", buttonsFn.focus_next_widget)
    # Appearnce Title

    Title = tkinter.Label(buttonsFn.top, text="Security Corporate APN Configuration")
    Title.config(font=("Calibri", 28), foreground="black")
    Title.place(x=150, y=20)

    # Define the size of the main window
    buttonsFn.top.geometry("800x470")  # Width x Height
    buttonsFn.top.title("Security Corporate APN Configuration")
    buttonsFn.top.mainloop()
    # New_Window.configure(background='white')


def openCorpMenu():
    # Main menu
    # define font
    myFont = font.Font(family='Calibri', size=15)

    Imgname = tkinter.PhotoImage(file="Vodafone.png")
    background_label = tkinter.Label(buttonsFn.top, image=Imgname)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Define Buttons of the main window
    # 1
    buttonCorpAPNAudit = tkinter.Button(buttonsFn.top, text="Packet Corporate\n APN Creation", command=openPacketCorpMenu)
    buttonCorpAPNAudit.place(x=170, y=70)
    buttonCorpAPNAudit.config(height=3, width=20, fg='black', background='white')
    buttonCorpAPNAudit['font'] = myFont
    # 2
    buttonIDNSAudit = tkinter.Button(buttonsFn.top, text="Security Corporate\n APN Creation",command=openSecurityCorpMenu)
    buttonIDNSAudit.place(x=170, y=180)
    buttonIDNSAudit.config(height=3, width=20, fg='black', background='white')
    buttonIDNSAudit['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openDataMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=1, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("550x350")  # Width x Height
    buttonsFn.top.title("Corporate APN Creation")
    # top.configure(background = 'sky blue')
    buttonsFn.top.mainloop()


#IP_Pool_Expansion GUI

def IPPoolExpanRun():
    IPpools = []
    Subnetnames = []
    if buttonsFn.file3_path.get()!="":
        IPpools.append(buttonsFn.file3_path.get())
    if buttonsFn.file5_path.get() != "":
        IPpools.append(buttonsFn.file5_path.get())
    if buttonsFn.file7_path.get() != "":
        IPpools.append(buttonsFn.file7_path.get())
    if buttonsFn.file9_path.get() != "":
        IPpools.append(buttonsFn.file9_path.get())
    if buttonsFn.file2_path.get() != "":
        Subnetnames.append(buttonsFn.file2_path.get())
    if buttonsFn.file4_path.get() != "":
        Subnetnames.append(buttonsFn.file4_path.get())
    if buttonsFn.file6_path.get() != "":
        Subnetnames.append(buttonsFn.file6_path.get())
    if buttonsFn.file8_path.get() != "":
        Subnetnames.append(buttonsFn.file8_path.get())
    print(IPpools)
    print(Subnetnames)
    # get path to save output script(in the same folder of excel sheet)
    fileNameToRemove = buttonsFn.file1_path.get().split('/')[-1]
    pathToSave = buttonsFn.file1_path.get().replace(fileNameToRemove, "")
    IPPoolExpansion.IPPoolExpansionConfig(buttonsFn.tkvar2.get(),IPpools,Subnetnames,buttonsFn.tkvar4.get(),buttonsFn.tkvar5.get(),buttonsFn.tkvar3.get(),buttonsFn.tkvar1.get(),buttonsFn.file10_path.get(),pathToSave)



def UpdateDropDownFromExcelForIPpoolExpansion():
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

    MTXMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar4, *MTXs)
    MTXMenu.place(x=250, y=170)
    MTXMenu.config(height=1, width=4, fg='black')
    buttonsFn.tkvar4.set(MTXs[0])  # set the default option


#to add another subnets and pool names in the gui
numOfSubnet=1
def AddSubnet():

    global numOfSubnet
    if(numOfSubnet ==1):

        lbPoolName = tkinter.Label(buttonsFn.top, text="Pool Name 2")
        lbPoolName.place(x=430, y=320)
        lbPoolName.config(font=("Calibri", 12, 'bold'), fg='black')

        entryPoolName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file4_path)
        entryPoolName.place(x=580, y=320, width=120, height=25)
        entryPoolName.delete(0, 'end')

        lbSubnet = tkinter.Label(buttonsFn.top, text="Subnet 2")
        lbSubnet.place(x=430, y=370)
        lbSubnet.config(font=("Calibri", 12, 'bold'), fg='black')

        entrySubnet = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file5_path)
        entrySubnet.place(x=580, y=370, width=120, height=25)
        entrySubnet.delete(0, 'end')



    elif(numOfSubnet==2):
        lbPoolName = tkinter.Label(buttonsFn.top, text="Pool Name 3")
        lbPoolName.place(x=100, y=420)
        lbPoolName.config(font=("Calibri", 12, 'bold'), fg='black')

        entryPoolName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file6_path)
        entryPoolName.place(x=250, y=420, width=120, height=25)
        entryPoolName.delete(0, 'end')

        lbSubnet = tkinter.Label(buttonsFn.top, text="Subnet 3")
        lbSubnet.place(x=100, y=470)
        lbSubnet.config(font=("Calibri", 12, 'bold'), fg='black')

        entrySubnet = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file7_path)
        entrySubnet.place(x=250, y=470, width=120, height=25)
        entrySubnet.delete(0, 'end')

    elif(numOfSubnet==3):
        lbPoolName = tkinter.Label(buttonsFn.top, text="Pool Name 4")
        lbPoolName.place(x=430, y=420)
        lbPoolName.config(font=("Calibri", 12, 'bold'), fg='black')

        entryPoolName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file8_path)
        entryPoolName.place(x=580, y=420, width=120, height=25)
        entryPoolName.delete(0, 'end')

        lbSubnet = tkinter.Label(buttonsFn.top, text="Subnet 4")
        lbSubnet.place(x=430, y=470)
        lbSubnet.config(font=("Calibri", 12, 'bold'), fg='black')

        entrySubnet = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file9_path)
        entrySubnet.place(x=580, y=470, width=120, height=25)
        entrySubnet.delete(0, 'end')
    else:
        messagebox.showinfo("Error", "Maximum Number Of subnets is 4")
    numOfSubnet += 1

def openIpPoolExpansionMenu():
    global numOfSubnet
    numOfSubnet = 1
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
    lbMTX.place(x=100, y=170)
    lbMTX.config(font=("Calibri", 12, 'bold'), fg='black')

    MTXMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar4, [""])
    MTXMenu.place(x=250, y=170)
    MTXMenu.config(height=1, width=4, fg='black')
    buttonsFn.tkvar4.set("")  # set the default option

    lbAPNName = tkinter.Label(buttonsFn.top, text="APN Name")
    lbAPNName.place(x=430, y=170)
    lbAPNName.config(font=("Calibri", 12, 'bold'), fg='black')

    entryAPNName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file10_path)
    entryAPNName.place(x=580, y=170, width=120, height=25)
    entryAPNName.delete(0, 'end')

    lbContextName = tkinter.Label(buttonsFn.top, text="Context Name")
    lbContextName.place(x=100, y=220)
    lbContextName.config(font=("Calibri", 12, 'bold'), fg='black')

    contextChoices = {'Gi-IMS', 'Gi-DPI','Gi-Corp2','Gi-Corp','VAS-Corp'}
    buttonsFn.tkvar2.set('Gi-DPI')  # set the default option
    ContextNameMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar2, *contextChoices)
    ContextNameMenu.place(x=250, y=220)
    # link function to change dropdown
    buttonsFn.tkvar2.trace('w', buttonsFn.change_dropdown2)

    # Dictionary with options
    APNTypeChoices = {'Internet', 'PC Connectivity', '3G WIC', 'Sim2Sim','Commerical_main_APN'}
    buttonsFn.tkvar6.set('Commerical_main_APN')  # set the default option

    lbAPNType = tkinter.Label(buttonsFn.top, text="Choose APN Type")
    lbAPNType.place(x=430, y=220)
    lbAPNType.config(font=("Calibri", 12, 'bold'), fg='black')
    APNTypeMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar6, *APNTypeChoices)
    APNTypeMenu.place(x=580, y=220)

    # link function to change dropdown
    buttonsFn.tkvar6.trace('w', buttonsFn.change_dropdownAPNType)

    lbNodeVendor = tkinter.Label(buttonsFn.top, text="Node Vendor")
    lbNodeVendor.place(x=100, y=270)
    lbNodeVendor.config(font=("Calibri", 12, 'bold'), fg='black')

    NodeVendorChoices = {'Cisco', 'Huawei', 'Ericsson'}
    buttonsFn.tkvar3.set('Cisco')  # set the default option
    NodeVendorMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar3, *NodeVendorChoices)
    NodeVendorMenu.place(x=250, y=270)
    # link function to change dropdown
    buttonsFn.tkvar3.trace('w', buttonsFn.change_dropdown3)

    lbStatOrDyn = tkinter.Label(buttonsFn.top, text="Choose Static\n or Dynamic")
    lbStatOrDyn.place(x=430, y=270)
    lbStatOrDyn.config(font=("Calibri", 12, 'bold'), fg='black')

    StatOrDynChoices = {'Static', 'Dynamic'}
    buttonsFn.tkvar5.set('Dynamic')  # set the default option
    StatOrDynMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar5, *StatOrDynChoices)
    StatOrDynMenu.place(x=580, y=270)
    StatOrDynMenu.configure(state="disabled")

    # link function to change dropdown
    buttonsFn.tkvar5.trace('w', buttonsFn.change_dropdown4)

    lbPoolName = tkinter.Label(buttonsFn.top, text="Pool Name")
    lbPoolName.place(x=100, y=320)
    lbPoolName.config(font=("Calibri", 12, 'bold'), fg='black')


    entryPoolName = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
    entryPoolName.place(x=250, y=320, width=120, height=25)
    entryPoolName.delete(0, 'end')

    lbSubnet = tkinter.Label(buttonsFn.top, text="Subnet")
    lbSubnet.place(x=100, y=370)
    lbSubnet.config(font=("Calibri", 12, 'bold'), fg='black')


    entrySubnet = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file3_path)
    entrySubnet.place(x=250, y=370, width=120, height=25)
    entrySubnet.delete(0, 'end')

    buttonAddSubnet = tkinter.Button(buttonsFn.top, text="Add Subnet", command=AddSubnet)
    buttonAddSubnet.place(x=250, y=530)
    buttonAddSubnet.config(height=1, width=12)
    buttonAddSubnet['font'] = myFont2

    buttonRun = tkinter.Button(buttonsFn.top, text="Run", command=IPPoolExpanRun)
    buttonRun.place(x=450, y=530)
    buttonRun.config(height=1, width=12)
    buttonRun['font'] = myFont2

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openDataMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=2, width=8, fg='black')
    buttonBack['font'] = myFont

    e = tkinter.Text(buttonsFn.top, width=75, height=10)
    e.bind("<Tab>", buttonsFn.focus_next_widget)
    # Appearnce Title

    Title = tkinter.Label(buttonsFn.top, text="IP Pool Expansion")
    Title.config(font=("Calibri", 30), foreground="black")
    Title.place(x=260, y=20)

    # Define the size of the main window
    buttonsFn.top.geometry("800x600")  # Width x Height
    buttonsFn.top.title("IP Pool Expansion")
    buttonsFn.top.mainloop()
    # New_Window.configure(background='white')

def BuildDBRun():
    Build_APN_DB.APNDB(buttonsFn.folder_path.get())

def openBuildDBMenu():
    # define font
    myFont = font.Font(family='Calibri', size=12)
    myFont2 = font.Font(family='Calibri', size=15)

    # Imgname2 = tkinter.PhotoImage(file="Vodafone2.png")

    background_label = tkinter.Label(buttonsFn.top)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # background_label.configure(background='red')
    # Define Buttons of the main window

    lbConfigFile = tkinter.Label(buttonsFn.top, text="Select GGSN\nConfigurations Folder")
    lbConfigFile.place(x=70, y=200)
    lbConfigFile.config(font=("Calibri", 12, 'bold'), fg='black')

    entryConfigFile = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.folder_path)
    entryConfigFile.place(x=250, y=200, width=400, height=25)
    entryConfigFile.delete(0, 'end')

    buttonBrowse = tkinter.Button(buttonsFn.top, text="Browse", command=buttonsFn.first_browser)
    buttonBrowse.place(x=670, y=190)
    buttonBrowse['font'] = myFont

    buttonRun = tkinter.Button(buttonsFn.top, text="Run", command=BuildDBRun)
    buttonRun.place(x=330, y=330)
    buttonRun.config(height=1, width=12)
    buttonRun['font'] = myFont2

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openCorporateAPNAuditMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=2, width=8, fg='black')
    buttonBack['font'] = myFont

    e = tkinter.Text(buttonsFn.top, width=75, height=10)
    e.bind("<Tab>", buttonsFn.focus_next_widget)
    # Appearnce Title

    Title = tkinter.Label(buttonsFn.top, text="Build Corporate APNs DB")
    Title.config(font=("Calibri", 24), foreground="black")
    Title.place(x=260, y=40)

    # Define the size of the main window
    buttonsFn.top.geometry("800x400")  # Width x Height
    buttonsFn.top.title("Build Corporate APNs DB")
    buttonsFn.top.mainloop()
    # New_Window.configure(background='white')

def openAPNsCleanupMenu():
    # define font
    myFont = font.Font(family='Calibri', size=12)
    myFont2 = font.Font(family='Calibri', size=15)

    # Imgname2 = tkinter.PhotoImage(file="Vodafone2.png")

    background_label = tkinter.Label(buttonsFn.top)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # background_label.configure(background='red')
    # Define Buttons of the main window

    lbExcel = tkinter.Label(buttonsFn.top, text="Select APNs \nExcel Sheet")
    lbExcel.place(x=150, y=130)
    lbExcel.config(font=("Calibri", 12, 'bold'), fg='black')

    entryExcel = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file1_path)
    entryExcel.place(x=250, y=130, width=400, height=25)
    entryExcel.delete(0, 'end')

    buttonBrowse = tkinter.Button(buttonsFn.top, text="Browse", command=buttonsFn.file1_browser)
    buttonBrowse.place(x=670, y=130)
    buttonBrowse['font'] = myFont

    lbFrom= tkinter.Label(buttonsFn.top, text="From")
    lbFrom.place(x=150, y=230)
    lbFrom.config(font=("Calibri", 12, 'bold'), fg='black')

    entryFrom = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file1_path)
    entryFrom.place(x=250, y=230, width=120, height=25)
    entryFrom.delete(0, 'end')

    lbTo = tkinter.Label(buttonsFn.top, text="To")
    lbTo.place(x=400, y=230)
    lbTo.config(font=("Calibri", 12, 'bold'), fg='black')

    entryTo = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
    entryTo.place(x=450, y=230, width=120, height=25)
    entryTo.delete(0, 'end')

    buttonRun = tkinter.Button(buttonsFn.top, text="Run")
    buttonRun.place(x=330, y=330)
    buttonRun.config(height=1, width=12)
    buttonRun['font'] = myFont2

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openCorporateAPNAuditMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=2, width=8, fg='black')
    buttonBack['font'] = myFont

    e = tkinter.Text(buttonsFn.top, width=75, height=10)
    e.bind("<Tab>", buttonsFn.focus_next_widget)
    # Appearnce Title

    Title = tkinter.Label(buttonsFn.top, text="APNs Cleanup")
    Title.config(font=("Calibri", 24), foreground="black")
    Title.place(x=300, y=40)

    # Define the size of the main window
    buttonsFn.top.geometry("800x400")  # Width x Height
    buttonsFn.top.title("APNs Cleanup")
    buttonsFn.top.mainloop()
    # New_Window.configure(background='white')

def openCorporateAPNAuditMenu():
    # Main menu
    # define font
    myFont = font.Font(family='Calibri', size= 15)

    Imgname = tkinter.PhotoImage(file="Vodafone.png")
    background_label = tkinter.Label(buttonsFn.top,image=Imgname)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Define Buttons of the main window
    # 1
    buttonBuildDB = tkinter.Button(buttonsFn.top, text="Build Corporate\nAPNs DB",command=openBuildDBMenu)
    buttonBuildDB.place(x=170, y=70)
    buttonBuildDB.config(height=3, width=20,  fg='black', background = 'white')
    buttonBuildDB['font'] = myFont
    # 2
    buttonUpdateDB= tkinter.Button(buttonsFn.top, text="APNs Cleanup",command=openAPNsCleanupMenu)
    buttonUpdateDB.place(x=170, y=180)
    buttonUpdateDB.config(height=3, width=20,  fg='black', background = 'white')
    buttonUpdateDB['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openPacketAuditMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=1, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("550x350")  # Width x Height
    buttonsFn.top.title("Corporate APNs Audit")
    #top.configure(background = 'sky blue')
    buttonsFn.top.mainloop()
def openPacketAuditMenu():
    # Main menu
    # define font
    myFont = font.Font(family='Calibri', size=15)

    Imgname = tkinter.PhotoImage(file="Vodafone.png")
    background_label = tkinter.Label(buttonsFn.top, image=Imgname)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Define Buttons of the main window
    # 1
    buttonCorpAPNAudit = tkinter.Button(buttonsFn.top, text="Corporate APN Audit", command=openCorporateAPNAuditMenu)
    buttonCorpAPNAudit.place(x=170, y=70)
    buttonCorpAPNAudit.config(height=3, width=20, fg='black', background='white')
    buttonCorpAPNAudit['font'] = myFont
    # 2
    buttonIDNSAudit = tkinter.Button(buttonsFn.top, text="IDNS Audit")
    buttonIDNSAudit.place(x=170, y=180)
    buttonIDNSAudit.config(height=3, width=20, fg='black', background='white')
    buttonIDNSAudit['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openDataMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=1, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("550x350")  # Width x Height
    buttonsFn.top.title("Packet Audit")
    # top.configure(background = 'sky blue')
    buttonsFn.top.mainloop()

def openDataMenu():

    # Main menu
    # define font
    myFont = font.Font(family='Calibri', size= 15)

    Imgname = tkinter.PhotoImage(file="Vodafone.png")
    background_labe = tkinter.Label(buttonsFn.top,image=Imgname)
    background_labe.place(x=0, y=0, relwidth=1, relheight=1)

    # Define Buttons of the main window
    # 1
    button_Corporate_APN = tkinter.Button(buttonsFn.top, text="Corporate APN", command=openCorpMenu)
    button_Corporate_APN.place(x=100, y=100)
    button_Corporate_APN.config(height=3, width=20,  fg='black', background = 'white')
    button_Corporate_APN['font'] = myFont
    # 2
    button_Test_APN = tkinter.Button(buttonsFn.top, text="Test APN")
    button_Test_APN.place(x=100, y=220)
    button_Test_APN.config(height=3, width=20,  fg='black', background = 'white')
    button_Test_APN['font'] = myFont

    # 3
    button_IP_Pool_Expansion = tkinter.Button(buttonsFn.top, text="IP Pool Expansion", command=openIpPoolExpansionMenu)
    button_IP_Pool_Expansion.place(x=350 ,y=100)
    button_IP_Pool_Expansion.config(height=3, width=20, fg='black', background='white')
    button_IP_Pool_Expansion['font'] = myFont

    # 4
    button_Corporate_APN_DB = tkinter.Button(buttonsFn.top, text="Packet Audit", command=openPacketAuditMenu)
    button_Corporate_APN_DB.place(x=350, y=220)
    button_Corporate_APN_DB.config(height=3, width=20, fg='black', background='white')
    button_Corporate_APN_DB['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openMainMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=1, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("700x400")  # Width x Height
    buttonsFn.top.title("Packet Tool")
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
