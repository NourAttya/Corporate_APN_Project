
def Cisco_Script (Contextname,Ippoolarray,netmaskpoolarray,Subnetnames,MTX,SorD,pathToSave,TypeOfAPN,APNname):

    script = open(pathToSave + Contextname + "_Script.txt", "a")
    script.write('On' + MTX + '-GGSN'  + ':\n')
    script.write(' Configure\n')
    script.write( Contextname + '\n')

    if (TypeOfAPN == 'PC Connectivity'):
        if (SorD == "Static"):
            for i in range (len(Ippoolarray)):
                script.write(
                    'ip pool ' + Subnetnames[i]  + str(Ippoolarray[i]) + " " + str(
                    netmaskpoolarray[i]) + ' static group-name ' + APNname + '_pool advertise-if-used vrf' + APNname+'_vrf \n')
        else:
             for i in range(len(Ippoolarray)):
                script.write(
                'ip pool ' + Subnetnames[i]  + str(Ippoolarray[i]) + " " + str(
                    netmaskpoolarray[i]) + ' private 0 group-name ' + APNname + '_pool advertise-if-used vrf' + APNname+'_vrf\n')

    elif (TypeOfAPN == 'Sim2Sim'):
        for i in range(len(Ippoolarray)):
            script.write(
                'ip pool ' + Subnetnames[i] + str(Ippoolarray[i]) + " " + str(
                    netmaskpoolarray[i]) + ' static group-name ' + APNname + '_pool advertise-if-used vrf' + APNname+'_vrf \n')

    elif (TypeOfAPN == '3G WIC'):
        for i in range (len(Ippoolarray)):
                script.write(
                    'ip pool ' + Subnetnames[i] + str(Ippoolarray[i]) + " " + str(
                        netmaskpoolarray[i]) + ' static group-name ' + APNname + '_pool advertise-if-used \n')

    elif (TypeOfAPN == 'Commerical_main_APN'):
        for i in range(len(Ippoolarray)):
            script.write(
                'ip pool ' + Subnetnames[i] + str(Ippoolarray[i]) + " " + str(
                    netmaskpoolarray[i]) + ' private 0 group-name internet advertise-if-used address-hold-timer 60 \n')

    elif (TypeOfAPN == 'Internet'):
        for i in range (len(Ippoolarray)):
                script.write(
                 'ip pool ' + Subnetnames[i]  + str(Ippoolarray[i]) + " " + str(
                     netmaskpoolarray[i]) + ' private 0 group-name ' + APNname + '_pool advertise-if-used \n')

    else :
        return
    script.write('  exit\n')
    script.write('    end\n')