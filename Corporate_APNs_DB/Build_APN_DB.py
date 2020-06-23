
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
    with open(configPath) as f:
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




    print("APNName",APNName)
    print("contextName",contextName)
    print("VRF",VRF)
    print("interface",interface)







getAllAPNS("D:\\Automation Team\\Corporate APN Project\\config files\\TG2 GGSN 21 6 2020")