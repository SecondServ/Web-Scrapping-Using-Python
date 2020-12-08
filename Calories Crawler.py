from gevent import monkey
monkey.patch_all()
import requests,csv,gevent
from bs4 import BeautifulSoup
from gevent.queue import Queue

url_list = []
for i in range(1,4):
    for x in range(1,4):
        url = 'http://www.boohee.com/food/group/'+str(i)+'?page='+str(x)
        url_list.append(url)

line = Queue()
for url in url_list:
    line.put_nowait(url)
print(type(line))
def pa():
    while not line.empty():
        url = line.get_nowait()
        res = requests.get(url)
        bs = BeautifulSoup(res.text, 'html.parser')
        foodlist = bs.find_all('li',class_="item clearfix")
        
        for food in foodlist:
            name = food.find('h4').text.strip()
            cal = food.find('p').text.strip()
            link = food.find('a')['href'].strip()
            url = 'http://www.boohee.com'+link
            
            with open(r'c:\Users\Administrator\Desktop\foodcal.csv', 'a', newline = '', encoding = 'utf-8-sig') as f1:
                writer = csv.writer(f1)
                writer.writerow([name, cal, url])
            

tasks = []
for i in range(3):
    task = gevent.spawn(pa())
    tasks.append(task)
gevent.joinall(tasks)

