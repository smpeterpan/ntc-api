from bs4 import BeautifulSoup
import requests

data = {'data':[]}

for i in range(1,9):
    url = 'http://www.ntc.ac.th/index.php?page='+str(i)+'&usid=20110025&p=newsblog&textsearch='

    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')
    caption_tag = soup.find_all('b')
    image_pic = soup.find_all('div',{'class':'img-responsive thumbnail'})

    for i in range(len(caption_tag)):
        caption_tag[i] = caption_tag[i].text
        if len(caption_tag[i]) > 17:
            data['data'].append({'caption': caption_tag[i]})
