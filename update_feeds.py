from feedgen.feed import FeedGenerator
from datetime import datetime, timezone
import grequests

def _handle_exception(request, exception):
    print(f"{request} failed with exception {exception}")

def _job_xml_to_rss(name, url, response):
    postings = response.json()

    if not isinstance(postings, list):
        return

    feed = FeedGenerator()
    feed.id(name)
    feed.title(f'{name.title()} Job Postings')
    feed.author({'name':'Thanussian Sharvananthan','email':'thanussian@gmail.com'})
    feed.link(href=url, rel='alternate')
    feed.subtitle(f'Job postings for {name.title()} from lever.co')
    feed.language('en')

    for posting in postings:
        text = posting["text"]
        url = posting["hostedUrl"]
        description = posting["descriptionPlain"]
        pub_date = datetime.fromtimestamp(posting["createdAt"] / 1000, tz=timezone.utc)

        new_entry = feed.add_entry()
        new_entry.title(text)
        new_entry.link(href=url)
        new_entry.description(description)
        new_entry.published(pub_date)

    feed.rss_file(f"feeds/{name.lower()}.rss.xml")

def main():
    # I got these names by doing the following
    #   1) Searched up "allinurl:jobs.lever.co"
    #   2) Copied every URL that started with "https://jobs.lever.co"
    #   3) Cleaned up the names and got the unique company IDs
    names = ["lever", "stackadapt", "koho", "taplytics", "homestars", "cohere", "atlassian", "invisible", "canva", "Medchart", "lever", "palantir", "wealthsimple", "benchsci", "gojek", "paytm", "yelp", "theathletic", "lime", "sfcg", "geotab", "waveapps", "nielsen", "newton", "arcteryx", "Polygon", "dave", "modsquad"]

    urls = [f"https://api.lever.co/v0/postings/{name}?mode=json" for name in names]

    all_requests = (grequests.get(url) for url in urls)

    responses = grequests.imap(all_requests, exception_handler=_handle_exception, size=5)

    for name, url, response in zip(names, urls, responses):
        _job_xml_to_rss(name, url, response)

if __name__ == "__main__":
    main()