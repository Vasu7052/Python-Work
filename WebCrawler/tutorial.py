import requests
from bs4 import BeautifulSoup

url = "https://thenewboston.com/search.php"

def trade_spider1(max_pages) :
    page = 1
    while page <= max_pages :
        tempUrl = url + "?page=" + str(page)
        sourceCode = requests.get(tempUrl)
        plain_text = sourceCode.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text, 'html.parser')
        for f in soup.findAll("a",{"class" : "user-name"}) :
            href = f.get("href")
            title = f.string
            print(title + "  " + href)
        page += 1


def get_single_item(url) :
    sourceCode = requests.get(url)
    plain_text = sourceCode.text.encode('ascii', 'replace')
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll("span",{"class" : "text-semibold"}) :
        print(item_name.string)
    print("All Links : ")
    for item_name in soup.findAll("a") :
        print(item_name.get("href"))

# trade_spider1(2)

get_single_item("https://thenewboston.com/profile.php?user=522")