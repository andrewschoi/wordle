import requests
from bs4 import BeautifulSoup
from googlesearch import search
import string


words = []
res = requests.get('https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt')
soup = soup = BeautifulSoup(res.text, 'html.parser')
td = soup.find_all('td')
for w in td:
    words += [w.text]

punc = {}
for p in string.punctuation:
    punc[ord(p)] = ""


query = "wordle answer today"
links = search(query, tld="co.in", num=20, stop=20, pause=2)

guess = ""
for url in links:
    try:
        print('searching {}'.format(url))
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        b = soup.find_all('b')
        for elem in b:
            word = elem.text.lower().translate(punc)
            if(word in words):
                guess = word
    except:
        print('error with link {}'.format(url))

print("\nguess: {}".format(guess))
