import ipaddress
from Corporate_APNs import Internet_APN_script, PCconnectivity_APN_script, WIc3G_APN_script, Sim2Sim_script
import xlrd



def IDNSandAPNConfigCorp(APNname,IPpool,MTX,XLSXsheet,TypeOfAPN,SorD,VRFDest,SecMTX,IPrange):

    #resolving IP(getting netmask)
    net= ipaddress.ip_network(IPpool)
    netmask=net.netmask
    IP=IPpool.split("/")[0]
    print(netmask)
    print(IP)
    print(SorD)
    print("VRF Dest: ",VRFDest)

    #get path to save output script(in the same folder of excel sheet)
    fileNameToRemove = XLSXsheet.split('/')[-1]
    pathToSave = XLSXsheet.replace(fileNameToRemove, "")

    #open the excel sheet and get the corresponding number to MTX name
    wb = xlrd.open_workbook(XLSXsheet)
    sheet = wb.sheet_by_index(0)
    firstRow = 0
    for j in range(sheet.nrows):
        row = sheet.row_values(j)
        if firstRow == 0:
            for i in range(len(row)):
                if(row[i]=="MTX Name"):
                    MTXindex=i
                elif (row[i] == "MTX Number"):
                    MTXnumindex=i

            firstRow=1
        elif row[MTXindex]==MTX:
            MTXNum=str(row[MTXnumindex])
            MTXNum=MTXNum.replace('=',"")
            MTXNum = MTXNum.replace('"', "")

        if(row[MTXindex]==SecMTX and firstRow!=0):
            secMTXnum=str(row[MTXnumindex])
            secMTXnum = secMTXnum.replace('=', "")
            secMTXnum = secMTXnum.replace('"', "")



    #call the fn that will write the script based on the APN type
    if(TypeOfAPN=='Internet APN'):
        Internet_APN_script.InternetAPNScript(APNname, IP, netmask, MTX, MTXNum, SecMTX, secMTXnum, SorD, pathToSave)
    elif(TypeOfAPN=='PC Connectivity'):
        PCconnectivity_APN_script.PCconnectivityScript(APNname, IP, netmask, MTX, MTXNum, SecMTX, secMTXnum, SorD, pathToSave, VRFDest,IPrange)
    elif(TypeOfAPN== '3G WIc'):
        WIc3G_APN_script.WIc3GScript(APNname, IP, netmask, MTX, MTXNum, SecMTX, secMTXnum, SorD, pathToSave)
    elif (TypeOfAPN == 'Sim2Sim'):
        Sim2Sim_script.Sim2Sim_script(APNname, IP, netmask, MTX, MTXNum, SecMTX, secMTXnum, SorD, pathToSave)
    else:
        return








def IDNSandAPNConfigTest(APNname,IPpool,MTX,XLSXsheet):
    net = ipaddress.ip_network('192.0.2.0/26')
    print(net.netmask)
