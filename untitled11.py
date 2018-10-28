# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 22:57:59 2018

@author: Jonas
"""

from bs4 import BeautifulSoup
import requests


#1 get all a href from the main web page 
#2 get all the a href form the secondary(s) web page(s) 

def scrape_links(from_url):
    
    source_code = requests.get(from_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html5lib')
    for link in soup.find_all('a'):
        href =   link.get('href')
        print("href on the main page " +  href)
     
        get_href_data(href)



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