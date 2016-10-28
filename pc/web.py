from bs4 import BeautifulSoup

with open('/home/cb/HtmlProject/test.html','r')as web_data:
    Soup=BeautifulSoup(web_data,'lxml')
    images=Soup.select('body > div.main-content > ul > li > img')
    titles=Soup.select('body > div.main-content > ul > li > h3')
    print images,titles

for i,t in zip(images,titles):
    data={
        'title':t.get_text(),
        'image':i.get('src')
    }
    print data