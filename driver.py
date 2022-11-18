from emailin import *
from emailout import *
from filemod import *
from scraper import *


def driver():
    driver = emailin()
    print(driver)
    filemod(driver)
    emailout(driver)
    

driver()