import random
import urllib.request

def downloadImage(url) :
    name = random.randrange(1,1000)
    fullName = str(name) + ".jpg"
    urllib.request.urlretrieve(url,fullName)

downloadImage("https://realpython.com/learn/python-first-steps/images/pythonlogo.jpg")
