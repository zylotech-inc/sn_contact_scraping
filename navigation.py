from lib2to3.pgen2 import driver
from logging import exception
from selenium import webdriver
import time
from readinig_and_writing import reading_cred


def startingbrowser(): 
    """ Starts chrome browser instance and logins to linkedin.
    
    Param:
        None
    Returns:
        object: chrome driver instance.
    """
    try:
        id = reading_cred()[0]
        password =reading_cred()[1]
    except:
        raise Exception("Check login ID or Password")

    try:
        driver = webdriver.Chrome()
        driver.get('https://www.linkedin.com/uas/login')
        driver.find_element_by_id("username").send_keys(id)
        time.sleep(2)
        driver.find_element_by_id("password").send_keys(password)
        time.sleep(2)
        driver.find_element_by_class_name("btn__primary--large").click()
        driver.get("https://www.linkedin.com/sales/search/people?query=(recentSearchParam%3A(id%3A1281201281%2CdoLogHistory%3Atrue)%2Cfilters%3AList((type%3AREGION%2Cvalues%3AList((id%3A103644278%2Ctext%3AUnited%2520States%2CselectionType%3AINCLUDED)))%2C(type%3ACURRENT_COMPANY%2Cvalues%3AList((text%3Azylotech%2CselectionType%3AINCLUDED)))%2C(type%3ASENIORITY_LEVEL%2Cvalues%3AList((id%3A6%2Ctext%3ADirector%2CselectionType%3AINCLUDED)%2C(id%3A8%2Ctext%3ACXO%2CselectionType%3AINCLUDED)%2C(id%3A5%2Ctext%3AManager%2CselectionType%3AINCLUDED)%2C(id%3A7%2Ctext%3AVP%2CselectionType%3AINCLUDED)))))&sessionId=Y%2BFvawF7SiS0wE%2FKHPn7RA%3D%3D&viewAllFilters=true")
        print("logged in successfully")
    except:
        raise exception ("Check Chrome driver or internet connection")
    return driver
