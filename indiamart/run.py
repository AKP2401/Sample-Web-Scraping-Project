import requests
from bs4 import BeautifulSoup

def run():
    jj = 0
    page = requests.get('https://dir.indiamart.com/')

    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find_all(class_="dirDib dirExplHed dirFwB dirFs14 dirClr8 hovrTdU")

    Titles = []
    URLS = []

    for i in result:
        Titles.append(i.text)
        URLS.append(i['href'])
    jsun = {}
    for i in range(len(URLS)):
        page = requests.get(URLS[i])

        soup = BeautifulSoup(page.content, 'html.parser')

        resname = soup.find_all('a', class_="pnm ldf cur")
        resph = soup.find_all('span', class_="ls_co phn bo")
        resloc = soup.find_all(class_="srad cty-t")  

        jin =  {Titles[i]:["++++"]}
        for i in range(len(resname)):
            jin[resname[i].text] = [int(resph[i].text[-10:]), resloc[i].text]
            print(jj)
            jj+=1
        jsun.update(jin)

    print()
    print(f'{len(jsun)} Unique Sellers')
    return jsun

