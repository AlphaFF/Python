#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re,time
import os,json
import base64
from Crypto.Cipher import AES
from pprint import pprint
import binascii

#成功爬取了网易云音乐的评论过total的音乐id/音乐名/歌手名

headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Host':'music.163.com',
	'Referer':'https://music.163.com/',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
}

url = 'https://music.163.com/'

_session = requests.session()
_session.headers.update(headers)

def getPage(pageIndex):
	pageUrl = 'http://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset='+pageIndex
	soup = BeautifulSoup(_session.get(pageUrl).content,'lxml')
	songList = soup.findAll('a',attrs={'class':'tit f-thide s-fc0'})
	for i in songList:
		print(i['href'])
		getPlayList(i['href'])

def getPlayList(playListId):
	playListUrl = url + playListId
	soup = BeautifulSoup(_session.get(playListUrl).content,'lxml')
	songList = soup.find('ul',attrs={'class':'f-hide'})
	for i in songList.findAll('li'):
		startIndex = (i.find('a'))['href']
		songId = startIndex.split('=')[1]
		readEver(songId)

	# songList = soup.find('tbody')
	# if songList:
	# 	for i in songList.findAll('tr'):
	# 		startIndex = (i.find('a'))['href']
	# 		songId = startIndex.split('=')[1]
	# 		readEver(songId)
	# else:
	# 	print('wrong')


def getSongInfo(songId):
	pageUrl = url + '/song?id=' + songId
	soup = BeautifulSoup(_session.get(pageUrl).text,'lxml')
	strArr = soup.title.string.split('-')
	name = strArr[0].strip()
	singer = strArr[1].strip()
	return name,singer

# 由于网易云音乐歌曲评论采取AJAX填充的方式所以在HTML上爬不到，需要调用评论API，而API进行了加密处理，下面是相关解决的方法
def aesEncrypt(text,secKey):
	pad = 16 - len(text) % 16
	text = text + pad * chr(pad)
	encryptor = AES.new(secKey,2,'0102030405060708')
	ciphertext = encryptor.encrypt(text)
	ciphertext = base64.b64encode(ciphertext)
	return ciphertext

def rsaEncrypt(text,pubKey,modulus):
	text = text[::-1]
	# rs = int(text.encode('hex'),16)**int(pubKey,16)%int(modulus,16)
	rs = int(binascii.hexlify(text.encode()), 16) ** int(pubKey, 16) % int(modulus, 16)
	return format(rs,'x').zfill(256)

def createSecretKey(size):
	return (''.join(map(lambda xx:(hex(xx)[2:]),os.urandom(size))))[0:16]


def readEver(songId):
	url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_'+str(songId)+'/?csrf_token=12d75aaad5399b36bd99e19c7564b87e'
	headers = {'Cookie': 'appver=1.5.0.75771;', 'Referer': 'http://music.163.com/'}
	text = {'username': 'liushahedi@163.com', 'password': '31415926fw', 'rememberLogin': 'true'}
	modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
	nonce = '0CoJUm6Qyw8W8jud'
	pubKey = '010001'
	text = json.dumps(text)
	secKey = createSecretKey(16)
	encText = aesEncrypt(aesEncrypt(text, nonce).decode(), secKey)
	encSecKey = rsaEncrypt(secKey, pubKey, modulus)
	data = {'params': encText, 'encSecKey': encSecKey}
	req = requests.post(url, headers=headers, data=data)
	total = req.json()['total']
	if int(total) > 10000:
		name,singer = getSongInfo(songId)
		print(songId,total,name,singer)
	else:
		pass

if __name__ == '__main__':
	for i in range(1,43):
		getPage(str(i*35))







