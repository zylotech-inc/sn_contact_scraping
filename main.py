from navigation import *
from readinig_and_writing import *
from parsing_scraped_result import *

def scrapingcontacts():
    """Reads input, scrapes contacts and saves in sqlite db by calling other functions.
    """
    
    inputdata = readinginput() # Reading input file from folder
    company = inputdata[0]     # Reading all companies in the list
    filter = inputdata[1]      # Reading all filters in the list
    code = inputdata[2]        # Reading all code in the list 

    driver = startingbrowser() # Starting Browser instance  
    time.sleep(5)
    

    for eachcompany, eachfilter, eachcode in zip(company,filter,code):
        url = eachfilter
        driver.get(url)
        time.sleep(3)
        
        # counting all elements to move to the last element to scroll down. 
        try:
            element_count = len(driver.find_element_by_id("search-results-container").find_elements_by_class_name("artdeco-list__item"))
            all_element = driver.find_element_by_id("search-results-container").find_elements_by_class_name("artdeco-list__item")[element_count-1]
            all_element.location_once_scrolled_into_view
       
            htmlpage = driver.page_source
            htmlparse(htmlpage,eachcode,eachcompany) # passing html to function to parse data
        except:
            pass
scrapingcontacts()


       