import os
import requests
from bs4 import BeautifulSoup


def show_banner():
    os.system('clear')
    print("*********************************\nGUZ GETTER - from benhammond.tech\n*********************************")


show_banner()
# Get URL from user
URL = input('Please enter the URL to scrape: ') 
print("looking...")
# URL='https://benhammond.tech'
page = requests.get(URL)

# parse HTTP response
soup = BeautifulSoup(page.content, 'html.parser')

# extract all <a> tags
links = soup.find_all('a')


# get all actual social URLs
social_links = []
for link in links:
    # print(link)
    # print(link.attrs)
    if 'href' in link.attrs:
        website = link.attrs['href']
        # print(website)
        social_links.append(website)


# store possibilities
twitter_url = ""
instagram_url = ""
for social_link in social_links:
    if "twitter" in social_link.lower(): twitter_url = social_link
    if "instagram" in social_link.lower(): instagram_url = social_link


show_banner()
print(f"Twitter: {twitter_url}\nInstagram: {instagram_url}")




