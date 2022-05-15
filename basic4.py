from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

prices = {}

## need to find how to search after 10
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

print(prices)

## print next sibling
# #print(trs[0].next_sibling)

## print previous sibling
# print(trs[1].previous)

## print next siblings, need to change to list as the return type is object
# print(list(trs[0].next_siblings))

## print parent content
# print (trs[0].parent)

## print parent name
# print (trs[0].parent.name)

## print children
# print (list(trs[0].children))
