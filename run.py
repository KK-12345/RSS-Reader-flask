import sys
from flask import Flask, request
from views import RSS_Feed
import os

app = Flask(__name__, template_folder='templates')

app.add_url_rule('/rss_feed/', view_func=RSS_Feed.as_view('rss_list'), methods=['GET'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)