from bs4 import BeautifulSoup
import requests as r

def _download_postings(name: str) -> list:
    """Downloads postings for a company on lever.co

    Arguments:
        name -- The unique ID of the company

    Returns:
        A list of postings from a certain company
    """
    # Note that a companies job postings look like 
    url_template = "https://api.lever.co/v0/postings/{}?mode=json"

    url = url_template.format(name)
    postings = r.get(url).json()

    return postings

def _job_xml_to_rss():
    pass

def main():

    # I got these names by doing the following
    #   1) Searched up "allinurl:jobs.lever.co"
    #   2) Copied every URL that started with "https://jobs.lever.co"
    #   3) Cleaned up the names and got the unique company IDs
    names = ["lever", "stackadapt", "koho", "taplytics", "homestars", "cohere", "atlassian", "invisible", "canva", "Medchart", "lever", "palantir", "wealthsimple", "benchsci", "gojek", "paytm", "yelp", "theathletic", "lime", "sfcg", "geotab", "waveapps", "nielsen", "newton", "arcteryx", "Polygon", "dave", "modsquad"]

if __name__ == "__main__":
    main()