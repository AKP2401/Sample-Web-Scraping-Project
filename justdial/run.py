from bs4 import BeautifulSoup

numb = {
        'mobilesvicon-acb' : '0',
        'mobilesvicon-yz' : '1',
        'mobilesvicon-wx' : '2',
        'mobilesvicon-vu' : '3',
        'mobilesvicon-ts' : '4',
        'mobilesvicon-rq' : '5',
        'mobilesvicon-po' : '6',
        'mobilesvicon-nm' : '7',
        'mobilesvicon-lk' : '8',
        'mobilesvicon-ji' : '9',
        'mobilesvicon-dc' : '+',
        'mobilesvicon-ba' : '-',
        'mobilesvicon-fe' : '(',
        'mobilesvicon-hg' : ')',
}    


def calc(resnum):
    num = ''
    if resnum.b is None:
        for j in resnum.a:
            d = ''
            for ele in j['class']:
                d+=ele
            num+=numb[d]
    else:
        for j in resnum.b:
            d = ''
            for ele in j['class']:
                d+=ele
            num+=numb[d]
    return num



def run():
    file = open('justdial/jd.html','r', encoding='utf-8')
    soup = BeautifulSoup(file, 'html.parser')

    resname = soup.find_all(class_='jcn')
    resadd = soup.find_all(class_='cont_fl_addr')
    resnum = soup.find_all(class_='contact-info')

    res = {}
    try:
        for i in range(len(resname)):
            res[resname[i].a['title']] = [calc(resnum[i]), resadd[i].text]
    except:
        pass

    return res

run()