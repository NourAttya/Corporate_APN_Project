def FRScript_3GWicFixed(Sim_Range, pathTosave):
    script = open(pathTosave + Sim_Range + "_Script.txt", "w")
    script.write('FR-SW1(172.30.30.21) & FR-SW2(172.30.30.22) :\n')
    script.write('===========================================\n')
    script.write('ip prefix-list APNs-SIM-IPs permit' +Sim_Range+ ' \n')
    script.write('write \n')
    script.write('\n\n')
    script.write('######################################################\n')
    script.write('\n')
    script.write('Rollback:\n')
    script.write('========= \n')
    script.write('no ip prefix-list APNs-SIM-IPs permit' + Sim_Range + ' \n')
    script.write('write \n')
    script.write('\n\n')
    script.close()