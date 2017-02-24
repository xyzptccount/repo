from time import sleep
from selenium import webdriver

linksOne = []
individualProductLinks = []
individualProductNumbers = []
individualProductPrices = []
i = 0
ciu = []


#driver = webdriver.Firefox(executable_path='/home/dave/drivers/geckodriver')
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get("https://www.millikenmedical.com/login")
driver.find_element_by_id('j_username').send_keys("info@ptunited.com")
driver.find_element_by_id("j_password").send_keys('1miltopline')
driver.find_element_by_css_selector('.submitform').click()
sleep(2)
driver.find_element_by_id('j_b2bunitid').click();
sleep(2)
driver.find_element_by_css_selector('#j_b2bunitid > option:nth-child(2)').click()
sleep(2)
driver.find_element_by_css_selector('.accountLoginForm').click()
sleep(4)
isBackend = driver.find_element_by_css_selector('.sign_header > a:nth-child(1)').text

if isBackend == 'MY ACCOUNT':
    driver.get('https://www.millikenmedical.com/search?q=%3Arelevance&view=grid&showItem=100&sort=relevance&page=0')
    
    for x in range(int(driver.find_element_by_css_selector('span.num_productlist:nth-child(8)').text)):
        linksOne.append('https://www.millikenmedical.com/search?q=%3Arelevance&view=grid&showItem=100&sort=relevance&page=' + str(x))

    for x in linksOne:
        driver.get(x)
        #sleep(2)
        ipl = driver.find_elements_by_css_selector('div.item a')
        for y in ipl:
            individualProductLinks.append(y.get_attribute('href'))
    
    for x in individualProductLinks:
        if i == 50:
            break
        else:
            i = i + 1
            driver.get(x)
            #sleep(2)
            itemNumbers = driver.find_elements_by_css_selector('td.varCode')
            itemPrices = driver.find_elements_by_css_selector('td.price')
            for y in itemNumbers:
                ciu.append(str(driver.current_url))
                individualProductNumbers.append(str(y.text))
            for z in itemPrices:
                individualProductPrices.append(str(z.text))

    print len(individualProductLinks)
    print individualProductNumbers
    print individualProductPrices
    print len(individualProductNumbers)
    print len(individualProductPrices)
    
    with open('mmItems.py', 'w') as f:
        f.write('numbers = ' + str(individualProductNumbers) + '\n')
        f.write('prices = ' + str(individualProductPrices) + '\n')
        f.write('links = ' + str(ciu))
        f.close()







