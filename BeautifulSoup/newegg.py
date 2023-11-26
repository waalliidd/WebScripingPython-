from bs4 import BeautifulSoup
import requests
import re
search_terms  = input("What product do you want search for ")
url = f"http://newegg.ca/p1?d={search_terms}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
page_text = doc.find(class_="list-tool-pagination-text")
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
item_found = {}
for page in range(1, pages+1):
    url = f"https://www.newegg.ca/p/p1?d={search_terms}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    items = doc.find_all("div", class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cells")


    for item in items:
        parent = item.parent

        if parent.name !='a':
            continue
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        price = next_parent.find(class_="item-current").strong.string
        item_found[item]= {"price":int(price.replace(",", "")),
                             "link": link}
    print(item_found)

sorted_items = sorted(item_found.items(), lambda x:x[1][price])
for item in sorted_items:
    print(item[0])

