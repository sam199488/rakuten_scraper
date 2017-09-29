from builtins import len

from flask import Flask
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

app = Flask(__name__)






def urlify(s):
     # Remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"[^\w\s]", '', s)
     # Replace all runs of whitespace with a '+'
     s = re.sub(r"\s+", '+', s)
     return s

def getResults(item_name = 'luxury handbags', number_pages = 5):
    results = []
    print("query : "+ item_name )
    print("we will scrap from "+str(number_pages)+" pages")
    for i in range(1, number_pages+1):
        search_query = "https://global.rakuten.com/en/search/?p="+str(i)+"&k="+urlify(item_name)+"&l-id=search_regular&vm=1"
        page = urlopen(search_query)
        soup = BeautifulSoup(page, 'html.parser')
        raw_links = soup.find_all("li", class_="b-item")
        print("     processing page "+str(i)+" ,it contains "+str(len(raw_links)))
        for element in raw_links:
            url = 'https://global.rakuten.com' + element.find("div", class_="b-thumb-128px").a['href']
            description = element.find("div", class_="b-content b-fix-2lines").a.get_text()
            price = element.find("span", class_="b-text-prime").get_text()
            picture_url = element.find("div", class_="b-thumb-128px").a.img['src']
            seller_name = element.find("div", class_="b-content b-text-overflow b-text-small b-text-sub").a.get_text()
            seller_url = 'https://global.rakuten.com' + element.find("div", class_="b-content b-text-overflow b-text-small b-text-sub").a['href']
            item = {'url' : url, 'description' : description, 'price' : price, 'picture_url' : picture_url, 'seller_name' : seller_name, 'seller_url' : seller_url}
            results.append(item)
    print("nombre de resultats "+str(len(results)))
    return json.dumps(results)






@app.route('/items')
def hello_world():
    return getResults()


if __name__ == '__main__':
    app.run()
