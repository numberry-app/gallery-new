import json
import requests

from default_widget import default_widget
from random_background import random_background

top_18 = {
	'USD/CAD', 'EUR/JPY', 'EUR/USD', 'EUR/CHF', 'USD/CHF', 'EUR/GBP',
  'GBP/USD', 'AUD/CAD', 'NZD/USD', 'GBP/CHF', 'AUD/USD', 'GBP/JPY',
  'USD/JPY', 'CHF/JPY', 'EUR/CAD', 'AUD/JPY', 'EUR/AUD', 
  'AUD/NZD'
}

for pair in top_18:
  c1, c2 = pair[:3], pair[4:]
  url = 'https://api.exchangeratesapi.io/latest?base={}&symbols={}'.format(c1, c2)

  widget = default_widget
  widget['description'] = 'Track {} exchange rate according to the European Central Bank.'.format(pair)
  widget['value'] = str(json.loads(requests.get(url).content)['rates'][c2])

  widget['request']['url'] = url
  widget['request']['filter'] = '$.rates.{}'.format(c2)

  widget['appearance'] = {
    'title': pair,
    'icon': 'coloncurrencysign.circle.fill',
    'backgroundHex': random_background(),
    'foregroundHex': 0xffffff,
    'prefix': '',
    'suffix': ''
  }

  with open('../content/widgets/currencies_111_{}.json'.format(c1 + c2), 'w+') as widget_file:
    json.dump(widget, widget_file)


#############################################################################################

widget = default_widget
widget['description'] = 'Track any exchange rate published by the European Central Bank.'
widget['value'] = ''

url = 'https://api.exchangeratesapi.io/latest?base={{currency1}}&symbols={{currency2}}'

widget['request']['url'] = url
widget['request']['filter'] = '$.rates.{{currency2}}'

widget['appearance'] = {
  'title': 'Any rate',
  'icon': 'coloncurrencysign.circle.fill',
  'backgroundHex': 0xffffff,
  'foregroundHex': 0x000000,
  'prefix': '',
  'suffix': ''
}

widget['variables'] = ['currency1', 'currency2']
widget['helpText'] = 'Specify three-letter codes for the currencies you want to track the exchange rate for. Supported currencies are USD, EUR, JPY, GBP, AUD, CAD, CHF, HKD, NZD, ISK, PHP, DKK, HUF, CZK, RON, SEK, IDR, INR, BRL, RUB, HRK, THB, MYR, BGN, TRY, CNY, NOK, ZAR, MXN, SGD, ILS, KRW, PLN.'
widget['helpLinks'] = {
  'exchangeratesapi.io': 'https://exchangeratesapi.io',
  'European Central Bank': 'https://www.ecb.europa.eu/'
}

with open('../content/widgets/currencies_111_any.json', 'w+') as widget_file:
  json.dump(widget, widget_file)



