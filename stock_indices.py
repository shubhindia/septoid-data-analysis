import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml.html as lh
url = 'https://www.investing.com/indices/major-indices'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
result = requests.get(url, headers=header)
soup = BeautifulSoup(result.text, features="lxml")
datasets = []
for row in soup.find_all('tr'):
    for col in row.find_all('td'):
        info = col.text
        print(info)
        
