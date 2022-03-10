from bs4 import BeautifulSoup
import requests

def get_currency(in_currency,out_currency,amount):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}'
  content = requests.get(url).text
  soup = BeautifulSoup(content,'html.parser')
  currency = soup.find("span", class_="ccOutputRslt").get_text()
  currency = currency[:-4]
  return currency

get_currency('USD','AUD','5000')