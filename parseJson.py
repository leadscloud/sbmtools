# -*- coding: utf-8 -*-
import os
import re
import httplib
import json
import urllib
import urllib2
import tornado.ioloop
import tornado.web
from string import letters
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def renderJson(query):
	conn = httplib.HTTPConnection('key.eagle-project.org:10093')
	conn.request('GET', '/?query='+ query )
	res = conn.getresponse()
	data = res.read()
	j = json.loads(data)
	results = []
	result = j['data']['group'][0]['resultitem']
	for l in result:
		try:
			results.append(l['word'])
		except KeyError:
			pass
	return results
		
class Search(tornado.web.RequestHandler):
    def get(self):
        self.render("search.html")

    def post(self):
    	query = self.request.Get('query')
    	if query:
    		query = query.encode('UTF-8','ignore')
    		query = urllib.quote(query, safe='/:')
    		self.redirect('/result?query=' + query)

class Result(tornado.web.RequestHandler):
	def get(self):
		query = self.request.Get('query')
		query = query.encode('UTF-8','ignore')
		query = urllib.quote(query, safe='/:')
		self.render('result.html', result = renderJson(query))

application = tornado.web.Application([
                               (r'/search', Search),
							   (r'/result', Result)
                               ])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()