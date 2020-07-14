import xlrd
def APN_DB_Logic(From, To, MTX):
    APNs = []

    workbook = xlrd.open_workbook("D:\\EPC\\Automation\\Corporate_APN_Project_PullfromNour\\Corporate APNs.xlsx")
    worksheet = workbook.sheet_by_index(0)
    print(worksheet)
    script = open('To be edited '+ "_Script.txt", "w")
    script.write('On ' + MTX + '-GGSN' + ':\n')

    for j in range (From, To):
        row = worksheet.row_values(j)
        print(row)
        if j == 0: continue
        if row[1]=='3G WIC':
            script.write(' Configure\n')
            script.write(' context aaa\n')
            script.write(' no ' + row[0] + ' \n')
            script.write(' exit \n')
            script.write(' context' + row[2] + '\n') ##Context name should be printed
            ##IF condition of row[4]==0
            script.write(' ip pool ' + row[0] +'_pool.0 \n')
            script.write(' ip pool ' + row[4] + '_pool.1 \n')




     #    for i in range(len(row)): #Range el x and y
     #        if (row[i] == "APN Name"):
     #            APNType = i
     #        elif(APNType == )
     #    firstRow = 1
     # else:
     #    APNs.append( str(row[APNType]))
    #print(APNs)


APN_DB_Logic(0,10)
