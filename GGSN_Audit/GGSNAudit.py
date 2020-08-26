from sys import argv
import csv
import paramiko
import time
import re
import os
import csv
import ast
from tkinter import messagebox


# function to extract unused rules to delete them
# input1: Template file
# input2: GGSN config file
# input3: name of GGSN to generate output file
def extract_ruledef(TGfile, Gconfigfile, GGSN, path):
    rulesfile = path + GGSN + "rules.txt"
    # adding template rules in a list "Template_rules"
    with open(TGfile, "r") as test:
        Template_rules = []
        for i in test:
            Template_rules.append(i.strip("\n"))
    # extracting ruldefs/group of ruledefs config only from config file and put it in list "yy"
    with open(path + Gconfigfile, "r") as test:
        x = []
        for i in re.findall('Last login(.*?)edr-format', test.read(), re.S):
            x.append(i)
    with open(rulesfile, "w") as op:
        for i in x:
            op.write(i)
    with open(rulesfile, "r") as test:
        y = test.readlines()
        yy = []
        yy2 = []
        for i in y:
            if ("ruledef" in i and "priority" not in i and "statistics-collection" not in i) or (
                    "group-of-ruledefs" in i and "priority" not in i and "statistics-collection" not in i):
                yy.append(i.replace("    ruledef", "ruledef").replace("    group-of-ruledefs", "group-of-ruledefs"))
            if ("ruledef" in i and "priority" in i):
                yy2.append(i)

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
            matching.append(" " + i + "\n")
        else:
            non_matching.append(i)

    testy = [i for i in yy if any(s in i for s in matching)]

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
            non_matching.append(" " + i + "\n")

    testy = []
    testy1 = [i for i in yy if any(s in i for s in non_matching)]

    for i in testy1:
        testy.append(i.strip("\n"))

    # preparing to remove ruledefs from group of ruledefs

    # all stand alone rules that needs to be deleted in list (testy2)
    testy2 = []
    for i in testy:
        if "ruledef " in i:
            testy2.append(i)

    # all group of ruledefs configuration in list (blo1)
    with open(rulesfile, "r") as test:
        blo1 = []
        for i in re.findall('(group-of-ruledefs.*?)#exit', test.read(), re.S):
            blo1.append(i)

    # from all ruledefs, matching which ruledefs needed to be deleted from group of ruledefs
    global testy5
    testy5 = list(
        set([re.sub("[ \t]*add-ruledef ", "add-ruledef ", i).strip("\n") for i in yy2 if any(s in i for s in testy2)]))
    # from the above list matches which group of ruledefs these rules are configured in

    testy3 = list(set([i for i in blo1 if any(s in i for s in testy5)]))

    # writing all matched group of ruledefs that needs ruledefs to be deleted from it in a file and then in a list, to have each line in an item of a list "all_groups_match"
    with open(path + "test2.txt", "w") as test:
        for i in testy3:
            test.write(i + "exit\n")

    global all_groups_match
    all_groups_match = []
    with open(path + "test2.txt", "r") as test:
        for i in test:
            all_groups_match.append(re.sub("[ \t]*add-ruledef ", "add-ruledef ", i).strip("\n"))
    # print(all_groups_match)

    # replace what needs to be deleted from under of the group of ruledef from "add-ruledef" to be "no add-ruledef"
    group_of_ruledef_cleanup = []
    for i in all_groups_match:
        if i is '':
            continue
        if "exit" in i:
            group_of_ruledef_cleanup.append(re.sub("[ \t]*exit", "\t\texit\n", i))
        if "group-of-ruledefs" in i:
            group_of_ruledef_cleanup.append(re.sub("[ \t]*group-of-ruledefs", "\t\tgroup-of-ruledefs", i))
        if i not in testy5 and "group-of-ruledefs" not in i and "exit" not in i:
            continue
        # group_of_ruledef_cleanup.append("\t\t\t"+i)
        if i in testy5:
            group_of_ruledef_cleanup.append(
                re.sub(r"add-ruledef priority (\d+?) .*", r"\t\t\tno add-ruledef priority \1", i))

    # for c in group_of_ruledef_cleanup:
    #	print (c)

    # Generate output CRQ file
    with open(path + GGSN + "_output_script.txt", "w") as op:
        op.write("configure\n")
        op.write("\tactive-charging service ecs\n")
        for i in group_of_ruledef_cleanup:
            op.write(i + "\n")
        for i in testy:
            op.write("\t\tno " + i + "\n")
        op.write("end\n\n")


def rulebase_cleanup(Gconfigfile, GGSN, path):
    new_rulebases = []
    x = []
    with open(path + Gconfigfile, "r") as test:
        for i in re.findall('[ \t]*rulebase (.*?)\n', test.read(), re.S):
            x.append(i)

    testy1 = []
    for f in testy:
        testy1.append(f + " ")

    for i in x:
        if ' ' in i:
            x.remove(i)
        if i is "None":
            x.remove(i)
    for i in x:
        new_rulebases.append("rulebase " + i)

    for i in new_rulebases:
        with open(path + Gconfigfile, "r") as test:
            x = []
            for m in re.findall(i + '(.*?)route priority', test.read(), re.S):
                x.append(m)
        with open(path + "test.txt", "w") as op:
            for o in x:
                op.write(o)
        with open(path + "test.txt", "r") as test2:
            x = []
            for l in test2:
                x.append(l)
        deleted_from_rulebases = [io for io in x if any(s in io for s in testy1)]
        if deleted_from_rulebases:
            with open(path + GGSN + "_output_script.txt", "a") as op:
                op.write("\n\n")
                op.write("configure\n")
                op.write("\t" + i + "\n")
                for im in deleted_from_rulebases:
                    op.write(re.sub(r'[ \t]*(action priority \d*?) .*', r'\t\tno \1 ', im).replace("\n", ""))
                    op.write("\n")
                op.write("end\n")


def rollback_extract_ruledef(TGfile, Gconfigfile, GGSN, path):
    rulesfile = path + GGSN + "rules.txt"
    with open(path + Gconfigfile, "r") as test:
        x = []
        for i in re.findall('Last login(.*?)edr-format', test.read(), re.S):
            x.append(i)

    with open(rulesfile, "w") as op:
        for i in x:
            op.write(i)

    x = []
    with open(rulesfile, "r") as op:
        for i in op:
            x.append(i)

    y = []
    z = []
    f = []
    for i in testy:
        if "ruledef " in i:
            y.append(i)
        else:
            z.append(i)

    x = []
    for i in y:
        with open(rulesfile, "r") as test:
            for m in re.findall(i + '\n(.*?)#', test.read(), re.S):
                if ("add-ruledef" in m) and ("group-of-ruledefs " + i not in m):
                    continue
                else:
                    x.append(i + m.replace("\n\n", "\n") + "exit")

    for i in z:
        with open(rulesfile, "r") as test:
            for m in re.findall(i + '\n(.*?)#', test.read(), re.S):
                f.append(i + m.replace("\n\n", "\n") + "exit")

    group_of_ruledef_cleanup = []
    for i in all_groups_match:
        if i is '':
            continue
        if "exit" in i:
            group_of_ruledef_cleanup.append(re.sub("[ \t]*exit", "\t\texit\n", i))
        if "group-of-ruledefs" in i:
            group_of_ruledef_cleanup.append(re.sub("[ \t]*group-of-ruledefs", "group-of-ruledefs", i).strip("\n"))
        if i not in testy5 and "group-of-ruledefs" not in i and "exit" not in i:
            continue
        if i in testy5:
            group_of_ruledef_cleanup.append(re.sub("add-ruledef ", "\t\t\tadd-ruledef ", i).strip("\n"))

    with open(path + GGSN + "_output_script.txt", "a") as op:
        op.write("==============================================================================\n")
        op.write("		Rollback\n")
        op.write("==============================================================================\n\n")
        op.write("configure\n")
        op.write("\tactive-charging service ecs\n")
        for im in x:
            op.write(im + "\n\n")
        for im in group_of_ruledef_cleanup:
            op.write(im + "\n")
        for im in f:
            op.write(im + "\n\n")
        op.write("end\n")
        op.write("==============================================================================\n\n")


def rollback_rulebase_cleanup(Gconfigfile, GGSN, path):
    new_rulebases = []
    x = []
    with open(path + Gconfigfile, "r") as test:
        for i in re.findall('[ \t]*rulebase (.*?)\n', test.read(), re.S):
            x.append(i)

    testy1 = []
    for f in testy:
        testy1.append(f + " ")

    for i in x:
        if ' ' in i:
            x.remove(i)
        if i is "None":
            x.remove(i)
    for i in x:
        new_rulebases.append("rulebase " + i)

    for i in new_rulebases:
        with open(path + Gconfigfile, "r") as test:
            x = []
            for m in re.findall(i + '(.*?)route priority', test.read(), re.S):
                x.append(m)
        with open(path + "test.txt", "w") as op:
            for o in x:
                op.write(o)
        with open(path + "test.txt", "r") as test2:
            x = []
            for l in test2:
                x.append(l)

        deleted_from_rulebases = [io for io in x if any(s in io for s in testy1)]
        if deleted_from_rulebases:
            with open(path + GGSN + "_output_script.txt", "a") as op:
                op.write("\n\n")
                op.write("configure\n")
                op.write("\t" + i + "\n")
                for im in deleted_from_rulebases:
                    op.write(im.replace("\n\n", ""))
                # op.write(re.sub(r'[ \t]*(action priority \d*?) .*',r'\t\tno \1 ',im).replace("\n",""))
                # op.write("\n")
                op.write("end\n")


def open_SSH(uname, pwrd, IP, name, path):
    try:
        # username = uname
        # password = pwrd
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(IP, username=uname, password=pwrd)
        connection = session.invoke_shell()
        time.sleep(3)
        connection.send("\n")
        time.sleep(3)
        connection.send("show configuration active-charging service name ecs \n")
        time.sleep(3)
        output = connection.recv(10000000000)
        # print output + "\n"
        with open(path + name + ".txt", "w") as op:
            op.write(output.decode("utf-8"))
        # Closing the connection
        session.close()
    except:
        print("Can't login on " + name + " " + IP + "! Please check Connectivity, username and password. Continuing..")


# uname = argv[1]
# pwrd = argv[2]
# ggsn_template = argv[3]
##GGSN_IP_DICT = argv[4]
# Node_IP = argv[4]


# specify GGSN template file
# ggsn_template = "D:\\python3\\ggsn_template.txt"

def main_ggsn_rule(uname, pwrd, ggsn_template, name, IP):
    # def main_ggsn_rule(uname,pwrd,ggsn_template,name,IP):


    GGSN_IP_DICT = dict(zip(name,IP))
    pathlist = ggsn_template.split("/")
    pathlist.pop(-1)
    path = "/".join(pathlist) + "/"
    SCRIPT_STATUS = []
    for i, x in GGSN_IP_DICT.items():
    #    print("Collecting Data for " + "GGSN" + i, x)
        try:
            open_SSH(uname, pwrd, x, "GGSN" + i, path)
            extract_ruledef(ggsn_template, "GGSN" + i + ".txt", "GGSN" + i, path)
            rulebase_cleanup("GGSN" + i + ".txt", "GGSN" + i, path)
            rollback_extract_ruledef(ggsn_template, "GGSN" + i + ".txt", "GGSN" + i, path)
            rollback_rulebase_cleanup("GGSN" + i + ".txt", "GGSN" + i, path)
            SCRIPT_STATUS.append("Succeeded on GGSN"+i)
        except FileNotFoundError:
            SCRIPT_STATUS.append("Failed on GGSN"+i)
            pass
        try:
            os.remove(path + "GGSN" + i + ".txt")
        except FileNotFoundError:
            pass
        try:
            os.remove(path + "GGSN" + i + "rules.txt")
        except FileNotFoundError:
            pass
        try:
            os.remove(path + "test2.txt")
        except FileNotFoundError:
            pass
        try:
            os.remove(path + "test.txt")
        except FileNotFoundError:
            pass

    messagebox.showinfo("Message Box", "\n".join(SCRIPT_STATUS))
#main_ggsn_rule(uname=argv[1], pwrd=argv[2], ggsn_template=argv[3], name=argv[4], IP=argv[5], Node_IP=argv[6])




#main_ggsn_rule(uname=argv[1], pwrd=argv[2], ggsn_template=argv[3], name=argv[4], IP=argv[5], Node_IP=argv[6])

