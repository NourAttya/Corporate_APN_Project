import time
import paramiko

host = "10.255.224.224"
port = 22
username = "aayman"
password = "Voda_1010"

command = "cat  /Core/home/aayman/ConfigFile_from_export"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
if not ssh.connect(host, port, username, password):
    print("SSH session failed on login.")
else:
    print("SSH session login successful")

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
timestr = time.strftime("%d-%m-%Y")
f = open("D:\EPC\Automation\Corporate APNs App" + "/SGSN Config" + timestr + ".txt", "w")

for line in lines:
    f.write(line)

f.close()