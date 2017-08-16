import requests
from bs4 import BeautifulSoup

# get the hacker news front page
request = requests.get("http://news.ycombinator.com")
soup = BeautifulSoup(request.text, "html.parser")
links = soup.select("a.storylink")

for link in links:
    print(link.text, "\n        =>", link["href"])
