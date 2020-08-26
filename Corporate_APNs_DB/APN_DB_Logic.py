import xlrd
import os
import csv
from openpyxl import Workbook

def getAPNs(DBFolder,referenceSheet):

    workbook = xlrd.open_workbook(referenceSheet)
    worksheet = workbook.sheet_by_index(0)
    APNsToBeTerminated=[]
    firstRow=0
    for j in range(worksheet.nrows):
        row = worksheet.row_values(j)

        if(firstRow==0):
            for i in range(len(row)):
                if(row[i]=="APN  Name"):
                    APNnameIndex=i
                    firstRow=1

        else:
            APNsToBeTerminated.append(row[APNnameIndex])

    print(APNsToBeTerminated)
    book = Workbook()
    sheet = book.active

    for filename in os.listdir(DBFolder):

        # get the file name without the extension in "file"
        (file, ext) = os.path.splitext(filename)

        # Only get xml files
        if not filename.endswith('.csv'): continue

        fullnameCSV = os.path.join(DBFolder, filename)

        with open(fullnameCSV) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    for i in range(len(row)):
                        if(row[i]=="APN Name"):
                            APNnameIndex=i
                            break
                    line_count += 1
                else:
                    if(row[APNnameIndex] in APNsToBeTerminated):
                        sheet.append(row)
    book.save(DBFolder+'\\APNsCleanup.xlsx')
#getAPNs("D:\\Automation Team\\Corporate APN Project\\DBs","D:\\Automation Team\\Corporate APN Project\\GGSN Config Files\\APN-To be terminated.xlsx")



def APN_DB_Logic(From, To,DBFolder,referenceSheet,APNsCleanupSheet):
    #APNs = []
    if(DBFolder!=""):
        getAPNs(DBFolder,referenceSheet)
        workbook = xlrd.open_workbook(DBFolder+'\\APNsCleanup.xlsx')
    elif(APNsCleanupSheet!=""):
        workbook = xlrd.open_workbook(APNsCleanupSheet)
    worksheet = workbook.sheet_by_index(0)
    print(worksheet)
    script = open(DBFolder+'\\To be edited '+ "_Script.txt", "w")
    row = worksheet.row_values(int(From))
    script.write('On ' + row[4] + '-GGSN' + ':\n')

    for j in range (int(From),int( To)):
        row = worksheet.row_values(j)
        print(row)
        #if j == 0: continue
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
            for i in range (0, int(IPpoolCount) ):
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


#APN_DB_Logic(1,10,"D:\\Automation Team\\Corporate APN Project\\DBs","D:\\Automation Team\\Corporate APN Project\\GGSN Config Files\\APN-To be terminated.xlsx")
