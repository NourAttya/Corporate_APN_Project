def IPpoolExpansionScript(IP,netmask,Poolname,MTX,ContextName,SorD,pathToSave,NodeVendor,VRFDest):
    # open output text file
    script = open(pathToSave + "IPpool_Script.txt", "a")

    script.write(MTX + '-GGSN' + ':\n')
    script.write('-----------\n')
    script.write('save configuration /flash/configfiles/Before_' + IPpool + '.cfg -redundant\n')
    script.write('config\n')
    script.write('Context Gi-DPI\n')
    script.write('ip pool ' + Poolname + '\n')
    script.write(
        '      ip pool ' + Poolname + str(IP) + " " + str(netmask) + ' static group-name ' + APNname + '_pool advertise-if-used\n')
    script.write(
        'ip pool ' + Poolname + str(IP) + " " + str(netmask) + ' private 0 group-name ' + APNname + '_pool advertise-if-used vrf ' + APNname + '_vrf \n')