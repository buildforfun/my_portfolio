import requests
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def return_random_link(url, sub_folder_name):
    """
    Return random url link contained in url given

    Args:
        url
        sub_folder_name 
    """
    # Send a GET request to fetch the webpage
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all anchor tags and extract their href attributes
    links = [urljoin(url, link.get('href')) for link in soup.find_all('a') if link.get('href')]

    # Extracted links
    link_list = []
    print(links)
    for link in links:
        if sub_folder_name in link:
            link_list.append(link)
    
    link_chosen = random.choice(link_list)
    
    return link_chosen
