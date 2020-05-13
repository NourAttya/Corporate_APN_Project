
def WIc3GScript(APNname,IP,netmask,MTX,MTXNum,SecMTX,secMTXnum,SorD,pathToSave):
    # open output text file
    script = open(pathToSave + APNname + "_Script.txt", "a")
    script.write(MTX+'-GGSN'+str(MTXNum)+':\n')
    script.write('-----------\n')
    script.write('save configuration /flash/configfiles/Before_'+APNname+' -redundant\n')
    script.write('config\n')
    script.write(' context aaa \n')
    script.write('   apn '+APNname+'\n')
    script.write('      accounting-mode none\n')
    script.write('      gtpp group PGW'+str(MTXNum)+' accounting-context gn\n')
    script.write('      ip hide-service-address\n')
    script.write('      aaa group Corporate-radgom \n')
    if(SorD=="Static"):
        script.write('      ip address alloc-method no-dynamic allow-user-specified\n')
    else:
        script.write('     ip address alloc-method local\n')
    script.write('      ip access-group Corporate.vodafone.net-acl.in in\n')
    script.write('      ip access-group Corporate.vodafone.net-acl.out out\n')
    script.write('      mediation-device no-interims\n ')
    script.write('      ip context-name Gi-Corp\n')
    script.write('      ip address pool name '+APNname+'_pool\n')
    script.write('      active-charging rulebase corporate-mbc-rs\n')
    script.write('      ims-auth-service corporate-mbc-pool\n')
    script.write('      credit-control-group corporate-mbc-cc\n')
    script.write('     exit\n')
    script.write('   context Gi-Corp\n')
    if (SorD == "Static"):
      script.write(
        '      ip pool '+APNname+'_pool.0 '+str(IP)+" "+str(netmask)+' static group-name '+APNname+'_pool advertise-if-used\n')
    else:
        script.write(
            'ip pool '+APNname+'_pool.0 '+str(IP)+" "+str(netmask)+' private 0 group-name '+APNname+'_pool advertise-if-used \n')
    script.write('     exit\n')
    script.write('    end\n')
    script.write('save configuration /flash/configfiles/'+MTX+'-GGSN-running -redundant\n')
    script.write('-----------------------------------------------\n')
    script.write(SecMTX+'-GGSN-'+str(secMTXnum)+':\n')
    script.write('---------\n')
    script.write('save configuration /flash/configfiles/Before_'+APNname+' -redundant\n')
    script.write('config\n')
    script.write(' context aaa\n')
    script.write('   apn '+APNname+' \n')
    script.write('      accounting-mode none\n')
    script.write('      gtpp group PGW'+str(secMTXnum)+' accounting-context gn\n')
    script.write('      ip hide-service-address\n')
    script.write('      aaa group Corporate-radgom\n')
    if (SorD == "Static"):
        script.write('      ip address alloc-method no-dynamic allow-user-specified\n')
    else:
        script.write('     ip address alloc-method local\n')
    script.write('      ip access-group Corporate.vodafone.net-acl.in in\n')
    script.write('      ip access-group Corporate.vodafone.net-acl.out out\n')
    script.write('      mediation-device no-interims \n')
    script.write('      ip context-name Gi-Corp\n')
    script.write('      ip address pool name '+APNname+'_pool\n')
    script.write('      active-charging rulebase corporate-mbc-rs\n')
    script.write('      ims-auth-service corporate-mbc-pool\n')
    script.write('      credit-control-group corporate-mbc-cc\n')
    script.write('     exit\n')
    script.write('\n')
    script.write('  context Gi-Corp\n')
    if (SorD == "Static"):
      script.write(
        '      ip pool '+APNname+'_pool.0 '+str(IP)+" "+str(netmask)+' static group-name '+APNname+'_pool advertise-if-used\n')
    else:
        script.write(
            'ip pool '+APNname+'_pool.0 '+str(IP)+" "+str(netmask)+' private 0 group-name '+APNname+'_pool advertise-if-used \n')
    script.write('     exit\n')
    script.write('    end  \n')
    script.write('\n')
    script.write('save configuration /flash/configfiles/'+SecMTX+'-GGSN-config -redundant\n')
    script.write('---------------------------------------------------------------\n')
    script.write('Add the below entries On All IDNSs:\n')
    script.write('----------------------------------------\n')
    script.write(
        'create naptrrecord '+APNname+'.apn.epc.mnc002.mcc602.3gppnetwork.org. -set order=100;preference=10;flags=a;service=x-3gpp-pgw:x-s5-gtp:x-gn;replacement=topoff.pgws5gn.'+MTX.lower()+'gw.nodes.epc.mnc002.mcc602.3gppnetwork.org.\n')

    script.close()

