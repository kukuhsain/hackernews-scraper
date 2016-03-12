import requests
from scraper import HackernewsScraper

if __name__ == "__main__":
    url = "https://news.ycombinator.com"
    response = requests.get(url)
    resources = HackernewsScraper(response.content)
    scraped_resources = resources.scrape()
    num = 1
    for res in scraped_resources:
        print(num)
        print(res["title"])
        print(res["link"])
        print(res["host"])
        print(res["score"])
        print(res["by"])
        print(res["age"])
        print(res["comments"])
        num = num+1
