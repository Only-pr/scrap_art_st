from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time,requests,re,csv

driver = webdriver.Firefox(service=Service(
    r"C:\your_driver_way\geckodriver.exe"))

with open('art_station.csv','w', encoding="utf-8",newline='') as file:
    writter = csv.writer(file, delimiter=';')
    writter.writerow(
        (
            "name",
            "link"
        )
    )

try:
    for i in range(5):
        page = i
        url = f"https://www.artstation.com/api/v2/community/explore/projects/latest.json?page={page}&dimension=all&per_page=30"
        driver.get(url=url)
        time.sleep(7)

        with open("art_s.html",'w',encoding='utf-8') as file:
            file.write(driver.page_source)

        with open('art_s.html','r',encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src,'lxml')
        tree_art = soup.find_all('div', class_='panelContent')

        for i in tree_art:
            name = i.find_all('tr', {'class':'treeRow','id':re.compile('full_name')})
            link = i.find_all('tr', {'class':'treeRow','id':re.compile('url')})
            list_name = []
            list_link = []

            for g in name:
                name_1 = g.find('span',class_='objectBox')
                list_name.append(name_1.text)

            for k in link:
                ur = k.find('a',class_= 'url').get('href')

                if 'https://www.artstation.com/'  in ur:
                    list_link.append(ur)
                else:
                    continue

            for i,k in zip(list_name,list_link):

                with open('art_station.csv','a', encoding="utf-8",newline='') as file:
                    writter = csv.writer(file, delimiter=';')
                    writter.writerow(
                        (
                            i,
                            k
                        )
                    )


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()