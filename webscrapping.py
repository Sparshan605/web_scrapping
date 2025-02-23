import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
'Accept-Language': 'en-US, en;q=0.5'
}
search_query = 'monitor'.replace(' ', '+')
base_url = f'https://www.amazon.com/s?k={search_query}'
name=[]
items=[]
ratings=[]
for i in range(1,5):
    print(f'processing {i}...'+base_url + f'&page={i}')
    response= requests.get(base_url + '&page={0}'.format(i), headers= headers)
    soup=BeautifulSoup(response.content,"html.parser")
    
    n=soup.find_all('span',attrs={'class':'a-size-medium a-color-base a-text-normal'})
    for item in n:
        name.append(item.text)
    sleep(1.5)
    
    n=soup.find_all('span',attrs={'class':'a-size-base s-underline-text'})
    for item in n:
        ratings.append(item.text)
    sleep(1.5)
    
data_dict={'item_name':name,
           'total_reviews':ratings}
df=pd.DataFrame(data_dict)
print(df)
df.to_excel(f'{search_query}.xlsx')