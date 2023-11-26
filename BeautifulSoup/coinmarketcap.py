from bs4 import BeautifulSoup
import requests
import re


url = "https://coinmarketcap.com/"
result =  requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
Tbody = doc.tbody #get tbody in html
trs = Tbody.contents
trs0 = list(trs[0].descendants) #get toutes les données de 1ʳᵉ table
child_tsr = list(trs[0].children) #get toutes les children de trs[0]
prices = {}
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    print(fixed_price)
    print()
