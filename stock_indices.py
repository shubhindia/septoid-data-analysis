import pandas as pd
import requests
from bs4 import BeautifulSoup
url = 'https://www.investing.com/indices/major-indices'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
result = requests.get(url, headers=header)
soup = BeautifulSoup(result.text, features="lxml")
table = soup.find("table", attrs={"id":"QBS_2_inner"})
headings = [th.get_text() for th in table.find("tr").find_all("th")]
datasets = []
for row in table.find_all("tr")[1:]:
    dataset = list(zip(headings, (td.get_text() for td in row.find_all("td"))))
    datasets.append(dataset)
print(datasets)