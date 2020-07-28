#Nour Attya
import os
import paramiko
import xlrd
def readConfig(IP,username,password):

    host = IP
    port = 22
    command = "show config"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if not ssh.connect(host, port, username, password):
        print("SSH session failed on login.")
    else:
        print("SSH session login successful")

    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    return lines

def is_integer(value: str, *, base: int=10) -> bool:
    try:
        int(value, base=base)
        return True
    except ValueError:
        return False

def getAllAPNS(lines):
#input : configuration lines from node
#output : 4 Lists with the same length
#           APNName -> (list of strings)all apn names in the config file,
#           contextName -> (list of strings)the context name corresponding to apn name,
#           VRF -> (list of 0 or 1) for each apn if there's vrf configured to it vrf will be =1 else vrf =0
#           interface -> (list of 0 or 1) for each apn if there's interface configured to it interface will be =1 else vrf =0
    APNName=[]
    contextName=[]
    poolName=[]
    IPpoolLines=[]
    VRF=[]
    interface=[]
    IPpoolCount=[]
    IPs=[]
    reading=0
    for line in lines:
        line=line.lstrip()
        if (line.startswith("apn ") and not line.startswith("apn schema")):
            reading=1
            if(len(APNName)!=len(contextName)):
                contextName.append(None)
            if(len(APNName)!=len(poolName)):
                print("poolName",None)
                poolName.append(None)
            VRF.append(0)
            interface.append(0)
            IPpoolCount.append(0)
            IPs.append("")
            print("APN Name",line.split(" ")[1].replace("\n",""))
            APNName.append(line.split(" ")[1].replace("\n","").lower())
            continue
        if ("ip pool" in line):
            IPpoolLines.append(line)
        if(reading==1):
            if (line.startswith("ip address pool name")):
                if (len(APNName)>len(poolName)):
                    print("pool Name",line.split(" ")[4].replace("\n", ""))
                    poolName.append(line.split(" ")[4].replace("\n", "").lower())
                else:
                    print(APNName[-1])

            if(line.startswith("ip context-name")):
                contextName.append(line.split(" ")[2].replace("\n",""))
            if ("interface" in line):
                name = line.split(" ")[1].lower()
                check1 = [name.find(i) for i in APNName]
                check2=[name.find(str(i).split("_")[0]) for i in poolName]
                if (check1.count(0) != 0):
                    for i in range(len(check1)):
                        if(check1[i]==0):
                            interface[i] = 1
                        ##Condition to be added using pool name and none condition to be counted
                elif(check2.count(0)!=0):
                    for i in range(len(check2)):
                        if(check2[i]==0):
                            interface[i] = 1


    for line in IPpoolLines:

        if ("ip pool" in line):
            print("line", line)
            toRemove = line.split(" ")[2].split(".")[-1]
            if(is_integer(toRemove)):
                name = line.split(" ")[2].replace("." + toRemove, "").lower()
            else:
                name = line.split(" ")[2].lower()
            print("name", name)
            if (name in poolName):
                index = poolName.index(name)
                IPpoolCount[index] = IPpoolCount[index] + 1
                if(IPpoolCount[index]==1):
                    IPs[index]=IPs[index]+line.split(" ")[3]
                else:
                    IPs[index] = IPs[index] +", "+ line.split(" ")[3]
                if ("vrf" in line):
                    VRF[index] = 1

    print("APNName",len(APNName))
    print("contextName",len(contextName))
    print("VRF",len(VRF))
    print("interface",len(interface))
    print("IPpoolCount",len(IPpoolCount))
    print("poolName",len(poolName))

    return APNName,contextName,VRF,interface,IPpoolCount,poolName,IPs


def getAPNType(APNName,contextName,VRF,interface):
    APNType=[]

    for i in range(len(APNName)):
        if(VRF[i]==1 and interface[i]==0):
            APNType.append("sim2sim")
        elif(VRF[i]==1 and interface[i]==1):
            APNType.append("PC Connectivity")
        elif(VRF[i]==0 and (contextName[i]=="Gi-Corp" or contextName[i]=="Gi-Corp2")):
            APNType.append("3G WIC")
        elif (VRF[i]==0 and contextName[i]=="VAS-Corp"):
            APNType.append("Internet")
        else:
            APNType.append(None)

    return APNType


def writeInCSV(APNName,APNType,contextName,IPpoolCount,MTX,poolName,IPs,pathToSave):

    with open(pathToSave + '\\'+MTX+' Corporate APNs' + '.csv', 'w') as out_file:
        out_file.write('{0},{1},{2},{3},{4},{5},{6}\n'.format("APN Name", "APN Type","Context Name","Number of pools","MTX","Pool Name","IPs"))
        for i in range(len(APNName)):
            # if APNType[i]==None:continue

            out_file.write('{0},{1},{2},{3},{4},{5},{6}\n'.format(APNName[i],APNType[i],contextName[i],IPpoolCount[i],MTX,poolName[i],IPs[i]))
##To write pool name for APN logic

def APNDB(excelPath,MTX,pathToSave,username,password):

    wb = xlrd.open_workbook(excelPath)
    sheet = wb.sheet_by_index(0)
    firstRow = 0
    for j in range(sheet.nrows):
        row = sheet.row_values(j)
        if firstRow == 0:
            for i in range(len(row)):
                if (row[i] == "MTX Name"):
                    MTXindex = i
                elif(row[i]=="IP"):
                    IPindex=i
            firstRow = 1
        else:
            if(row[MTXindex]==MTX):
                IP=row[IPindex]
    print(IP)
    lines=readConfig(IP,username,password)
    # with open("D:\\Automation Team\\Corporate APN Project\\GGSN Config Files\\HQ GGSN 16 7 2020") as f:
    #     lines = f.readlines()
    APNName, contextName, VRF, interface,IPpoolCount,poolName,IPs=getAllAPNS(lines)
    APNType=getAPNType(APNName,contextName,VRF,interface)
    writeInCSV(APNName,APNType,contextName,IPpoolCount,MTX,poolName,IPs,pathToSave)

