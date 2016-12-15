import os
import sys
import urllib
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as BS
import re

head="http://m.mzitu.com/page/"
linkList=[]
def getLinks(url):
	try:

		html=urlopen(url)
	except urllib.error.HTTPError:
		pass
	bsObj=BS(html,"html.parser")
	links=bsObj.findAll("a",{"href":re.compile("com\/[0-9]+$")})
	for link in links:
		if link["href"] not in linkList:
			linkList.append(link["href"])
	return linkList



def imageUrls(link):
	try:

		html=urlopen(link)
		bsObj=BS(html,"html.parser")
		image=bsObj.find("a",{"href":re.compile("\/[0-9]+\/[0-9]+$")})
		imgUrl=image.img["src"]
		return imgUrl
	except urllib.error.HTTPError:
		pass
	
	


def getImage(urls,dir_name):
	x=1
	for i in urls:
		i=imageUrls(i)
		try:
				
			urlretrieve(i,'./%s/%s.jpg' % (dir_name,str(x)))
		except (urllib.error.HTTPError,TypeError):
			pass
		
		print("第%s张美图已经下载完成" % str(x))
		x+=1
	return x-1


'''for i in range(1):
	getLinks(head+str(i+1))
x=getImage(linkList)'''

def main(page,dir_name='images'):
	if dir_name not in os.listdir('.'):
		os.mkdir(dir_name)
	for i in range(int(page)):
		getLinks(head+str(i+1))
	getImage(linkList,dir_name)


if __name__=='__main__':
	if len(sys.argv)<2:
		print("Usage:python crawler.py pages [dir_name]")
	elif len(sys.argv)==2:
		main(sys.argv[1])
	else:
		main(sys.argv[1],sys.argv[2])









