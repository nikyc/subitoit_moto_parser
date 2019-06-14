from helpers import url_base, get_no_pages, get_ad_links

# get the max page number
max_page = get_no_pages()

# go through all pages and get ads links
for page_no in range(1, max_page+1):
	# build the current url
	url = url_base + "?o={}".format(page_no)
	
	# get all ad links on the page
	ad_links = get_ad_links(page_no)
	
	# for each link in ad_links, until ad_links empty
	while ad_links:
		link = ad_links.pop()
		print(link)
