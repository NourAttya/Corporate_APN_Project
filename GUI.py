import tkinter
import tkinter.font as font
import buttonsFn
from Corporate_APNs import IDNSandAPNconfig
from Corporate_APNs_DB import  Build_APN_DB
from tkinter import messagebox
import xlrd
from IP_Pool_Expansion import IPPoolExpansion
from Security_Corp_APN import Sec3GWIC_Script,SecInternet_script,SecPC_Connectivity_Script
#Nour Attyiaa
#Ahmed Ayman



#Corporate_APNs
def CorpConfigRun():

    IDNSandAPNconfig.IDNSandAPNConfigCorp(buttonsFn.file3_path.get(), buttonsFn.file2_path.get(), buttonsFn.tkvar3.get(), buttonsFn.file1_path.get(), buttonsFn.tkvar1.get(), buttonsFn.tkvar2.get(), buttonsFn.file6_path.get(),buttonsFn.tkvar4.get(),buttonsFn.file7_path.get(),buttonsFn.file4_path.get(),buttonsFn.file5_path.get())


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
    entryVRF.place(x=550, y=355, width=200, height=25)
    entryVRF.configure(state="disabled")
    entryVRF.delete(0, 'end')

    lbIPRange = tkinter.Label(buttonsFn.top, text="IP Range")
    lbIPRange.place(x=400, y=400)
    lbIPRange.config(font=("Calibri", 12, 'bold'), fg='black')
    lbIPRange.configure(state="disabled")

    entryIPRange = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file7_path)
    entryIPRange.place(x=550, y=400, width=200, height=25)
    entryIPRange.configure(state="disabled")
    entryIPRange.delete(0, 'end')

    lbStatOrDyn = tkinter.Label(buttonsFn.top, text="Choose Static\n or Dynamic")
    lbStatOrDyn.place(x=100, y=400)
    lbStatOrDyn.config(font=("Calibri", 12, 'bold'), fg='black')



    StatOrDynChoices = {'Static', 'Dynamic'}
    buttonsFn.tkvar2.set('Static')  # set the default option
    StatOrDynMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar2, *StatOrDynChoices)
    StatOrDynMenu.place(x=250, y=400)
    # link function to change dropdown
    buttonsFn.tkvar2.trace('w', buttonsFn.change_dropdown2)

    lbUsername = tkinter.Label(buttonsFn.top, text="Remedy's Username")
    lbUsername.place(x=100, y=470)
    lbUsername.config(font=("Calibri", 12, 'bold'), fg='black')

    entryUsername = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file4_path)
    entryUsername.place(x=250, y=470, width=120, height=25)
    entryUsername.delete(0, 'end')

    lbPassword = tkinter.Label(buttonsFn.top, text="Remedy's Password")
    lbPassword.place(x=400, y=470)
    lbPassword.config(font=("Calibri", 12, 'bold'), fg='black')

    entryPassword = tkinter.Entry(buttonsFn.top, show="*", textvariable=buttonsFn.file5_path)
    entryPassword.place(x=550, y=470, width=120, height=25)
    entryPassword.delete(0, 'end')

    buttonRun = tkinter.Button(buttonsFn.top, text="Run", command=CorpConfigRun)
    buttonRun.place(x=330, y=530)
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
    buttonsFn.top.geometry("800x600")  # Width x Height
    buttonsFn.top.title("Packet Corporate APN Configuration")

    buttonsFn.top.mainloop()
    # New_Window.configure(background='white')

def securityCorpRun():
    if(buttonsFn.tkvar1.get()=="PC Connectivity"):
        SecPC_Connectivity_Script.SecPC_Connectivity_Script(buttonsFn.file1_path.get(), buttonsFn.file4_path.get())
    elif (buttonsFn.tkvar1.get() == "3G WIc"):
        Sec3GWIC_Script.Sec3GWIC_Script(buttonsFn.file1_path.get(),buttonsFn.file2_path.get(),buttonsFn.file3_path.get())

    elif (buttonsFn.tkvar1.get() == "Internet APN"):
     SecInternet_script.SecInternet_Script(buttonsFn.file1_path.get(), buttonsFn.file2_path.get(), buttonsFn.file5_path.get())

def change_dropdownSecurityApnType(*args):
    if(buttonsFn.tkvar1.get()=="PC Connectivity"):

        lbSimRange = tkinter.Label(buttonsFn.top, text="Sim Range")
        lbSimRange.place(x=100, y=150)
        lbSimRange.config(font=("Calibri", 12, 'bold'), fg='black')
        lbSimRange.configure(state="disabled")

        entrySimRange = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
        entrySimRange.place(x=250, y=150, width=200, height=25)
        entrySimRange.configure(state="disabled")
        entrySimRange.delete(0, 'end')

        lbSrcTunnel = tkinter.Label(buttonsFn.top, text="Src Tunnel\nFixed")
        lbSrcTunnel.place(x=100, y=300)
        lbSrcTunnel.config(font=("Calibri", 12, 'bold'), fg='black')
        lbSrcTunnel.configure(state="active")

        entrySrcTunnel = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file4_path)
        entrySrcTunnel.place(x=250, y=300, width=200, height=25)
        entrySrcTunnel.configure(state="normal")
        entrySrcTunnel.delete(0, 'end')

        lbLoopbackIP = tkinter.Label(buttonsFn.top, text="Loopback IP")
        lbLoopbackIP.place(x=100, y=200)
        lbLoopbackIP.config(font=("Calibri", 12, 'bold'), fg='black')
        lbLoopbackIP.configure(state="disabled")

        entryLoopbackIP = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file3_path)
        entryLoopbackIP.place(x=250, y=200, width=200, height=25)
        entryLoopbackIP.configure(state="disabled")
        entryLoopbackIP.delete(0, 'end')

        lbPublicIP = tkinter.Label(buttonsFn.top, text="Public IP")
        lbPublicIP.place(x=100, y=350)
        lbPublicIP.config(font=("Calibri", 12, 'bold'), fg='black')
        lbPublicIP.configure(state="disabled")

        entryPublicIP = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file5_path)
        entryPublicIP.place(x=250, y=350, width=200, height=25)
        entryPublicIP.configure(state="disabled")
        entryPublicIP.delete(0, 'end')

    elif (buttonsFn.tkvar1.get()=="Internet APN"):
        lbSimRange = tkinter.Label(buttonsFn.top, text="Sim Range")
        lbSimRange.place(x=100, y=150)
        lbSimRange.config(font=("Calibri", 12, 'bold'), fg='black')

        entrySimRange = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
        entrySimRange.place(x=250, y=150, width=200, height=25)
        entrySimRange.delete(0, 'end')

        lbSrcTunnel = tkinter.Label(buttonsFn.top, text="Src Tunnel\nFixed")
        lbSrcTunnel.place(x=100, y=300)
        lbSrcTunnel.config(font=("Calibri", 12, 'bold'), fg='black')
        lbSrcTunnel.configure(state="disabled")

        entrySrcTunnel = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file4_path)
        entrySrcTunnel.place(x=250, y=300, width=200, height=25)
        entrySrcTunnel.configure(state="disabled")
        entrySrcTunnel.delete(0, 'end')

        lbPublicIP = tkinter.Label(buttonsFn.top, text="Public IP")
        lbPublicIP.place(x=100, y=350)
        lbPublicIP.config(font=("Calibri", 12, 'bold'), fg='black')
        lbPublicIP.configure(state="active")

        entryPublicIP = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file5_path)
        entryPublicIP.place(x=250, y=350, width=200, height=25)
        entryPublicIP.configure(state="normal")
        entryPublicIP.delete(0, 'end')

        lbLoopbackIP = tkinter.Label(buttonsFn.top, text="Loopback IP")
        lbLoopbackIP.place(x=100, y=200)
        lbLoopbackIP.config(font=("Calibri", 12, 'bold'), fg='black')
        lbLoopbackIP.configure(state="disabled")

        entryLoopbackIP = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file3_path)
        entryLoopbackIP.place(x=250, y=200, width=200, height=25)
        entryLoopbackIP.configure(state="disabled")
        entryLoopbackIP.delete(0, 'end')

    elif(buttonsFn.tkvar1.get()=="3G WIc"):
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
        entryLoopbackIP.configure(state="normal")
        entryLoopbackIP.delete(0, 'end')

        lbSrcTunnel = tkinter.Label(buttonsFn.top, text="Src Tunnel\nFixed")
        lbSrcTunnel.place(x=100, y=300)
        lbSrcTunnel.config(font=("Calibri", 12, 'bold'), fg='black')
        lbSrcTunnel.configure(state="disabled")

        entrySrcTunnel = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file4_path)
        entrySrcTunnel.place(x=250, y=300, width=200, height=25)
        entrySrcTunnel.configure(state="disabled")
        entrySrcTunnel.delete(0, 'end')

        lbPublicIP = tkinter.Label(buttonsFn.top, text="Public IP")
        lbPublicIP.place(x=100, y=350)
        lbPublicIP.config(font=("Calibri", 12, 'bold'), fg='black')
        lbPublicIP.configure(state="disabled")

        entryPublicIP = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file5_path)
        entryPublicIP.place(x=250, y=350, width=200, height=25)
        entryPublicIP.configure(state="disabled")
        entryPublicIP.delete(0, 'end')

def openSecurityCorpMenu():

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
    entryLoopbackIP.configure(state="normal")
    entryLoopbackIP.delete(0, 'end')
    # Dictionary with options
    APNTypeChoices = {'Internet APN', 'PC Connectivity', '3G WIc'}
    buttonsFn.tkvar1.set('3G WIc')  # set the default option

    lbAPNType = tkinter.Label(buttonsFn.top, text="Choose APN Type")
    lbAPNType.place(x=100, y=250)
    lbAPNType.config(font=("Calibri", 12, 'bold'), fg='black')
    APNTypeMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar1, *APNTypeChoices)
    APNTypeMenu.place(x=250, y=250)

    # link function to change dropdown
    buttonsFn.tkvar1.trace('w',change_dropdownSecurityApnType)

    lbSrcTunnel = tkinter.Label(buttonsFn.top, text="Src Tunnel\nFixed")
    lbSrcTunnel.place(x=100, y=300)
    lbSrcTunnel.config(font=("Calibri", 12, 'bold'), fg='black')
    lbSrcTunnel.configure(state="disabled")

    entrySrcTunnel = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file4_path)
    entrySrcTunnel.place(x=250, y=300, width=200, height=25)
    entrySrcTunnel.configure(state="disabled")
    entrySrcTunnel.delete(0, 'end')

    lbPublicIP= tkinter.Label(buttonsFn.top, text="Public IP")
    lbPublicIP.place(x=100, y=350)
    lbPublicIP.config(font=("Calibri", 12, 'bold'), fg='black')
    lbPublicIP.configure(state="disabled")

    entryPublicIP = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file5_path)
    entryPublicIP.place(x=250, y=350, width=200, height=25)
    entryPublicIP.configure(state="disabled")
    entryPublicIP.delete(0, 'end')

    buttonRun = tkinter.Button(buttonsFn.top, text="Run", command= securityCorpRun)
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
    buttonsFn.top.configure(bg='white')
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
    fileNameToRemove = buttonsFn.file1_path.get().split('/')[-1]
    pathToSave = buttonsFn.file1_path.get().replace(fileNameToRemove, "")
    Build_APN_DB.APNDB(buttonsFn.file1_path.get(),buttonsFn.tkvar1.get(),pathToSave,buttonsFn.file2_path.get(),buttonsFn.file3_path.get())


def UpdateDropDownFromExcelForAPNDB():
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

    MTXMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar1, *MTXs)
    MTXMenu.place(x=250, y=200)
    MTXMenu.config(height=1, width=4, fg='black')
    buttonsFn.tkvar1.set(MTXs[0])  # set the default option


def openBuildDBMenu():
    # define font
    myFont = font.Font(family='Calibri', size=12)
    myFont2 = font.Font(family='Calibri', size=15)

    # Imgname2 = tkinter.PhotoImage(file="Vodafone2.png")

    background_label = tkinter.Label(buttonsFn.top)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # background_label.configure(background='red')
    # Define Buttons of the main window

    # 1
    lbExcel = tkinter.Label(buttonsFn.top, text="Select Excel Sheet")
    lbExcel.place(x=100, y=150)
    lbExcel.config(font=("Calibri", 12, 'bold'), fg='black')

    entryExcelPath = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file1_path)
    entryExcelPath.place(x=250, y=150, width=400, height=25)
    entryExcelPath.delete(0, 'end')

    buttonBrowse = tkinter.Button(buttonsFn.top, text="Browse", command=UpdateDropDownFromExcelForAPNDB)
    buttonBrowse.place(x=670, y=145)
    buttonBrowse['font'] = myFont

    lbMTX = tkinter.Label(buttonsFn.top, text="Choose MTX")
    lbMTX.place(x=100, y=200)
    lbMTX.config(font=("Calibri", 12, 'bold'), fg='black')
    MTXMenu = tkinter.OptionMenu(buttonsFn.top, buttonsFn.tkvar1, [""])

    MTXMenu.place(x=250, y=200)
    MTXMenu.config(height=1, width=4, fg='black')
    buttonsFn.tkvar1.set("")  # set the default option

    lbUsername = tkinter.Label(buttonsFn.top, text="Username")
    lbUsername.place(x=100, y=250)
    lbUsername.config(font=("Calibri", 12, 'bold'), fg='black')

    entryUsername = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
    entryUsername.place(x=250, y=250, width=120, height=25)
    entryUsername.delete(0, 'end')

    lbPassword = tkinter.Label(buttonsFn.top, text="Password")
    lbPassword.place(x=100, y=300)
    lbPassword.config(font=("Calibri", 12, 'bold'), fg='black')

    entryPassword = tkinter.Entry(buttonsFn.top, show="*",textvariable=buttonsFn.file3_path)
    entryPassword.place(x=250, y=300, width=120, height=25)
    entryPassword.delete(0, 'end')

    buttonRun = tkinter.Button(buttonsFn.top, text="Run", command=BuildDBRun)
    buttonRun.place(x=330, y=350)
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
    buttonsFn.top.geometry("800x420")  # Width x Height
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

    lbSectionName= tkinter.Label(buttonsFn.top, text="APN Index :")
    lbSectionName.place(x=150, y=205)
    lbSectionName.config(font=("Calibri", 16, 'bold'), fg='black')

    lbFrom= tkinter.Label(buttonsFn.top, text="From")
    lbFrom.place(x=150, y=250)
    lbFrom.config(font=("Calibri", 12, 'bold'), fg='black')

    entryFrom = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file1_path)
    entryFrom.place(x=250, y=250, width=120, height=25)
    entryFrom.delete(0, 'end')

    lbTo = tkinter.Label(buttonsFn.top, text="To")
    lbTo.place(x=400, y=250)
    lbTo.config(font=("Calibri", 12, 'bold'), fg='black')

    entryTo = tkinter.Entry(buttonsFn.top, textvariable=buttonsFn.file2_path)
    entryTo.place(x=450, y=250, width=120, height=25)
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
    buttonCorpAPNAudit.place(x=100, y=100)
    buttonCorpAPNAudit.config(height=3, width=20, fg='black', background='white')
    buttonCorpAPNAudit['font'] = myFont
    # 2
    buttonIDNSAudit = tkinter.Button(buttonsFn.top, text="iDNS Audit")
    buttonIDNSAudit.place(x=100, y=220)
    buttonIDNSAudit.config(height=3, width=20, fg='black', background='white')
    buttonIDNSAudit['font'] = myFont
    # 3
    buttoneDNSAudit = tkinter.Button(buttonsFn.top, text="eDNS Audit")
    buttoneDNSAudit.place(x=350, y=100)
    buttoneDNSAudit.config(height=3, width=20, fg='black', background='white')
    buttoneDNSAudit['font'] = myFont
    # 4
    buttonSGSNAudit = tkinter.Button(buttonsFn.top, text="SGSN Audit")
    buttonSGSNAudit.place(x=350, y=220)
    buttonSGSNAudit.config(height=3, width=20, fg='black', background='white')
    buttonSGSNAudit['font'] = myFont
    # 5
    buttonGGSNAudit = tkinter.Button(buttonsFn.top, text="GGSN Audit")
    buttonGGSNAudit.place(x=100, y=340)
    buttonGGSNAudit.config(height=3, width=20, fg='black', background='white')
    buttonGGSNAudit['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openDataMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=1, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("700x500")  # Width x Height
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
    button_Test_APN.place(x=350, y=220)
    button_Test_APN.config(height=3, width=20,  fg='black', background = 'white')
    button_Test_APN['font'] = myFont

    # 3
    button_IP_Pool_Expansion = tkinter.Button(buttonsFn.top, text="IP Pool Expansion", command=openIpPoolExpansionMenu)
    button_IP_Pool_Expansion.place(x=350 ,y=100)
    button_IP_Pool_Expansion.config(height=3, width=20, fg='black', background='white')
    button_IP_Pool_Expansion['font'] = myFont

    # 4
    button_Corporate_APN_DB = tkinter.Button(buttonsFn.top, text="Packet Audit", command=openPacketAuditMenu)
    button_Corporate_APN_DB.place(x=100, y=220)
    button_Corporate_APN_DB.config(height=3, width=20, fg='black', background='white')
    button_Corporate_APN_DB['font'] = myFont

    # 5
    button_Capacity_Moves = tkinter.Button(buttonsFn.top, text="Capacity Moves")
    button_Capacity_Moves.place(x=100, y=340)
    button_Capacity_Moves.config(height=3, width=20, fg='black', background='white')
    button_Capacity_Moves['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openMainMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=1, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("700x500")  # Width x Height
    buttonsFn.top.title("Packet Tool")
    #top.configure(background = 'sky blue')

    buttonsFn.top.mainloop()

def openVoiceAuditMenu():
    # Main menu
    # define font
    myFont = font.Font(family='Calibri', size=15)

    Imgname = tkinter.PhotoImage(file="Vodafone.png")
    background_label = tkinter.Label(buttonsFn.top, image=Imgname)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Define Buttons of the main window
    # 1
    buttonBSCAudit = tkinter.Button(buttonsFn.top, text="BSC Audit")
    buttonBSCAudit.place(x=100, y=100)
    buttonBSCAudit.config(height=3, width=20, fg='black', background='white')
    buttonBSCAudit['font'] = myFont
    # 2
    buttonRNCAudit = tkinter.Button(buttonsFn.top, text="RNC Audit")
    buttonRNCAudit.place(x=100, y=220)
    buttonRNCAudit.config(height=3, width=20, fg='black', background='white')
    buttonRNCAudit['font'] = myFont
    # 3
    buttonMSCAudit = tkinter.Button(buttonsFn.top, text="MSC Audit")
    buttonMSCAudit.place(x=350, y=100)
    buttonMSCAudit.config(height=3, width=20, fg='black', background='white')
    buttonMSCAudit['font'] = myFont
    # 4
    buttonIMSAudit = tkinter.Button(buttonsFn.top, text="IMS Audit")
    buttonIMSAudit.place(x=350, y=220)
    buttonIMSAudit.config(height=3, width=20, fg='black', background='white')
    buttonIMSAudit['font'] = myFont
    # 5
    buttonIPSTPAudit = tkinter.Button(buttonsFn.top, text="IPSTP Audit")
    buttonIPSTPAudit.place(x=100, y=340)
    buttonIPSTPAudit.config(height=3, width=20, fg='black', background='white')
    buttonIPSTPAudit['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openVoiceMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=1, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("700x500")  # Width x Height
    buttonsFn.top.title("Voice Audit")
    # top.configure(background = 'sky blue')
    buttonsFn.top.mainloop()


def openVoiceMenu():

    # Main menu
    # define font
    myFont = font.Font(family='Calibri', size= 15)

    Imgname = tkinter.PhotoImage(file="Vodafone.png")
    background_labe = tkinter.Label(buttonsFn.top,image=Imgname)
    background_labe.place(x=0, y=0, relwidth=1, relheight=1)

    # Define Buttons of the main window
    # 1
    button_Short_Codes = tkinter.Button(buttonsFn.top, text="Short Codes")
    button_Short_Codes.place(x=100, y=100)
    button_Short_Codes.config(height=3, width=20,  fg='black', background = 'white')
    button_Short_Codes['font'] = myFont
    # 2
    button_Interconnect = tkinter.Button(buttonsFn.top, text="Interconnect")
    button_Interconnect.place(x=100, y=220)
    button_Interconnect.config(height=3, width=20,  fg='black', background = 'white')
    button_Interconnect['font'] = myFont

    # 3
    button_MGW = tkinter.Button(buttonsFn.top, text="MGW")
    button_MGW.place(x=350 ,y=100)
    button_MGW.config(height=3, width=20, fg='black', background='white')
    button_MGW['font'] = myFont

    # 4
    button_B_Analysis = tkinter.Button(buttonsFn.top, text="B no. Analysis")
    button_B_Analysis.place(x=350, y=220)
    button_B_Analysis.config(height=3, width=20, fg='black', background='white')
    button_B_Analysis['font'] = myFont

    # 5
    button_Voice_Audit = tkinter.Button(buttonsFn.top, text="Voice Audit",command=openVoiceAuditMenu)
    button_Voice_Audit.place(x=100, y=340)
    button_Voice_Audit.config(height=3, width=20, fg='black', background='white')
    button_Voice_Audit['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openMainMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=1, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("700x500")  # Width x Height
    buttonsFn.top.title("Voice Tool")
    #top.configure(background = 'sky blue')

    buttonsFn.top.mainloop()


def openSecurityAudit():
    # Main menu
    # define font
    myFont = font.Font(family='Calibri', size=15)

    Imgname = tkinter.PhotoImage(file="Vodafone.png")
    background_label = tkinter.Label(buttonsFn.top, image=Imgname)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Define Buttons of the main window
    # 1
    buttonFWPolicies = tkinter.Button(buttonsFn.top, text="FW Policies")
    buttonFWPolicies.place(x=170, y=190)
    buttonFWPolicies.config(height=3, width=20, fg='black', background='white')
    buttonFWPolicies['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openSecurityMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=1, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("550x450")  # Width x Height
    buttonsFn.top.title("Security Audit")
    # top.configure(background = 'sky blue')
    buttonsFn.top.mainloop()


def openSecurityMenu():

    # Main menu
    # define font
    myFont = font.Font(family='Calibri', size= 15)

    Imgname = tkinter.PhotoImage(file="Vodafone.png")
    background_labe = tkinter.Label(buttonsFn.top,image=Imgname)
    background_labe.place(x=0, y=0, relwidth=1, relheight=1)

    # Define Buttons of the main window
    # 1
    button_Test_APN = tkinter.Button(buttonsFn.top, text="Test APNs")
    button_Test_APN.place(x=100, y=100)
    button_Test_APN.config(height=3, width=20,  fg='black', background = 'white')
    button_Test_APN['font'] = myFont
    # 2
    button_Users_Cleanup = tkinter.Button(buttonsFn.top, text="Users Cleanup")
    button_Users_Cleanup.place(x=100, y=220)
    button_Users_Cleanup.config(height=3, width=20,  fg='black', background = 'white')
    button_Users_Cleanup['font'] = myFont

    # 3
    button_IPs_Blocking = tkinter.Button(buttonsFn.top, text="IPs Blocking")
    button_IPs_Blocking.place(x=350 ,y=100)
    button_IPs_Blocking.config(height=3, width=20, fg='black', background='white')
    button_IPs_Blocking['font'] = myFont

    # 4
    button_IP_Pool_Expansion = tkinter.Button(buttonsFn.top, text="IP Pool Expansion")
    button_IP_Pool_Expansion.place(x=350, y=220)
    button_IP_Pool_Expansion.config(height=3, width=20, fg='black', background='white')
    button_IP_Pool_Expansion['font'] = myFont


    # 5
    button_FW_Policies = tkinter.Button(buttonsFn.top, text="Security Audit",command=openSecurityAudit)
    button_FW_Policies.place(x=100, y=340)
    button_FW_Policies.config(height=3, width=20, fg='black', background='white')
    button_FW_Policies['font'] = myFont

    buttonBack = tkinter.Button(buttonsFn.top, text="Back", command=openMainMenu)
    buttonBack.place(x=20, y=20)
    buttonBack.config(height=1, width=8, fg='black', bg='white')
    buttonBack['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("700x500")  # Width x Height
    buttonsFn.top.title("Security Tool")
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
    buttonVoiceDomain = tkinter.Button(buttonsFn.top, text="Voice Domain",command=openVoiceMenu)
    buttonVoiceDomain.place(x=170, y=70)
    buttonVoiceDomain.config(height=3, width=20,  fg='black', background = 'white')
    buttonVoiceDomain['font'] = myFont
    # 2
    buttonDataDomain = tkinter.Button(buttonsFn.top, text="Data Domain", command=openDataMenu)
    buttonDataDomain.place(x=170, y=180)
    buttonDataDomain.config(height=3, width=20,  fg='black', background = 'white')
    buttonDataDomain['font'] = myFont

    # 3
    buttonSecurity = tkinter.Button(buttonsFn.top, text="Security", command=openSecurityMenu)
    buttonSecurity.place(x=170, y=290)
    buttonSecurity.config(height=3, width=20, fg='black', background='white')
    buttonSecurity['font'] = myFont

    # Define the size of the main window
    buttonsFn.top.geometry("550x450")  # Width x Height
    buttonsFn.top.title("CN Planning & Configuration App")
    #top.configure(background = 'sky blue')

    buttonsFn.top.mainloop()

openMainMenu()
