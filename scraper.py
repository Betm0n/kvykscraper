from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.firefox.options import Options as FirefoxOptions

def initiatedriver():
    options = FirefoxOptions()
    options.add_argument("--headless")     
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options = options)  # <--- To run the driver without opening a broser window
    #driver = webdriver.Firefox(options=options)
    return driver

def pricecheckamazon(driver, keyword):  #AMAZON SCRAPER
    web = 'https://www.amazon.in/s?k='
    driver.get(web+keyword.replace(' ','+'))
    #driver.implicitly_wait(2)

    items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
    for item in items:
    #find price
        price = item.find_elements(By.XPATH, './/span[@class="a-price-whole"]')
        amazon_product_price = price[0].text
        break



    return amazon_product_price

def pricecheckflipkart(driver, keyword):    #FLIPKART SCRAPER
    web = 'https://www.flipkart.com/search?q='
    driver.get(web+keyword.replace(' ','+'))
    #driver.implicitly_wait(2)
    
    items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "_13oc-S")]')))
    for item in items:
    #find price
        try:
            price = item.find_element(By.XPATH, './/div[@class="_30jeq3 _1_WHN1"]')
        except:
            price = item.find_element(By.XPATH, './/div[@class="_30jeq3"]')
        flipkart_product_price = price.text
        break



    return flipkart_product_price

def pricechecksnapdeal(driver, keyword):    #SNAPDEAL SCRAPER
    web = 'https://www.snapdeal.com/search?keyword='
    driver.get(web+keyword.replace(' ','+'))
    #driver.implicitly_wait(2)

    items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "col-xs-6  favDp product-tuple-listing js-tuple ")]')))
    for item in items:
    #find price
        try:
            price = item.find_elements(By.XPATH, './/span[@class="lfloat product-price"]')
        except:
            price.append(0)
        snapdeal_product_price = price[0].text
        break



    return snapdeal_product_price

def driverquit(driver):
    driver.quit()