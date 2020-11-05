from Whitelisting import Whitelisting_script

def Whitelisting(APNname,IPs,P2Ps,Domains,MTX,SecMTX,Priority,pathToSave,DDL, PDL, HDL):


    IP = IPs.split(",")
    P2Ps = P2Ps.split(",")

    Domains = Domains.split(",")
    print(Domains)
    #URLs = URLs.split(",")

    Whitelisting_script.Whitelisting_script(APNname,IP,Domains,MTX,SecMTX,Priority,pathToSave,DDL,PDL,HDL)
Whitelisting("TestAPN9", "10.0.0.0/26, 100.100.10.0/20","google.com, yahoo.com", "google.com, yahoo.com", "HQ", "ZHR", "1600", "D://EPC//Automation//Corporate_APN_Project//", "Domain, IP", "", "")





