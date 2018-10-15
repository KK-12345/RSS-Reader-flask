from flask.views import MethodView
from flask import render_template
from rss_parse import RSS_FEED
from flask import request


class RSS_Feed(MethodView):

    def get(self):

        url = request.args.get('url', None)
        if not url:
            return 'Please give ?url=<rss_feed_url> as argument'
        rss_feed = RSS_FEED()
        entries = rss_feed.get_data(rss_url=url)
        return render_template('rss_list.html', entries=entries)
