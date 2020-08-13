def Blocking_IPs_MI (BlockingIP):
    script = open(BlockingIP + " MI_Script.txt", "w")
    script.write('HQ-GI: \n')
    script.write('set security zones security-zone Internet address-book address Suspected_'+BlockingIP+' '+BlockingIP+'\n')
    script.write('set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_'+BlockingIP+'\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('HQ-2nd Leg Gi: \n')
    script.write(
        'set security zones security-zone Internet address-book address Suspected_' + BlockingIP + ' ' + BlockingIP + '\n')
    script.write(
        'set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_' + BlockingIP + '\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('MKT-Gi: \n')
    script.write(
        'set security zones security-zone Internet address-book address Suspected_' + BlockingIP + ' ' + BlockingIP + '\n')
    script.write(
        'set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_' + BlockingIP + '\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('MNS-Gi: \n')
    script.write(
        'set security zones security-zone Internet address-book address Suspected_' + BlockingIP + ' ' + BlockingIP + '\n')
    script.write(
        'set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_' + BlockingIP + '\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('RMD-2nd GI: \n')
    script.write(
        'set security zones security-zone Internet address-book address Suspected_' + BlockingIP + ' ' + BlockingIP + '\n')
    script.write(
        'set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_' + BlockingIP + '\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('RMD-GI: \n')
    script.write(
        'set security zones security-zone Internet address-book address Suspected_' + BlockingIP + ' ' + BlockingIP + '\n')
    script.write(
        'set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_' + BlockingIP + '\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('Alex-GI: \n')
    script.write(
        'set security zones security-zone Internet address-book address Suspected_' + BlockingIP + ' ' + BlockingIP + '\n')
    script.write(
        'set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_' + BlockingIP + '\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('BS-GI: \n')
    script.write(
        'set security zones security-zone Internet address-book address Suspected_' + BlockingIP + ' ' + BlockingIP + '\n')
    script.write(
        'set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_' + BlockingIP + '\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('BS 2nd Leg-GI: \n')
    script.write(
        'set security zones security-zone Internet address-book address Suspected_' + BlockingIP + ' ' + BlockingIP + '\n')
    script.write(
        'set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_' + BlockingIP + '\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('CA4-GI: \n')
    script.write(
        'set security zones security-zone Internet address-book address Suspected_' + BlockingIP + ' ' + BlockingIP + '\n')
    script.write(
        'set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_' + BlockingIP + '\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('CA5-GI: \n')
    script.write(
        'set security zones security-zone Internet address-book address Suspected_' + BlockingIP + ' ' + BlockingIP + '\n')
    script.write(
        'set security zones security-zone Internet address-book address-set Suspected_IPs_1 address Suspected_' + BlockingIP + '\n')
    script.write('--------------------------------------------------------------------------------- \n \n')

    script.write('################################################################################### \n \n')


