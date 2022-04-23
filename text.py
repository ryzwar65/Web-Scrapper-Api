import requests

tokped_url = 'https://www.shopee.co.id/'
keyword = 'kemeja pria'

header = {
  'User-Agent' : 'Chrome',
  'Referer' : '{}search?keyword={}'.format(tokped_url,keyword)
}

url = 'https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword={}&limit=100&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2'.format(keyword)

r = requests.get(url,headers=header).json()

cols_list = []

for item in r['items']:
  cols_list.append(item['item_basic']['name'])
  
print(cols_list)
print(len(cols_list))