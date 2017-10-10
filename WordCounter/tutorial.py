import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    sourceCode = requests.get(url)
    plain_text = sourceCode.text.encode('ascii', 'replace')
    soup = BeautifulSoup(plain_text, 'html.parser')
    for post_text in soup.findAll("a",{"class" : "list-group-item"}):
        content = str(post_text.text)
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-='1234567890"
        for i in range(0, len(symbols)) :
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # 2nd key is not talking about the dictionary key , operator works with built in data types ,
    # itemgetter goes to the dictionary and get each item , 1 means value & 0 means key
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, "-" , value)


start('https://thenewboston.com/videos_science.php/')