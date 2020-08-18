from sys import argv
import csv
import paramiko
import time
import re
import os
import csv

uname = argv[1]
pwrd = argv[2]
try:
    Node_IP = argv[3]
except:
    Node_IP = "None"

# specify GGSNs and their IPs
GGSN_IP_DICT = {"GGSN5": "10.253.2.50", "GGSN6": "10.254.2.21", "GGSN7": "10.254.222.17", "GGSN8": "10.122.246.18",
                "GGSN9": "10.122.244.20", "GGSN10": "10.255.224.4", "GGSN11": "10.5.14.4", "GGSN12": "10.254.222.20",
                "GGSN13": "172.18.202.152", "GGSN14": "10.254.2.24"}




# specify GGSN template file
ggsn_template = "D:\\python3\\ggsn_template.txt"
Trulebase_file = "D:\\python3\\rulebase_file.txt"


# function to extract unused rules to delete them
# input1: Template file
# input2: GGSN config file
# input3: name of GGSN to generate output file
def extract_ruledef(TGfile, Gconfigfile, GGSN):
    rulesfile = GGSN + "rules.txt"
    # adding template rules in a list "Template_rules"
    with open(TGfile, "r") as test:
        Template_rules = []
        for i in test:
            Template_rules.append(i.strip("\n"))
    # extracting ruldefs/group of ruledefs config only from config file and put it in list "yy"
    with open(Gconfigfile, "r") as test:
        x = []
        for i in re.findall('Last login(.*?)edr-format', test.read(), re.S):
            x.append(i)
    with open(rulesfile, "w") as op:
        for i in x:
            op.write(i)
    with open(rulesfile, "r") as test:
        y = test.readlines()
        yy = []
        for i in y:
            if ("ruledef" in i and "priority" not in i and "statistics-collection" not in i) or (
                    "group-of-ruledefs" in i and "priority" not in i and "statistics-collection" not in i):
                yy.append(i.replace("    ruledef", "ruledef").replace("    group-of-ruledefs", "group-of-ruledefs"))
    # preparing list "Grules" with no definetion to compare it with template
    Grules = []
    for i in yy:
        Grules.append(i.replace("group-of-ruledefs ", "").replace("ruledef ", "").replace("\n", ""))

    # preparing list "non_matching" which have rules not in template rules list "Template_rules"
    # preparing list "testy" which have rules in template rules list "Template_rules" but with legend whether it is ruledef or group of ruledefs
    global non_matching
    global testy
    matching = []
    non_matching = []
    for i in Grules:
        if i in Template_rules:
            matching.append(i + "\n")
        else:
            non_matching.append(i)

    for i in matching:
        print(i.strip("\n"))

    testy = [i for i in yy if any(s in i for s in matching)]

    # for i in testy:
    #	if "group-of-ruledefs" in i:
    #		print(i.strip("group-of-ruledefs").strip("\n").lstrip())
    #	if "ruledef " in i:
    #		print(i.strip("ruledef").strip("\n").lstrip())

    print(len(testy))
    print(len(matching))
    # preparing list "test2" which have rules only group of ruledefs that are in the template and in GGSN config
    test2 = []
    for i in testy:
        if "group-of-ruledefs" in i:
            test2.append(i)
    # extract ruledefs under group of ruledefs which exist in template, add them to list "Template_rules" with some parsing over the texts
    rulesingrules = []
    rulesingrules1 = []
    for i in test2:
        with open(rulesfile, "r") as test:
            for s in re.findall(i + '(.*?)#exit', test.read(), re.S):
                rulesingrules1.append(
                    re.sub("[ \t]*add-ruledef priority.*ruledef ", ",", s).replace("\n", "").replace("    ", "").split(
                        ","))

    for i in rulesingrules1:
        rulesingrules = rulesingrules + i
    rulesingrules1 = list(set(rulesingrules))
    if "" in rulesingrules1:
        rulesingrules1.remove("")
    if "_H" in rulesingrules1:
        rulesingrules1.remove("_H")
    rulesingrules = []

    for i in rulesingrules1:
        rulesingrules.append(re.sub(i, "ruledef " + i, i))

    Template_rules = Template_rules + rulesingrules1

    # preparing list "non_matching" which have rules not in template rules list "Template_rules"
    # preparing list "testy" which have rules not in template rules list "Template_rules" but with legend whether it is ruledef or group of ruledefs
    matching = []
    non_matching = []
    for i in Grules:
        if i in Template_rules:
            matching.append(i)
        else:
            non_matching.append(i + "\n")

    testy = []
    testy = [i for i in yy if any(s in i for s in non_matching)]
    # for i in testy:
    # for s in non_matching:
    #	if any(s in i for i in yy):
    #		testy.append(i)

    # for i in non_matching:
    #	print(i.strip("\n"))
    #
    # print(len(non_matching))
    # print (len(testy))
    # print(len(yy))

    # Generate output CRQ file
    with open(GGSN + "_output_script.txt", "w") as op:
        op.write("configure\n")
        op.write("\tactive-charging service ecs\n")
        for i in testy:
            op.write("\t\tno " + i + "\n")
        op.write("end\n\n")


def rulebase_cleanup(Gconfigfile, GGSN):
    # adding template rulebases in list "Trulebases" from file
    with open(Trulebase_file, "r") as Trulebasefile:
        Trulebases = []
        for i in Trulebasefile:
            Trulebases.append(i.replace("\n", ""))

    # extracting all configured rulebase names onn GGSN from the template
    with open(Gconfigfile, "r") as test:
        x = []
        for i in test:
            x.append(i)
        new_rulebases1 = [io for io in x if any(s in io for s in Trulebases)]
    new_rulebases = []
    for i in new_rulebases1:
        new_rulebases.append(re.sub("[ \t]*rulebase", "rulebase", i).replace("\n", ""))

    for i in new_rulebases:
        with open(Gconfigfile, "r") as test:
            x = []
            for m in re.findall(i + '(.*?)route priority', test.read(), re.S):
                x.append(m)
        with open("test.txt", "w") as op:
            for o in x:
                op.write(o)
        with open("test.txt", "r") as test2:
            x = []
            for l in test2:
                x.append(l)
        deleted_from_rulebases = [io for io in x if any(s in io for s in testy)]
        if deleted_from_rulebases:
            with open(GGSN + "_output_script.txt", "a") as op:
                op.write("\n\n")
                op.write("configure\n")
                op.write("\t" + i + "\n")
                for im in deleted_from_rulebases:
                    op.write(re.sub(r'[ \t]*(action priority \d*?) .*', r'\t\tno \1 ', im).replace("\n", ""))
                    op.write("\n")
                op.write("end\n")


def rollback_extract_ruledef(TGfile, Gconfigfile, GGSN):
    rulesfile = GGSN + "rules.txt"
    with open(Gconfigfile, "r") as test:
        x = []
        for i in re.findall('Last login(.*?)edr-format', test.read(), re.S):
            x.append(i)
    with open(rulesfile, "w") as op:
        for i in x:
            op.write(i)

    x = []
    for i in testy:
        with open(rulesfile, "r") as test:
            for m in re.findall(i + '(.*?)#', test.read(), re.S):
                x.append(i + m.replace("\n\n", "\n") + "exit")

    with open(GGSN + "_output_script.txt", "a") as op:
        op.write("==============================================================================\n")
        op.write("		Rollback\n")
        op.write("==============================================================================\n\n")
        op.write("configure\n")
        op.write("\tactive-charging service ecs\n")
        for im in x:
            op.write(im + "\n\n")
        op.write("end\n")
        op.write("==============================================================================\n\n")


def rollback_rulebase_cleanup(Gconfigfile, GGSN):
    # adding template rulebases in list "Trulebases" from file
    with open(Trulebase_file, "r") as Trulebasefile:
        Trulebases = []
        for i in Trulebasefile:
            Trulebases.append(i.replace("\n", ""))

    # extracting all configured rulebase names onn GGSN from the template
    with open(Gconfigfile, "r") as test:
        x = []
        for i in test:
            x.append(i)
        new_rulebases1 = [io for io in x if any(s in io for s in Trulebases)]
    new_rulebases = []
    for i in new_rulebases1:
        new_rulebases.append(re.sub("[ \t]*rulebase", "rulebase", i).replace("\n", ""))

    for i in new_rulebases:
        with open(Gconfigfile, "r") as test:
            x = []
            for m in re.findall(i + '(.*?)route priority', test.read(), re.S):
                x.append(m)
        with open("test.txt", "w") as op:
            for o in x:
                op.write(o)
        with open("test.txt", "r") as test2:
            x = []
            for l in test2:
                x.append(l)
        deleted_from_rulebases = [io for io in x if any(s in io for s in testy)]
        if deleted_from_rulebases:
            with open(GGSN + "_output_script.txt", "a") as op:
                op.write("\n\n")
                op.write("configure\n")
                op.write("\t" + i + "\n")
                for im in deleted_from_rulebases:
                    op.write(im.replace("\n\n", ""))
                # op.write(re.sub(r'[ \t]*(action priority \d*?) .*',r'\t\tno \1 ',im).replace("\n",""))
                # op.write("\n")
                op.write("end\n")


def open_SSH(uname, pwrd, Node_IP, logfile):
    try:
        # username = uname
        # password = pwrd
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(Node_IP, username=uname, password=pwrd)
        connection = session.invoke_shell()
        time.sleep(3)
        connection.send("\n")
        time.sleep(3)
        connection.send("show configuration active-charging service name ecs \n")
        time.sleep(3)
        output = connection.recv(10000000000)
        # print output + "\n"
        with open("D:\\python3\\" + logfile + ".txt", "w") as op:
            op.write(output.decode("utf-8"))
        # Closing the connection
        session.close()
    except IOError:
        print("Input parameter error in " + ip + "! Please check username, password and file name, continuing..")


if Node_IP == "None":
    for i, x in GGSN_IP_DICT.items():
        print("Collecting Data for " + i, x)
        open_SSH(uname, pwrd, x, i)
        extract_ruledef(ggsn_template, i + ".txt", i)
        rulebase_cleanup(i + ".txt", i)
        # rollback_extract_ruledef(ggsn_template,i +".txt",i)
        # rollback_rulebase_cleanup(i +".txt",i)
        try:
            # os.remove("D:\\python3\\"+i+".txt")
            os.remove("D:\\python3\\" + i + "rules.txt")
            os.remove("D:\\python3\\test.txt")
        except FileNotFoundError:
            pass

else:
    for i, v in GGSN_IP_DICT.items():
        if i == Node_IP:
            IP = v
            log = log2 = i
            file = "D:\\python3\\" + log + ".txt"
    try:
        print("Collecting Data for " + log)
        # open_SSH(uname,pwrd,IP,log)
        extract_ruledef(ggsn_template, log + ".txt", log)
        rulebase_cleanup(log + ".txt", log)
    # rollback_extract_ruledef(ggsn_template,log +".txt",log)
    # rollback_rulebase_cleanup(log +".txt",log)
    except NameError:
        print("Please enter correct GGSN name from the below, or don't enter any name, script will run on all GGSNs:")
        for i in list(GGSN_IP_DICT.keys()):
            print(i)
    try:
        # os.remove(log +".txt")
        os.remove(log + "rules.txt")
        os.remove("test.txt")
    except:
        pass
