from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import requests
import json
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import requests
import bs4
import re
import os


class Bot():
    def scrap(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable--dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
        df = pd.read_csv('ITI_DATA_pri.csv')

        name = []
        email = []
        contact =  []
        for i in range(1000,1400):
            try:
                self.browser.get(df["more_details"][i])
                self.browser.execute_script("window.scrollTo(0, 1000)")
                name.append(self.browser.find_element_by_xpath('//span[@id="lblprinciple"]').text)
                email.append(self.browser.find_element_by_xpath('//span[@id="lblPrincipalEmail"]').text)
                contact.append(self.browser.find_element_by_xpath('//span[@id="lblPrincipleMobo"]').text)
            except:
                name.append('')
                email.append('')
                contact.append('')
            print(i)

        df1 = pd.DataFrame({"name":name,"email":email,"contact":contact})
        df1.to_csv("details_from_1000_to_1400.csv")


b = Bot()
b.scrap()
