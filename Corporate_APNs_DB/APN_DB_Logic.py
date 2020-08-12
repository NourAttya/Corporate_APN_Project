import xlrd
def APN_DB_Logic(From, To):
    #APNs = []

    workbook = xlrd.open_workbook("D:\\EPC\\Automation\\Corporate_APN_Project\\TG1 Corporate APNs.xlsx")
    worksheet = workbook.sheet_by_index(0)
    print(worksheet)
    script = open('To be edited '+ "_Script.txt", "w")
    row = worksheet.row_values(From)
    script.write('On ' + row[4] + '-GGSN' + ':\n')

    for j in range (From, To):
        row = worksheet.row_values(j)
        print(row)
        if j == 0: continue
        IPpoolCount = row[3]
        if row[1]=='PC Connectivity':
            script.write(' Configure\n')
            script.write(' context aaa\n')
            script.write(' no ' + row[0] + ' \n')
            script.write(' exit \n')
            script.write(' context' + row[2] + '\n')
            for i in range (1, int(IPpoolCount) +1):
                script.write(' no ip pool_' + str(i) +'\n')
            script.write(' sleep 2 \n')
            script.write(' no ip route 0.0.0.0 0.0.0.0 0.0.0.0 ' + row[0] + 'vrf ' + row[0] +'_vrf\n')
            script.write(' sleep 2 \n')
            script.write(' no interface ' + row[0] + '\n')
            script.write(' sleep 2 \n')
            script.write(' no ip vrf ' + row[0] + '_vrf \n')
            script.write(' sleep 2 \n')
            script.write(' end \n')

        elif row[1]=='3G WIC':
            script.write(' Configure\n')
            script.write(' context aaa\n')
            script.write(' no ' + row[0] + ' \n')
            script.write(' exit \n')
            script.write(' context' + row[2] + '\n')
            for i in range (1, int(IPpoolCount) +1):
                script.write(' no ip pool_' + str(i) +'\n')
            script.write(' end \n')

        elif row[1] == 'Internet':
            script.write(' Configure\n')
            script.write(' context aaa\n')
            script.write(' no ' + row[0] + ' \n')
            script.write(' exit \n')
            script.write(' context' + row[2] + '\n')
            for i in range (1, int(IPpoolCount) +1):
                script.write(' no ip pool_' + str(i) +'\n')
            script.write(' end \n')

        elif row[1] == 'sim2sim':
            script.write(' Configure\n')
            script.write(' context aaa\n')
            script.write(' no ' + row[0] + ' \n')
            script.write(' exit \n')
            script.write(' context' + row[2] + '\n')
            for i in range (1, int(IPpoolCount) +1):
                script.write(' no ip pool_' + str(i) +'\n')
            script.write(' sleep 2 \n')
            script.write(' no ip vrf ' + row[0] +'_vrf \n')
            script.write(' sleep 2 \n')
            script.write(' end \n')

        else: continue


     #    for i in range(len(row)): #Range el x and y
     #        if (row[i] == "APN Name"):
     #            APNType = i
     #        elif(APNType == )
     #    firstRow = 1
     # else:
     #    APNs.append( str(row[APNType]))
    #print(APNs)


APN_DB_Logic(1,10)
