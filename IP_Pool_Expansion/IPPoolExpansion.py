import ipaddress
from IP_Pool_Expansion import Cisco_Script



def IPPoolExpansionConfig(Contextname,IPpools,Subnetnames,MTX,SorD,vendorname,TypeOfAPN,APNname,pathToSave):

   ##For loop for IP in one array
    print(IPpools)
    #resolving IP(getting netmask)
    netmaskpoolarray= []
    Ippoolarray =[]
    for i in range (len (IPpools)) :
        netpool= ipaddress.ip_network(IPpools[i],False)
        netmaskpool=netpool.netmask
        IPpool=IPpools[i].split("/")[0]
        Ippoolarray.append(IPpool)
        netmaskpoolarray.append(netmaskpool)




    #call the fn that will write the script based on the vendor Name
    if(vendorname=='Cisco'):
        Cisco_Script.Cisco_Script(Contextname,Ippoolarray,netmaskpoolarray,Subnetnames,MTX,SorD,pathToSave,TypeOfAPN,APNname)
   # elif(TypeOfAPN=='Huawei_Script'):
    #    Huawei_Script.HuaweiScript(Contextname,Ippoolarray,netmaskpoolarray,Subnetnames,MTX,SorD,pathToSave,TypeOfAPN,APNname)
    else:
        return



IPPoolExpansionConfig("Gi-DPI",["10.0.0.0/26"],["internet.1"],"HQ","Dynamic","Cisco","Commerical_main_APN","internet.vodafone.net","D:/Automation Team/Corporate APN Project/")

#IDNSandAPNConfigCorp("Test", "10.0.0.0/26","HQ","D:/EPC/Automation/Corporate APNs App/Test excel.xlsx","Internet APN","Static","","HQ","")

