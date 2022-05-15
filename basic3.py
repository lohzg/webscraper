from pydoc import text
from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

## Search with single parameter
# tag = doc.find("option")

## Change attribute
# tag["selected"] = "fail"
# tag['color'] = "blue"
# print(tag.attrs)
# print(tag)

## Search with list, text or value
# tags = doc.find_all(["option"], text="Undergraduate", value="undergraduate")
# print(tags)

## Search with class
# tags = doc.find_all(class_="btn-item")
# print(tags)

## Search with regular expression
# tags = doc.find_all(text=re.compile("\$.*"))
# for tag in tags:
#    print(tag.strip())

## Search with regular expression with limit
# tags = doc.find_all(text=re.compile("\$.*"), limit=1)
# for tag in tags:
#    print(tag.strip())


## Save modified html
tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(doc))