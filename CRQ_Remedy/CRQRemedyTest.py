import time
from splinter import Browser
from selenium import webdriver

try:

    executable_path = {'executable_path': 'D:/EPC\Automation/Corporate_APN_Project_PullfromNour/chromedriver.exe'}

    browser = Browser('chrome', **executable_path)
    browser.visit('https://remedy05.vf-eg.internal.vodafone.com/arsys/shared/login.jsp?/arsys/forms/remedy-app/SHR%3ALandingConsole/Default+Administrator+View/?/')
    browser.fill('username', 'V20NAttia')
    browser.fill('pwd', 'Voda!234')

    button = browser.find_by_name('login')
    button.click()
    time.sleep(3)
    button = browser.find_by_id('reg_img_304316340')
    button.click()
    time.sleep(13)
    button = browser.find_by_text('Change Management')
    button.click()
    time.sleep(3)
    button = browser.find_by_text('New Change')
    button.click()
    time.sleep(7)
    browser.find_by_id('arid_WIN_3_1000000000').fill('DNS TAC/LAC Change')
    time.sleep(3)
    browser.find_by_id('arid_WIN_3_536870975').fill('DNS TAC/LAC Change')
    time.sleep(3)
    button = browser.find_link_by_partial_text('Management')
    button.click()

    time.sleep(1)

    button = browser.find_by_name('WIN_3_RCGroup536871013')
    button.click()
    time.sleep(1)
    button = browser.find_by_name('WIN_3_RCGroup536871021')
    button.click()
    time.sleep(1)
    button = browser.find_by_name('WIN_3_RCGroup536871030')
    button.click()
    time.sleep(1)
    button = browser.find_by_name('WIN_3_RCGroup536871039')
    button.click()
    time.sleep(1)

    button = browser.find_by_css('[style="top:0px; left:283px; width:21px; height:21px;"]')
    button.click()

    button = browser.find_by_text('Packet  Core Configuration (2nd Line)')
    button.click()
    time.sleep(1)
    button = browser.find_by_text('DNS')
    button.click()
    time.sleep(1)
    button = browser.find_by_text('Software Upgrade (Major)')
    button.click()
    time.sleep(1)
    button = browser.find_by_text('Date/System')
    button.click()
    time.sleep(1)

    button = browser.find_by_css('[style="top:0px; left:317px; width:21px; height:21px;"]')
    button.click()

    button = browser.find_by_id('calenderon')
    time.sleep(1)
    day = button.value
    day = str(day)
    time.sleep(1)

    button = browser.find_by_id('popupmonth')
    month = button.value
    month = str(month)
    time.sleep(1)
    day1 = int(day) + 2
    time.sleep(1)
    day1 = str(day1)
    time.sleep(1)
    button = browser.find_by_text(day1)
    button.click()

    button = browser.find_by_id("hr").fill("03")
    time.sleep(1)
    button = browser.find_by_css('[style="position:relative; padding-top:3px; left:0px; height:19px;"]')
    button.click()
    time.sleep(1)
    button = browser.find_by_css('[style="top:0px; left:317px; width:21px; height:21px;"]')[1]
    button.click()
    time.sleep(1)
    button = browser.find_by_text(day1)
    button.click()
    time.sleep(1)
    button = browser.find_by_id("hr").fill("07")
    time.sleep(1)

    button = browser.find_by_css('[style="position:relative; padding-top:3px; left:0px; height:19px;"]')
    button.click()
    time.sleep(1)
    button = browser.find_link_by_text('Tasks')
    button.click()
    time.sleep(1)
    button = browser.find_by_id('WIN_3_10003044')
    button.click()
    time.sleep(2)
    window = browser.windows[1]
    window.is_current = True
    time.sleep(2)
    button = browser.find_by_id('arid_WIN_0_10007000').fill('DNS TAC/LAC Change')
    time.sleep(2)
    button = browser.find_by_id('arid_WIN_0_8').fill('DNS TAC/LAC Change')
    time.sleep(1)
    button = browser.find_link_by_text('Add')
    button.click()
    time.sleep(1)



    with browser.get_iframe(1) as iframe:
        elem = iframe.find_by_id("PopupAttInput").fill("C:\\Python27\\3G_Change.txt")
    with browser.get_iframe(1) as iframe:
        elem = iframe.find_by_id("PopupAttLabel1").fill("C:\\Python27\\3G_Change_rollback.txt")


    time.sleep(1)
    with browser.get_iframe(1) as iframe:
        iframe.find_by_css('[style="width: 398px; top: 202px;"]').find_by_text('OK').click()
    time.sleep(1)

    button = browser.find_by_id('arid_WIN_0_536870977').fill('attached')
    time.sleep(1)
    button = browser.find_by_id('arid_WIN_0_536871000').fill('attached')
    time.sleep(1)
    button = browser.find_by_id('arid_WIN_0_536871004').fill('attached')
    time.sleep(1)
    button = browser.find_by_text('Assignment/Dates')
    button.click()
    button = browser.find_by_css('[style="top:0px; left:345px; width:21px; height:21px;"]')
    button.click()
    button = browser.find_by_text('Service Management')
    button.click()
    time.sleep(1)
    button = browser.find_by_css('[style="top:0px; left:345px; width:21px; height:21px;"]')[1]
    button.click()
    button = browser.find_by_text('Mobile Internet & Enterprise')
    button.click()
    time.sleep(1)
    button = browser.find_by_css('[style="top:0px; left:345px; width:21px; height:21px;"]')[2]
    button.click()
    button = browser.find_by_text('Mobile Internet & Data Support')
    button.click()
    time.sleep(1)
    button = browser.find_by_css('[style="top:0px; left:345px; width:21px; height:21px;"]')[3]
    button.click()
    button = browser.find_by_text('Mobile Internet & Data Support General Account')
    button.click()
    time.sleep(1)
    button = browser.find_by_css('[style="top:0px; left:369px; width:21px; height:21px;"]')
    button.click()
    time.sleep(1)

    button = browser.find_by_id('calenderon')
    time.sleep(1)
    day = button.value
    time.sleep(1)
    day1 = int(day) + 2
    time.sleep(1)
    day1 = str(day1)
    time.sleep(1)
    button = browser.find_by_text(day1)
    button.click()
    button = browser.find_by_id("hr").fill("03")
    time.sleep(1)
    button = browser.find_by_css('[style="position:relative; padding-top:3px; left:0px; height:19px;"]')
    button.click()
    time.sleep(1)
    button = browser.find_by_css('[style="top:0px; left:369px; width:21px; height:21px;"]')[1]
    button.click()
    time.sleep(1)
    button = browser.find_by_text(day1)
    button.click()
    time.sleep(1)
    button = browser.find_by_id("hr").fill("07")
    time.sleep(1)

    button = browser.find_by_css('[style="position:relative; padding-top:3px; left:0px; height:19px;"]')
    button.click()
    time.sleep(1)

    button = browser.find_by_css('[style="top:0px; left:0px; width:54px; height:21px;"]')
    button.click()
    time.sleep(1)

    window = browser.windows[0]
    window.is_current = True

    button = browser.find_by_id('arid_WIN_3_1000000163')
    button.click()
    time.sleep(1)

    button = browser.find_by_text('4-Minor/Localized')
    button.click()
    time.sleep(1)

    button = browser.find_by_text('Save')
    button.click()
    time.sleep(5)

    button = browser.find_by_text('Next Stage')
    button.click()
    time.sleep(2)

    button = browser.find_by_id('arid_WIN_3_1000000182')
    CRQ = button.value
    print
    CRQ
    time.sleep(2)

    # button = browser.find_by_id('WIN_0_300000044')
    # button.click()
    # time.sleep(2)
    button = browser.find_by_text('Logout')
    button.click()
    time.sleep(7)
    browser.quit()
except:
    button = browser.find_by_text('Logout')
    button.click()
    time.sleep(7)
    browser.quit()
