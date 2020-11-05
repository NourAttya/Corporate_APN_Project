import paramiko
import xlrd
import  ipaddress
def Log_testAPN(host, username, password, APNname):

    port = 22
    command = "show config apn " +APNname

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if not ssh.connect(host, port, username, password):
        print("SSH session failed on login.")
    else:
        print("SSH session login successful")

    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    return lines

#if (lines[0] == "Failure: No matching configuration data\n"):
def Test_APN(APNname, pathToSave, MTX, MTXNum, IP, SorD):
    net = ipaddress.ip_network(IP, False)
    netmask = net.netmask
    IP = IP.split("/")[0]

    script = open(pathToSave + APNname + "_Script.txt", "w")
    script.write(MTX + '-GGSN' + str(MTXNum) + ':\n')
    script.write('-----------\n')
    script.write('save configuration /flash/configfiles/Before_' + APNname + '.cfg -redundant\n')
    script.write('config\n')
    script.write(' context aaa \n')
    script.write('   apn ' + APNname + '\n')
    script.write('   accounting-mode none\n')
    script.write('      gtpp group PGW' + str(MTXNum) + ' accounting-context gn\n')
    script.write('      aaa group Corporate-radgom \n')
    script.write('      dns primary 62.240.110.197\n')
    script.write('      dns secondary 62.240.110.198\n')
    script.write('      ip hide-service-address\n')
    script.write('      ip address alloc-method local\n')
    script.write('      ip access-group Corporate.vodafone.net-acl.in in\n')
    script.write('      ip access-group Corporate.vodafone.net-acl.out out \n')
    script.write('      ip source-violation ignore \n')
    script.write('      mediation-device no-interims\n')
    script.write('      ip context-name VAS-Corp\n')
    script.write('      ip address pool name ' + APNname + '_pool\n')
    script.write('      active-charging rulebase corporate-mbc-rs  \n')
    script.write('      ims-auth-service corporate-mbc-pool\n')
    script.write('      credit-control-group corporate-mbc-cc\n')
    script.write('   exit\n')
    script.write('context Gi-DPI \n')
    if (SorD == "Static"):
        script.write('    ip pool ' + APNname + '_pool.0 ' + str(IP) + " " + str(netmask) + ' static group-name ' + APNname + '_pool advertise-if-used\n')
    else:
        script.write('ip pool ' + APNname + '_pool.0 ' + str(IP) + " " + str(netmask) + ' private 0 group-name ' + APNname + '_pool advertise-if-used \n')
    script.write('  exit\n')
    script.write('    end\n')
    script.write('save configuration /flash/configfiles/' + MTX + '-GGSN-running.cfg -redundant\n')

    script.write('-----------------------------------------------\n')
    script.write('Add the below entries On All IDNSs:\n')
    script.write('----------------------------------------\n')
    script.write('\n \n')
    script.write('delete naptrrecord ' + APNname + '.apn.epc.mnc002.mcc602.3gppnetwork.org.\n')
    script.write('create naptrrecord ' + APNname + '.apn.epc.mnc002.mcc602.3gppnetwork.org. -set order=100;preference=10;flags=a;service=x-3gpp-pgw:x-s5-gtp:x-gn;replacement=topoff.pgws5gn.' + MTX.lower() + 'gw.nodes.epc.mnc002.mcc602.3gppnetwork.org.\n')
    script.write('\n')
    script.write('update dnsserver -rebuild=true\n')
    script.write('\n')
    script.write('Rollback on All iDNSs\n')
    script.write('======================\n')
    script.write('\n')
    script.write('delete naptrrecord ' + APNname + '.apn.epc.mnc002.mcc602.3gppnetwork.org.\n')
    script.write('\n')
    script.write('update dnsserver -rebuild=true\n')
    script.close()


#Test_APN("testapn2", "D:/EPC/Automation/Corporate APNs App/", "HQ", "05", "10.0.0.0/28", "Static","255.255.255.248")






