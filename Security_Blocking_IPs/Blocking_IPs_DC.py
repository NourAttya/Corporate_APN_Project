def Blocking_IPs_DC (BlockingIP):
    script = open(BlockingIP + " DC_Script.txt", "w")
    script.write('HQ-ON: \n')
    script.write('------ \n \n')
    script.write('set address "Internet" "Suspected_' +BlockingIP+ '" '+BlockingIP+' 255.255.255.255\n')
    script.write('set group address "Internet" "Suspected_IPs_1" add "Suspected_'+BlockingIP+'" \n')
    script.write(' \n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('RMD-ON: \n')
    script.write('------ \n \n')
    script.write('set address "Internet" "Suspected_' + BlockingIP + '" ' + BlockingIP + ' 255.255.255.255 \n')
    script.write('set group address "Internet" "Suspected_IPs_1" add "Suspected_' + BlockingIP + '" \n')
    script.write(' \n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('################################################################################### \n \n')

    script.write('ROLLBACK: \n')
    script.write('-------- \n \n')
    script.write('HQ-ON: \n')
    script.write('------ \n \n')
    script.write('unset address "Internet" "Suspected_' + BlockingIP + '" ' + BlockingIP + ' 255.255.255.255 \n')
    script.write('unset group address "Internet" "Suspected_IPs_1" remove "Suspected_' + BlockingIP + '" \n')
    script.write(' \n')
    script.write('--------------------------------------------------------------------------------- \n \n')
    script.write('--------------------------------------------------------------------------------- \n \n')