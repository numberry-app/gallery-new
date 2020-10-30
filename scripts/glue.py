import os
import json

sections = {
  'social_': 'Social',
	'stocks_': 'Stocks',
  'crypto_': 'Crypto',
  'currencies_': 'Currencies'
}

content = { 'sections': [] }

for prefix, title in sections.items():
  widgets = []

  for widget_file_name in sorted(os.listdir('../content/widgets/')):
    if widget_file_name.startswith(prefix):
      with open('../content/widgets/{}'.format(widget_file_name)) as widget_file:
        widgets.append(json.load(widget_file))

  content['sections'].append({
    'title': title,
    'icon': '',
    'widgets': widgets
  })

with open('../content/content.json', 'w+') as content_file:
  json.dump(content, content_file)

