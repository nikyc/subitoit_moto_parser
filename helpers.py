import requests
from bs4 import BeautifulSoup as bs4

url_base = "https://www.subito.it/annunci-lombardia-vicino/vendita/moto-e-scooter/"

def get_no_pages():
	'''
	'''
	# read the base url and parse it's content
	response = requests.get(url_base)
	soup = bs4(response.text, "html.parser")
	
	pagination_container = soup.find_all("div", "pagination-container")[0]
	page_links = pagination_container.find_all("a")
	for i in range(len(page_links)-1, -1, -1):
		max_page = page_links[i].text
		if max_page:
			return int(max_page)


def get_ad_links(page_no):
	'''
	'''
	# build the url
	url = url_base + "?o={}".format(page_no)
	
	# read the base url and parse it's content
	response = requests.get(url)
	soup = bs4(response.text, "html.parser")
	
	links = [link["href"] for link in soup.find_all("a") if link["class"][0].find("AdElements__Item")!=-1]
	
	return links
