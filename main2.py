import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
    """Retorna o código fonte da URL provida. 

    Args: 
        url (string): URL da página para raspar.

    Returns:
        response (object): HTTP objeto de resposta de requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
        
def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com.br/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https: // www.youtube.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

print(scrape_google("Gabriel"))
