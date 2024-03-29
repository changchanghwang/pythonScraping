import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    ranks = tr.select_one('td.number')
    titles = tr.select_one('td.info > a.title.ellipsis')
    artists = tr.select_one('td.info > a.artist.ellipsis')
    rank = ranks.text[0:2].strip()
    title = titles.text.strip()
    artist = artists.text.strip()

first = db.musicChart.find_one({'rank':'1'})
print(first['title'],'ㅣ',first['artist'])
print('-----------------------------------')

IUs = list(db.musicChart.find({'artist' : '아이유 (IU)'},{'_id':False}))
for IU in IUs :
    print(IU['title'])