from Whitelisting import Whitelisting_script

def Whitelisting(APNname,IPs,URLs,P2Ps,Domains,MTX,SecMTX,Priority,RG,pathToSave):



    IPs = IPs.split(",")
    P2Ps = P2Ps.split(",")
    Domains = Domains.split(",")
    URLs = URLs.split(",")




    Whitelisting_script.Whitelisting_script(APNname,IPs,URLs,Domains,P2Ps,MTX,SecMTX,Priority,RG,pathToSave)
