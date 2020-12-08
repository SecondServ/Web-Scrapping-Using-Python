from gevent import monkey
monkey.patch_all()
import requests,csv,gevent
from bs4 import BeautifulSoup
from gevent.queue import Queue

url_list = []
# Use for loop to append all targeted urls to url_list
for i in range(1,4):
    for x in range(1,4):
        # Use for loops to set category number and page number
        url = 'http://www.boohee.com/food/group/'+str(i)+'?page='+str(x)
        url_list.append(url)

# Create queue instance
line = Queue()
for url in url_list:
    # Add urls to the queue
    line.put_nowait(url)

# Define a crawler function
def pa():
    # Add headers to bypass anti-crawler
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    # Extract urls from the queue
    while not line.empty():
        url = line.get_nowait()
        # Get HTML source code
        res = requests.get(url, headers = headers)
        # Parser code using BeautifulSoup
        bs = BeautifulSoup(res.text, 'html.parser')
        # Extract content in <li class="item clearfix">
        foodlist = bs.find_all('li',class_="item clearfix")
        
        for food in foodlist:
            # Use find_all, extract the value inside <h4> element under <li class="item clearfix">
            name = food.find('h4').text.strip()
            # Use find_all, extract the value inside <p> element under <li class="item clearfix">
            cal = food.find('p').text.strip()
            # Use find_all, extract the value of 'href' inside <p> element under <li class="item clearfix">
            link = food.find('a')['href'].strip()
            # Concatenate links
            url = 'http://www.boohee.com'+link
            # Write gathered info into csv files
            with open(r'c:\Users\Administrator\Desktop\foodcal.csv', 'a', newline = '', encoding = 'utf-8-sig') as f1:
                writer = csv.writer(f1)
                writer.writerow([name, cal, url])
            
# Create an empty task list
tasks = []
# Create 3 crawlers
for i in range(3):
    # Use gevent.spawn() function to spawn and execute crawler() function
    task = gevent.spawn(pa())
    # Append task into the list
    tasks.append(task)
# Use gevent.joinall to initiate coroutine, execute all the tasks in the list
gevent.joinall(tasks)

