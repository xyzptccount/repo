#testing purposes, might need to work on url appenage while pulling href attributes also will need to get pages if products span more than one page


from time import sleep
from selenium import webdriver

linksOne = []
linksTwo = []
individualProductLinks = []
individualProductNumbers = []
individualProductPrices = []
i = 1
ciu = []


driver = webdriver.Firefox(executable_path='/home/dave/drivers/geckodriver')
driver.get("https://www.fab-ent.com/manage-account/")
driver.find_element_by_id('username').send_keys("qw@ptunited.com")
driver.find_element_by_id("password").send_keys('3Miltopline')
driver.find_element_by_css_selector('input.button').click()
sleep(5)
for x in driver.find_elements_by_css_selector('.subCat li a'):
    linksOne.append(x.get_attribute('href'))
for x in linksOne:
    driver.get(x)#might need to  add https://fab-ent.com in front
    for y in driver.find_elements_by_css_selector('.subCat > li:nth-child('+str(i)+') > ul li a'):
        linksTwo.append(y.get_attribute('href'))#might need driver.current_url in front
    i = i + 1
for x in linksTwo:
    driver.get(x)
    if driver.find_elements_by_css_selector('#fabent-product-options > form:nth-child(1) > table:nth-child(5) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(1)') != 0:
        for y in driver.find_elements_by_css_selector('#fabent-product-options > form:nth-child(1) > table .fabent-product-options-toggle'):
            individualProductNumbers.append(y.text)
            ciu.append(str(driver.current_url))
        for i, v in enumerate(driver.find_elements_by_css_selector('#fabent-product-options > form:nth-child(1) > table  .fabent-product-price')):
            if i % 2 == 1:
                #print(v.text)
                individualProductPrices.append(v.text)
    if driver.find_elements_by_css_selector('#content .products .search_result_title a') != 0:
        for z in driver.find_elements_by_css_selector('#content .products .search_result_title a'):
            print(z.get_attribute('href'))
            individualProductLinks.append(z.get_attribute('href'))#going to need to update if there are more than one page of products
for x in individualProductLinks:
    driver.get(x)
    for y in driver.find_elements_by_css_selector('#fabent-product-options > form:nth-child(1) > table .fabent-product-options-toggle'):
        individualProductNumbers.append(y.text)
        ciu.append(str(driver.current_url))
    for i, v in enumerate(driver.find_elements_by_css_selector('#fabent-product-options > form:nth-child(1) > table  .fabent-product-price')):
        if i % 2 == 1:
            #print(v.text)
            individualProductPrices.append(v.text)

with open('fabItems.py', 'w') as f:
    f.write('numbers = ' + str(individualProductNumbers) + '\n')
    f.write('prices = ' + str(individualProductPrices) + '\n')
    f.write('links = ' + str(ciu))
    f.close()
