from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-12gd/p/N82E16814932489?Description=gigabyte%203080&cm_re=gigabyte_3080-_-14-932-489-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)