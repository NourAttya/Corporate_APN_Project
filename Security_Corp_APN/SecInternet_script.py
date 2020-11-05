

def SecInternet_Script (APN_Name, Sim_Range, Public_IP ):

    script = open(APN_Name + "_Script.txt", "w")
    script.write('On Gi-HQ firewall'  + ':\n')
    script.write('---------------' + '\n')
    script.write('set security nat source pool '+APN_Name+'-APN-Pool address ' +Public_IP+ ' to ' +Public_IP+ '\n')
    script.write('set security nat source rule-set VAS-Corporate-to-Internet rule ' +APN_Name+'-APN match source-address ' +Sim_Range+ '\n')
    script.write('set security nat source rule-set VAS-Corporate-to-Internet rule ' +APN_Name+'-APN match destination-address 0.0.0.0/0 \n')
    script.write('set security nat source rule-set VAS-Corporate-to-Internet rule ' +APN_Name+'-APN then source-nat pool ' +APN_Name+'-APN-Pool \n')
    script.write('set security zones security-zone VAS-Corporate address-book address ' +APN_Name+'-APN ' +Sim_Range+ ' \n')
    script.write(
        'set security policies from-zone VAS-Corporate to-zone Internet policy' +APN_Name+ 'match source-address' +APN_Name+ ' \n')
    script.write(
        'set security policies from-zone VAS-Corporate to-zone Internet policy' +APN_Name+ 'match destination-address any \n')
    script.write(
        'set security policies from-zone VAS-Corporate to-zone Internet policy' +APN_Name+  'match application any \n')
    script.write(
        'set security policies from-zone VAS-Corporate to-zone Internet policy' +APN_Name+ 'then permit  \n')
    script.write('set routing-options static route ' +Sim_Range+ ' next-hop 10.222.7.139  \n')
    script.write(
        'set routing-instances RMD-GI-DNS routing-options static route' + Sim_Range + 'next-table inet.0 \n')
    script.write('commit \n')
    script.write('---------------------------------------------------------------\n')
    script.write(' On RMD-GI:\n')
    script.write('---------------\n')
    script.write('set routing-options static route' +Sim_Range+ ' next-hop 10.5.105.115\n')
    script.write('set routing-instances RMD-GI-DNS-VRF routing-options static route' +Sim_Range+ 'next-table inet.0 \n')
    script.write('---------------------------------------------------------------\n')
    script.write('\n \n')
    script.write('Rollback\n')
    script.write('=========\n \n')
    script.write('On Gi-HQ firewall\n')
    script.write('=========\n')
    script.write('\n \n')
    script.write('delete security nat source pool ' + APN_Name + '-APN-Pool address ' + Public_IP + ' to ' + Public_IP + '\n')
    script.write(
        'delete security nat source rule-set VAS-Corporate-to-Internet rule ' + APN_Name + '\n')
    script.write(
        'delete security zones security-zone VAS-Corporate address-book address ' + APN_Name + '-APN ' + Sim_Range + ' \n')
    script.write(
        'delete security policies from-zone VAS-Corporate to-zone Internet policy '+APN_Name +'\n')
    script.write('delete routing-options static route ' + Sim_Range + ' next-hop 10.222.7.139  \n')
    script.write('---------------------------------------------------------------\n')
    script.write(' On RMD-GI Rollback:\n')
    script.write('---------------\n')
    script.write('delete routing-options static route' + Sim_Range + ' next-hop 10.5.105.115\n')
    script.write(
        'delete routing-instances RMD-GI-DNS-VRF routing-options static route' + Sim_Range + 'next-table inet.0 \n')
    script.write('---------------------------------------------------------------\n')
    script.close()
    print('Nour')
