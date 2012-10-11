#Finish crawl web

def add_to_index(index,keyword,url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return 
	index.append([keyword,[url]])

def lookup(index,word):
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return []

def add_page_to_index(index,url,content):
	words = content.split()
	for word in words:
		add_to_index(index,word,url)

def get_page(url):
	try:
		if url == "http://www.com":
			return '<html>...</html>'
		elif url == "http://wwx.com":
			return '<html>...</html>'
	except:
		return ""
	return ""

def get_next_target(page):
	start_link = page.find('<a href=>')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url,end_quote

def union(p,q):
	for e in q:
		if e not in p:
			p.append(e)

def get_all_links(page):
	links = []
	while True:
		url,endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			union(tocrawl, get_all_links(page))
			crawled.append(page)
	return crawled

