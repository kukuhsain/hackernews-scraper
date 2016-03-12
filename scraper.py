from bs4 import BeautifulSoup

class HackernewsScraper():
    def __init__(self, response):
        self.response = response

    def scrape(self):
        soup = BeautifulSoup(self.response, "html5lib")

        title_items = soup.find("table", {"class": "itemlist"}).find_all("tr", {"class": "athing"})
        subtext_items = soup.find("table", {"class": "itemlist"}).find_all("td", {"class": "subtext"})

        n = 1
        resources = []
        for title_item in title_items:
            subtext_item = subtext_items[n-1]
            resources.append({
                "link": title_item.find_all("td", {"class": "title"})[1].find("a").get("href"),
                "title": title_item.find_all("td", {"class": "title"})[1].find("a").text,
                "host": title_item.find_all("td", {"class": "title"})[1].find("span", {"class": "sitestr"}).text,
                "score": subtext_item.find("span", {"class": "score"}).text,
                "by": subtext_item.find("a").text,
                "age": subtext_item.find("span", {"class": "age"}).text,
                "comments": subtext_item.find_all("a")[-1].text,
            })
            n=n+1
        return resources