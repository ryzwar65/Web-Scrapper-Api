import requests

tokped_url = 'https://www.tokopedia.com/'
keyword = 'macbook pro 2015'

header = {
  'User-Agent' : 'Chrome',
  'Referer' : '{}search?keyword={}'.format(tokped_url,keyword)
}

url = 'https://www.tokopedia.com/search?st=product&q={}&srp_component_id=02.01.00.00&navsource=home'.format(keyword)

r = requests.get(url,headers=header).json()

print(r)

# cols_list = []

# for item in r['items']:
#   cols_list.append(item['item_basic']['name'])
  
# print(cols_list)