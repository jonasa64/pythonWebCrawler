from bs4 import BeautifulSoup
import requests


# get all a href from the main web page 


def scrape_links(from_url):
    
    source_code = requests.get(from_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html5lib')
    for link in soup.find_all('a'):
        href =   link.get('href')
        print("href on the main page " +  href)
     
        get_href_data(href)


#get all the a href form the secondary(s) web page(s) 
def get_href_data(href_url):
    try:
        source_code = requests.get(href_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'html5lib')
        for link in soup.find_all('a'):
            href = link.get('href')
            print("secondary href " + href)
       
    except:
       pass
            
scrape_links("https://www.pythonforbeginners.com")
