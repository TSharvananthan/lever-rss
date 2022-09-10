from bs4 import BeautifulSoup
import requests as r
from feedgen.feed import FeedGenerator

def _job_xml_to_rss(name: str):
    url = f"https://api.lever.co/v0/postings/{name}?mode=json"

    feed = FeedGenerator()
    feed.title(f'{name.title()} Job Postings')
    feed.author({'name':'Thanussian Sharvananthan','email':'thanussian@gmail.com'})
    feed.link(href=url, rel='alternate')

    postings = postings = r.get(url).json()

    for posting in postings:
        new_entry = feed.add_entry()
        new_entry.title(posting["text"])
        new_entry.link(href=posting["hostedUrl"])
        new_entry.description(posting["descriptionPlain"])

    feed.rss_file(f"{name.lower()}.rss.xml")


def main():
    # I got these names by doing the following
    #   1) Searched up "allinurl:jobs.lever.co"
    #   2) Copied every URL that started with "https://jobs.lever.co"
    #   3) Cleaned up the names and got the unique company IDs
    names = ["lever", "stackadapt", "koho", "taplytics", "homestars", "cohere", "atlassian", "invisible", "canva", "Medchart", "lever", "palantir", "wealthsimple", "benchsci", "gojek", "paytm", "yelp", "theathletic", "lime", "sfcg", "geotab", "waveapps", "nielsen", "newton", "arcteryx", "Polygon", "dave", "modsquad"]

    print(_job_xml_to_rss("wealthsimple"))

if __name__ == "__main__":
    main()