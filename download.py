# -*- coding: utf-8 -*-
import requests
import json
import re
import random
import time
import os
from bs4 import BeautifulSoup

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36',
	'Referer': 'http://music.163.com',
	'Host': 'music.163.com'
	}

#主函数
def main():
	SingerId = input('Enter the Singer ID:')
	url = 'http://music.163.com/artist?id={}'.format(SingerId)
	Info = getSongInfo(url)
	IDs = Info['ID']
	i = 0
	for ID in IDs:
		lyric = getLyrics(ID)
		saveLyrics(Info['NAME'][i], lyric)
		i += 1
		time.sleep(random.random() * 3)

#获取网页源代码
def gethtml(url):
	try:
		res = requests.get(url = url, headers = headers) 
	except:
		return None
	return res.text

#获得歌曲信息
def getSongInfo(url):
	html = gethtml(url)
	soup = BeautifulSoup(html, 'lxml')
	links = soup.find('ul', class_='f-hide').find_all('a')
	if len(links) < 1:
		return None
	Info = {'ID': [], 'NAME': []}
	for link in links:
		SongID = link.get('href').split('=')[-1]
		SongName = link.get_text()
		Info['ID'].append(SongID)
		Info['NAME'].append(SongName)
	return Info

# 获取歌词
def getLyrics(SongID):
	ApiUrl = 'http://music.163.com/api/song/lyric?id={}&lv=1&kv=1&tv=-1'.format(SongID)
	html = gethtml(ApiUrl)
	html_json = json.loads(html)
	temp = html_json['lrc']['lyric']
	rule = re.compile(r'\[.*\]')
	lyric = re.sub(rule, '', temp).strip()
	return lyric

#保存歌词
def saveLyrics(SongName, lyric):
	if not os.path.isdir('./song'):
		os.makedirs('./song')
	with open('./song/{}.txt'.format(SongName), 'w', encoding='utf-8') as f:
		f.write(lyric)
		f.close()

main()