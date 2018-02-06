import requests
import os
from bs4 import BeautifulSoup

URL = "https://xkcd.com/"
PATH = "Desktop/XKCD"
FILE = "XKCD"

if not os.path.exists(PATH):
	os.makedirs(PATH)
os.chdir(PATH)

for counter in range(1,1000):
	r = requests.get(URL+str(counter))
	soup = BeautifulSoup(r.content,'html5lib')
	get_src = soup.findAll('img')[1].attrs
	src = 'http:'+ get_src['src']
	r = requests.get(src)
	img_name = FILE + str(counter) + ".png" 
	with open(img_name,"wb") as f:
		f.write(r.content)