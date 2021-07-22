import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    point = tr.select_one('td.point')
    if a_tag is not None:
        title = a_tag.text
        star = point.text
        rank = tr.select_one('td:nth-child(1) > img')['alt']

movie = db.movies.find_one({'title': '매트릭스'},{'_id':False})
print(movie['star'])
print('----------------------------------------')

target_star = movie['star']
same_star = list(db.movies.find({'star' : target_star},{'_id':False}))
for same in same_star :
    print(same['title'])
print('----------------------------------------')
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})