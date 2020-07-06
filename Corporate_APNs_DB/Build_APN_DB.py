
import os

def getAllAPNS(configPath):
#input : GGSN Configuration file
#output : 4 Lists with the same length
#           APNName -> (list of strings)all apn names in the config file,
#           contextName -> (list of strings)the context name corresponding to apn name,
#           VRF -> (list of 0 or 1) for each apn if there's vrf configured to it vrf will be =1 else vrf =0
#           interface -> (list of 0 or 1) for each apn if there's interface configured to it interface will be =1 else vrf =0
    APNName=[]
    contextName=[]
    VRF=[]
    interface=[]
    for filename in os.listdir(configPath):
        fullnameConfigFile = os.path.join(configPath, filename)
        with open(fullnameConfigFile) as f:
            reading = 0
            line = f.readline()
            while (line):
                line = f.readline()
                line=line.lstrip()
                if (line.startswith("apn ") and not line.startswith("apn schema")):
                    reading=1
                    if(len(APNName)!=len(contextName)):
                        contextName.append(None)

                    VRF.append(0)
                    interface.append(0)
                    APNName.append(line.split(" ")[1].replace("\n",""))
                    continue
                if(reading==1):
                    if(line.startswith("ip context-name")):
                        contextName.append(line.split(" ")[2].replace("\n",""))
                    if("vrf" in line):
                        name=line.split(" ")[2]
                        check = [name.find(i) for i in APNName]
                        if(check.count(0)!=0):
                            index=check.index(0)
                            VRF[index]=1
                    if ("interface" in line):
                        name = line.split(" ")[1]
                        check = [name.find(i) for i in APNName]
                        if (check.count(0) != 0):
                            for i in range(len(check)):
                                if(check[i]==0):
                                    interface[i] = 1
        print("APNName",len(APNName))
        print("contextName",len(contextName))
        print("VRF",len(VRF))
        print("interface",len(interface))


    return APNName,contextName,VRF,interface


def getAPNType(APNName,contextName,VRF,interface):
    APNType=[]

    for i in range(len(APNName)):
        if(VRF[i]==1 and interface[i]==0):
            APNType.append("sim2sim")
        elif(VRF[i]==1 and interface[i]==1):
            APNType.append("PC Connectivity")
        elif(VRF[i]==0 and contextName[i]=="Gi-Corp"): #To be checked if there is a VRF for 3WIC or not
            APNType.append("3G WIC")
        elif (VRF[i]==0 and contextName[i]=="VAS-Corp"):
            APNType.append("Internet")
        else:
            APNType.append(str(contextName[i])+" "+str(VRF[i])+" "+str(interface[i]))

    return APNType


def writeInCSV(APNName,APNType,pathToSave):

    with open(pathToSave + '\\Corporate APNs' + '.csv', 'w') as out_file:
        out_file.write('{0},{1}\n'.format("APN Name", "APN Type"))
        for i in range(len(APNName)):
            out_file.write('{0},{1}\n'.format(APNName[i],APNType[i]))


def APNDB(configPath):
    pathToSave=configPath
    APNName, contextName, VRF, interface=getAllAPNS(configPath)
    APNType=getAPNType(APNName,contextName,VRF,interface)
    writeInCSV(APNName,APNType,pathToSave)

# # getAllAPNS("D:\\Automation Team\\Corporate APN Project\\config files\\TG2 GGSN 21 6 2020")
# # # writeInCSV(["Test1","Test2","Test3"],["3GWIc","PC Connectivity","Internet"],"D:\\Automation Team\\Corporate APN Project\\")
# # APNDB("D:\\Automation Team\\Corporate APN Project\\config files\\TG2 GGSN 21 6 2020","D:\\Automation Team\\Corporate APN Project\\")
#Nour Attya