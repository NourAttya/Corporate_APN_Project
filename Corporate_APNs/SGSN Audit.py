import xlrd
import paramiko
import numpy as np
host = "10.255.224.224"
port = 22
username = "aayman"
password = "VFcore456"

command = " gsh list_la"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
if not ssh.connect(host, port, username, password):
    print("SSH session failed on login.")
else:
    print("SSH session login successful")

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()

#############################################################



for line in  lines :
    #line= np.array(lines)
    #line = int(line.lstrip("A  la   -mcc  602  -mnc  02  -lac"))
    line = line.lstrip("A  la   -mcc  602  -mnc  02  -lac")
    LAC= line.split("\n")
    for i in LAC:
        print(i)
    #print(LAC)
        #print(line)
    #del line[0:2]
    #print(line)

