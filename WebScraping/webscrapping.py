from builtins import print
import requests
from bs4 import BeautifulSoup
from csv import writer

# variable initialization
url = 'https://www.whatmobile.com.pk/'
uri = ''
brand_uri = ''
brand_list = []
brand_uri_list = []
brands_specs_dict = {}
brands_mobile_list = []


def html_parse(url):
    ''' For parsing html page on given url '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

try:
    div = html_parse(url).find('div', {'class': 'verticalMenu'})
except requests.exceptions.RequestException as e:
    print(e)
else:
    section_search_by_branch = div.find_all('section')[1]
    brands = section_search_by_branch.find('ul').find_all('li')
    for i in brands:
        brand_list.append((i.find('a').string, i.find('a')['href']))
    dict = list(enumerate(brand_list))
    if dict:  # If dictionary is not empty
        print('Choose brand of mobile you want to WebScrap?\n')
        for i in dict:
            print(i[0], ':', i[1][0])
        brand_selection = input('Enter your choice: ')

        for i in range(0, (len(brand_list) - 1)):
            if (brand_list[i][0] == brand_selection.rstrip()):
                uri = url + brand_list[i][1]
                break
        if uri:
            try:
                td = html_parse(uri).find_all('td', {'class': 'BiggerText'})
            except requests.exceptions.RequestException as e:
                print(e)
            else:
                for i in td:
                    brand_uri = url + i.find('a')['href']
                    brand_uri_list.append(brand_uri)
        else:
            print('oops ! something went wrong...')
    else:
        print('oops ! something went wrong...')

if brand_uri_list:
    for i in brand_uri_list:
        try:
            table = html_parse(i).find('table', {'class': 'specs'}) #table for specs
            div_price = html_parse(i).find('div', {'class': 'hdng3'})

            price_text = div_price.text.replace(' ','').replace(',','').strip()
            index_of_usd = price_text.index('U')
            str_to_lst = list(price_text)
            a = str_to_lst.insert(int(index_of_usd),',')
            lst_to_str = ''.join(str_to_lst).split(',')

            #Splitting dollars and rupees in seperate var
            price_rs = lst_to_str[0].replace('Rs.','')
            price_usd = lst_to_str[1].replace('USD$', '')

        except requests.exceptions.RequestException as e:
            print(e)
        else:
            tr = table.find_all('tr')
            for j in tr:
                th = j.select('th')
                td = j.select('th+td')
                for k, brand_specs_list in zip(th, td):
                    spec = k.text.strip()
                    value = brand_specs_list.text.strip()
                    brands_specs_dict[spec] = value
            mobile = i.split('//')
            brands_specs_dict['Brand'] = brand_selection
            brands_specs_dict['Mobile'] = mobile[2]
            brands_specs_dict['Price_RS'] = price_rs
            brands_specs_dict['Price_USD'] = price_usd

            brands_mobile_list.append(brands_specs_dict.copy())
else:
    print('oops ! something went wrong...')
# Set of all unique specifications of all mobiles of selected brand

brand_specs_list = []
all_brands_specs_list = []

if brands_mobile_list:
    specs_set = set()
    for p in brands_mobile_list:
        specs_set = set(p.keys())
        specs_set = specs_set.union(specs_set)
    for i in specs_set:
        for j in brands_mobile_list:
            if i in j.keys():
                brand_specs_list.append(j.get(i))
            else:
                brand_specs_list.append('Not Found')
        brand_specs_list.insert(0, i)
        all_brands_specs_list.append(brand_specs_list.copy())
        brand_specs_list.clear()
else:
    print('oops ! something went wrong...')

# Transponse of list for csv purposes
trans_list = []
if all_brands_specs_list:
    trans_list = list(map(list, zip(*all_brands_specs_list)))
else:
    print('oops ! something went wrong...')

# Saving list in cvs format
filename = brand_selection + '.csv'

if filename:
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            data_handler = writer(f, delimiter=',')
            for i in trans_list:
                data_handler.writerow(i)
    except IOError as e:
        print(e)
    else:
        print('Congratulations !',brand_selection,'has been scrapped in', filename, 'sucessfully...')
else:
    print('oops ! something went wrong...')
