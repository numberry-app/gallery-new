import json
import requests

from default_widget import default_widget
from random_background import random_background

top_25 = {
	'BTC': 'Bitcoin', 
  'ETH': 'Ethereum', 
  'XRP': 'Ripple', 
  'BCH': 'Bitcoin Cash', 
  'LINK': 'Chainlink', 
	'BNB': 'Binance Coin', 
  'LTC': 'Litecoin', 
  'DOT': 'Polkadot', 
  'ADA': 'Cardano',
	'EOS': 'EOS', 
  'XMR': 'Monero', 
  'TRX': 'TRON', 
  'XLM': 'Stellar', 
  'XTZ': 'Tezos',
	'NEO': 'Neo', 
  'ATOM': 'Cosmos', 
  'DAI': 'Dai', 
  'VET': 'VeChain',
	'DASH': 'Dash', 
  'ETC': 'Ethereum Classic', 
  'THETA': 'THETA', 
  'ZEC': 'Zcash', 
  'COMP': 'Compound',
  'ONT': 'Ontology',
  'WAVES': 'Waves'
}

for code, name in top_25.items():
  url = 'https://www.binance.com/api/v3/ticker/price?symbol={}USDT'.format(code)

  widget = default_widget
  widget['description'] = 'Track {} price.'.format(name)
  widget['value'] = json.loads(requests.get(url).content)['price']

  widget['request']['url'] = url
  widget['request']['filter'] = '$.price'

  widget['appearance'] = {
    'title': code,
    'icon': 'chart.bar.fill',
    'backgroundHex': random_background(),
    'foregroundHex': 0xffffff,
    'prefix': '$',
    'suffix': ''
  }

  with open('../content/widgets/crypto_111_{}.json'.format(code), 'w+') as widget_file:
    json.dump(widget, widget_file)


#############################################################################################

widget = default_widget
widget['description'] = 'Track price of any cryptocurrency listed on Binance.'
widget['value'] = ''

url = 'https://www.binance.com/api/v3/ticker/price?symbol={{symbol}}'

widget['request']['url'] = url
widget['request']['filter'] = '$.price'

widget['appearance'] = {
  'title': 'Any coin',
  'icon': 'chart.bar.fill',
  'backgroundHex': 0xffffff,
  'foregroundHex': 0x000000,
  'prefix': '$',
  'suffix': ''
}

widget['variables'] = ['symbol']
widget['helpText'] = 'Specify symbol for the cryptocurrency you want to track price of.'
widget['helpLinks'] = {
  'Binance API docs': 'https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md'
}

with open('../content/widgets/crypto_111_any.json', 'w+') as widget_file:
  json.dump(widget, widget_file)



