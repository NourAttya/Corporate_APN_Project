def Whitelisting_script(APNname,IPs,Domains,MTX,SecMTX,Priority,pathToSave,DDL,PDL,HDL):
    script = open(pathToSave + APNname + "_Script.txt", "w")
    script.write('On ' + MTX + '-GGSN' + ':\n')
    script.write(' Configure\n')
    script.write('On  ' + MTX + '-GGSN' + ':\n')
    script.write('==============\n \n')
    script.write('save configuration /flash/configfiles/Before_' + APNname + '.cfg -redundant\n')
    script.write(' config\n ')
    script.write('active-charging service ecs \n\n')
    if ("Domain" in DDL):
        script.write('ruledef' +APNname+'_Domains \n')
       # Domains= ",".join(Domains)
        for j in range(len(Domains)):
            script.write('ip server-ip-address = ' + Domains[j] + '\n')
        script.write('multi-line-or all-lines \n')
        script.write('exit \n\n')
        script.write('group-of-ruledefs ' +APNname+'_009_090_99999 \n')
        script.write('add-ruledef priority 10 ' + APNname +'_Domains \n')
        script.write('exit \n\n')
        if (HDL == 'Low Speed'):
            script.write('group-of-ruledefs ' + APNname + '_009_090_00064 \n')
            script.write('add-ruledef priority 10 ' + APNname + '_Domains \n')
            script.write('exit \n\n')
        else:
            pass
    if ("IP" in DDL):

        script.write('ruledef ' +APNname+'_IPs \n')
        for i in range(len(IPs)):
            script.write('ip server-ip-address =' + IPs[i] + '\n')
        script.write('multi-line-or all-lines \n')
        script.write('exit \n\n')
        script.write('group-of-ruledefs ' + APNname + '_009_090_99999 \n')
        script.write('add-ruledef priority 20 ' + APNname +'_IPs \n')
        script.write('exit \n\n')
        if (HDL == 'Low Speed'):
            script.write('group-of-ruledefs ' + APNname + '_009_090_00064 \n')
            script.write('add-ruledef priority 10 ' + APNname + '_Domains \n')
            script.write('exit \n')
        else:
            pass
    if ("P2P" in DDL):
        if ('Google maps' in PDL):
            script.write('ruledef ' +APNname+'_Googlemaps \n')
            script.write('p2p protocol = googlemaps \n')
            script.write('ip server-domain-name contains maps.google.com \n')
            script.write('ip server-domain-name contains google.com/maps \n')
            script.write('ip server-domain-name contains googleapis.com \n')
            script.write('ip server-domain-name contains maps.gstatic.com \n')
            script.write('ip server-domain-name contains www.gstatic.com \n')
            script.write('ip server-domain-name ends-with maps.google.com \n')
            script.write('ip server-domain-name ends-with google.com/maps \n')
            script.write('ip server-domain-name ends-with clients1.google.com \n')
            script.write('ip server-domain-name ends-with clients4.google.com \n')
            script.write('ip server-domain-name ends-with googleusercontent.com \n')
            script.write('ip server-domain-name ends-with lh3.googleusercontent.com \n')
            script.write('ip server-domain-name ends-with googlesyndication.com \n')
            script.write('ip server-domain-name ends-with ssl.gstatic.com \n')
            script.write('ip server-domain-name contains www.google.com \n')
            script.write('ip server-domain-name starts-with moe.gov.eg \n')
            script.write('ip server-domain-name contains gstatic.com \n')
            script.write('ip server-domain-name contains play.google.com \n')
            script.write('ip server-domain-name contains contacts.google.com \n')
            script.write('ip server-domain-name contains hangouts.google.com \n')
            script.write('ip server-domain-name contains android.clients.google.com \n')
            script.write('ip server-domain-name contains inbox.google.com \n')
            script.write('multi-line-or all-lines \n')
            script.write('exit \n\n')
            script.write('group-of-ruledefs' + APNname + '_009_090_99999 \n')
            script.write('add-ruledef priority 30' +APNname+'_Googlemaps \n')
            script.write('exit \n')

        if ('gmail' in PDL):
            script.write('ruledef' +APNname+'_gmail \n\n')
            script.write('p2p protocol = gmail \n')
            script.write('ip server-domain-name contains google.com.eg \n')
            script.write('ip server-domain-name contains mail.google.com \n')
            script.write('ip server-domain-name contains gstatic.com \n')
            script.write('ip server-domain-name contains play.google.com \n')
            script.write('ip server-domain-name contains contacts.google.com \n')
            script.write('ip server-domain-name contains hangouts.google.com \n')
            script.write('ip server-domain-name contains android.clients.google.com \n')
            script.write('ip server-domain-name contains inbox.google.com \n')
            script.write('multi-line-or all-lines \n\n')
            script.write('group-of-ruledefs' + APNname + '_009_090_99999 \n')
            script.write('add-ruledef priority 40' + APNname + '_gmail \n')
            script.write('exit \n')
        if ('instagram' in PDL):
            script.write('ruledef' +APNname+'_instagram \n')
            script.write('p2p protocol = instagram \n')
            script.write('multi-line-or all-lines \n')
            script.write('group-of-ruledefs' + APNname + '_009_090_99999 \n')
            script.write('add-ruledef priority 50' +APNname+'_gmail \n')
            script.write('exit \n')
        if ('Whatsapp' in PDL):
            script.write('ruledef APNname_Whatsapp \n')
            script.write('p2p protocol = Whatsapp \n')
            script.write('multi-line-or all-lines \n\n')
            script.write('group-of-ruledefs' +APNname+ '_009_090_99999 \n')
            script.write('add-ruledef priority 60' +APNname+'_gmail \n')
            script.write('exit \n\n')
        if (HDL == 'Low Speed'):
            script.write('group-of-ruledefs ' + APNname + '_009_090_00064 \n')
            script.write('add-ruledef priority 10 ' + APNname + '_Domains \n')
            script.write('exit \n\n')
        else:
            pass
    else:
        pass
        script.write('  exit\n')
    script.write('end\n')
    script.write('\n')
    script.write(' config\n ')
    script.write('active-charging service ecs \n\n')
    script.write('rulebase corporate-internet \n')
    script.write('action priority ' +Priority+ ' dynamic-only group-of-ruledefs ' +APNname+'_009_090_99999 charging-action sid_009_rg_090_rate_99999 \n')
    script.write(' exit \n')
    script.write('end\n')
    script.write('\n\n')
    #if (HDL == 'Low Speed'):
    ####Low speed script
    script.write('#################################################################################################################### \n')
    script.close()

