from bs4 import BeautifulSoup
from readinig_and_writing import saveoutput
import re


def htmlparse(pagesource,code,company):

    """Parses html to text and scrapes details (contact name, title, company, profile url)

    Args:
        pagesource (str): Html/ Page source of the browser instance
        code (str): Predifined Codes in the file
        company (str): Company to scrape contacts

    Returns:
        None: Saves scraped data in sqlite db
    """
  
    htmltext = pagesource
    soup = BeautifulSoup(htmltext,'html.parser')

    try:
        # Element which has all result of the page, contacts name, title, company, profile url
        allresult = soup.find(id="search-results-container").find_all(class_="artdeco-list__item")
        
        # storing all available contacts count to scrape more pages if required 
        morecontacts = soup.find(class_="ml3 pl4 t-14 t-black--light flex _display-count-spacing_1igybl").text
        morecontacts = morecontacts.lstrip().rstrip()
    except:
        pass
    
    try: 

        for each in allresult:

            try:
                # Contact name element
                name = each.find(class_='artdeco-entity-lockup__title').get_text()
                name = name.strip().lstrip().rstrip()

            except:
                name = ".."    

            try:
                # Contact Profile url element
                profile = 'https://www.linkedin.com/'+each.find(class_='artdeco-entity-lockup__title').find('a').get('href')
            except:
                profile = ".."    

            try:
                # Contact title element
                title_and_Company = each.find(class_='artdeco-entity-lockup__subtitle').get_text()
                title_and_Company = title_and_Company.lstrip().rstrip().replace('\n\n\n',"~~").split("~~")
                title = title_and_Company[0]    
            
            except:
                title = "" 

            try:
                # Contact Company element
                title_and_Company = each.find(class_='artdeco-entity-lockup__subtitle').get_text()
                title_and_Company = title_and_Company.lstrip().rstrip().replace('\n\n\n',"~~").split("~~")
                contactcompany = title_and_Company[1].lstrip().rstrip()
            except:
                contactcompany= ".."

            try:   
                # Contact location element  
                location = each.find(class_='artdeco-entity-lockup__caption').get_text()
                location = re.sub(' +',' ',location.replace('\n',"").strip().lstrip().rstrip())
            except:
                location = ".."
            
            try:
                # Output Company profile url element 
                contactcompanyurl = 'https://www.linkedin.com/s'+ each.find(class_='artdeco-entity-lockup__subtitle').find('a').get('href')
            except:
                contactcompanyurl= ".." 

            # storing all result in list to pass to db function
            outputlist = [code,company,name,title,contactcompany,location,profile,morecontacts,contactcompanyurl]
            
            # Calling db function to save output in sqlite db
            saveoutput(outputlist)  
    except:
        print("company not found")
        pass            

