from bs4 import BeautifulSoup
import requests as r

def _job_xml_to_rss():
    pass

def main():
    # Note that a companies job postings look like 
    url_template = "https://api.lever.co/v0/postings/{}?mode=json"

    # I got these names by doing the following
    #   1) Searched up "allinurl:jobs.lever.co"
    #   2) Copied every URL that started with "https://jobs.lever.co"
    #   3) Cleaned up the names and got the unique company IDs
    names = ["lever", "stackadapt", "koho", "taplytics", "homestars", "cohere", "atlassian", "invisible", "canva", "Medchart", "lever", "palantir", "wealthsimple", "benchsci", "gojek", "paytm", "yelp", "theathletic", "lime", "sfcg", "geotab", "waveapps", "nielsen", "newton", "arcteryx", "Polygon", "dave", "modsquad"]


if __name__ == "__main__":
    main()