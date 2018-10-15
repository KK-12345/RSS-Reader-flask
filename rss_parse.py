import feedparser
import os
import unidecode


class RSS(object):
    """
    RSS object
    """
    def __init__(self, title, link, website, summary, all_data):
        self.title = title
        self.link = link
        self.all_data = all_data
        self.website = website
        self.summary = summary


class RSS_FEED(object):

    def get_data(self, rss_url):
        """
        Parse RSS feed and send it for displaying
        """
        data=[]
        feed = feedparser.parse(rss_url)
        if not feed:
            return 'RSS feeds are not available'
        try:
            website = feed["feed"]["title"]
        except KeyError:
            raise Exception('Feed or title is not available')

        for key in feed["entries"]:
            title = unidecode.unidecode(key["title"])
            link = key["link"]
            summary = key["summary"]
            data.append(RSS(title, link, website, summary, key))
        return data


