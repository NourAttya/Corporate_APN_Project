def Sec3GWIC_Script (APN_Name, Sim_Range, IPs ):


    script = open(APN_Name + "_Script.txt", "w")
    script.write('On PIX firewall'  + ':\n') #Start From Here
    script.write('---------------' + '\n')
    script.write('set address "Corp_GPRS" " ' + APN_Name + 'APN"  ' + Sim_Range + '\n')
    for i in range(len(IPs)):
        script.write('set address "Outside" "' +APN_Name+ ' APN Loopback'+str(i) +IPs+ '\n')

    script.write('set policy top name "' +APN_Name+ 'APN" from "Corp_GPRS" to "Outside" "' + APN_Name+ 'APN" "' + APN_Name+ 'APN Loopback" "ANY" permit log' '\n')
    script.write('set policy top name "' +APN_Name+ 'APN" from "Outside" to "Corp_GPRS" "'+ APN_Name+'APN Loopback" "' + APN_Name+ 'APN "ANY" permit log' '\n')
    script.write('set route ' + Sim_Range+ 'interface ethernet3/1 gateway 10.254.14.3' '\n')
    for i in range(len(IPs)):

        script.write('set route ' +IPs+ 'interface ethernet3/2 gateway 192.168.151.200' '\n')
    script.write('save' '\n')
    script.write('---------------------------------------------------------------\n')
    script.write('\n \n')
    script.write('Rollback\n')
    script.write('=========\n \n')
    script.write('PIX firewall\n')
    script.write('=========\n')
    script.write('\n \n')
    script.write('unset address "Corp_GPRS" " ' + APN_Name + 'APN"' + Sim_Range + '\n')
    script.write('unset address "Outside" " ' + APN_Name + 'APN Loopback"'+ Loopback_IP+ '\n')
    script.write('unset policy id \n')
    script.write('unset policy id \n')
    script.write('unset route ' +Sim_Range+ 'interface ethernet3/1 gateway 10.254.14.3 \n')
    script.write('unset route ' +Loopback_IP+ 'interface ethernet3/2 gateway 192.168.151.200 \n')
    script.close()
    print('Nour')
