import requests, openpyxl

# Targeted website
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

# Include header info to bypass anti-crawler
headers = {'origin':'https://y.qq.com',
'referer':'https://y.qq.com/portal/search.html',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

# Include params, these parameters should be found in Query String Parameters under XHR
# Most parameters are just from copy&paste, only change value of "p" so that I can get as many pages as I want. 
for num in range (1,3):
    params = {'ct': '24',
'qqmusic_ver': '1298',
'remoteplace': 'txt.yqq.lyric',
'searchid': '96529858210962475',
'aggr': '0',
'catZhida': '1',
'lossless': '0',
'sem': '1',
't': '7',
# Using for loop to change the number of pages
'p': str(num),
'n': '5',
# Singer name
'w': '周杰伦',
'g_tk_new_20200303': '5381',
'g_tk': '5381',
'loginUin': '0',
'hostUin': '0',
'format': 'json',
'inCharset': 'utf8',
'outCharset': 'utf-8',
'notice': '0',
'platform': 'yqq.json',
'needNewCode': '0'}

    # Initiate request, include headers and params defined above
    res = requests.get(url, headers = headers, params= params)
    # Convert to json
    lists = res.json()
    # Extract wanted info
    context = lists['data']['lyric']['list']
    for i in context:
        print(i['content'])
