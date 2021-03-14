import requests

from bs4 import BeautifulSoup

import string

import os


trans_tab = str.maketrans(string.punctuation + " ", "_" * len(string.punctuation) + "_")
url_root = "https://www.nature.com"
page_count = int(input())
article_type = input()

for page_num in range(1, page_count + 1):
    url = url_root + f"/nature/articles?searchType=journalSearch&sort=PubDate&page={page_num}"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    work_dir = os.getcwd() + f"\\Page_{page_num}"
    if not os.access(work_dir, os.F_OK):
        os.mkdir(work_dir)
    sp1 = soup.find_all("article")
    for article in sp1:
        mt = article.find("span", class_="c-meta__type")
        if mt.get_text() == article_type:
            href = article.find("a")
            news_file = href.get_text().replace("-", "").strip().translate(trans_tab) + ".txt"
            while "__" in news_file:
                news_file = news_file.replace("__", "_")
            print(news_file)
            news_url = url_root + href.get("href")
            req2 = requests.get(news_url)
#            print(news_url)
#            print(req2.status_code)
            if req2.status_code == 200:
                soup2 = BeautifulSoup(req2.content, "html.parser")
                news_content = soup2.find("div", class_="article__body cleared")
                if not news_content:
                    news_content = soup2.find("article", class_="Core--rootElement Theme-Story")
                if not news_content:
                    news_content = soup2.find("div", class_="article-item__body")
                if news_content:
                    with open(work_dir + "\\" + news_file, "w", encoding="utf-8") as file_content:
                        file_content.write(news_content.text.strip())
print("Saved all articles.")
