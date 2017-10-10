import requests
from bs4 import BeautifulSoup

url = "https://thenewboston.com/search.php"

def trade_spide(max_pages) :
    page = 1
    while page <= max_pages :
        tempUrl = url + "?page=" + str(page)
        sourceCode = requests.get(tempUrl)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for f in soup.findAll("a",{"class" : "user-name"}) :
            href = f.get("href")
            title = f.string
            print(title + "  " + href)
        page += 1



trade_spide(1)