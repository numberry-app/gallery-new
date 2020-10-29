import json
import requests

from default_widget import default_widget
from random_background import random_background

top_25 = {
	'AAPL': 'Apple', 
  'AMZN': 'Amazon', 
  'MSFT': 'Microsoft', 
  'GOOGL': 'Google', 
  'BABA': 'Alibaba', 
	'FB': 'Facebook', 
  'WMT': 'Walmart', 
  'TSLA': 'Tesla', 
  'V': 'Visa', 
  'JNJ': 'Johnson & Johnson',
	'PG': 'Procter & Gamble', 
  'NVDA': 'NVIDIA', 
  'JPM': 'J.P. Morgan', 
  'MA': 'Mastercard', 
  'HD': 'Home Depot',
	'UNH': 'UnitedHealth', 
  'VZ': 'Verizon', 
  'PYPL': 'PayPal', 
  'ADBE': 'Adobe', 
  'CRM': 'Salesforce',
	'DIS': 'Walt Disney Company', 
  'NFLX': 'Netflix', 
  'KO': 'Coca-Cola', 
  'BAC': 'Bank of America', 
  'CMCSA': 'Comcast'
}

endpoint = 'https://api-adapter.backend.currency.com/api/v1/klines'

for ticker, name in top_25.items():
  url = '{}?symbol={}&interval=1m&limit=1'.format(endpoint, ticker)

  widget = default_widget
  widget['description'] = 'Track {} stock price.'.format(name)
  widget['value'] = json.loads(requests.get(url).content)[0][4]

  widget['request']['url'] = url
  widget['request']['filter'] = '$[0][4]'

  widget['appearance'] = {
    'title': ticker,
    'icon': 'chart.bar.fill',
    'backgroundHex': random_background(),
    'foregroundHex': 0xffffff,
    'prefix': '$',
    'suffix': ''
  }

  with open('../content/widgets/stocks_{}.json'.format(ticker), 'w+') as widget_file:
    json.dump(widget, widget_file)




