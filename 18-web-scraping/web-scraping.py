import requests
import pprint
from bs4 import BeautifulSoup

# read domain.com/robots.txt for 'allowed' scraping for different user agents (* is others)
# crawl-delay is second delay to prevent slow loading website


# crawl articles from hacker news that have 100 points or more
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# examples of some soup methods
soup.title
soup.find(id='score_22517319')
soup.find_all('a')
soup.body.contents

# beautifulsoup css selectors
soup.select('.score')
soup.select('#score_22517319')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda key:key['votes'], reverse=True)

links = soup.select('.storylink')
subtext = soup.select('.subtext')

def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title' : title, 'link' : href, 'votes' : points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))