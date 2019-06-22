import requests
from bs4 import BeautifulSoup as soup

# my_url = 'https://www.essentracomponents.com/en-us/access-hardware/hinges/leaf-flag-hinges/leaf-flag-fixed-position-hinges'
my_url = 'https://www.essentracomponents.com/en-us/access-hardware/hinges/leaf-flag-hinges/leaf-flag-torque-hinges'

r = requests.get(my_url)
html_page = r.text
page_soup = soup(r.text, 'html.parser')

page_containers = page_soup.find_all("div", {"class":"list_item row"})

filename = page_soup.find('div', {'class':'span9'}).h1.text.strip() + ".csv"
f = open(filename, "w")
headers = "product_name, product_short_description, product_image, product_stock_staus, number_of_sub_products\n"
f.write(headers)

counter = 1

for container in page_containers:
    product_name = container.find("div", {"class":"span6 prod_info"}).p.text.strip()
    product_short_description = container.find("div", {"class":"content"}).text.strip()
    product_image =  container.find("div", {"class":"fullimage"}).img['src']
    product_stock_staus = container.find("div", {"class":"span2 extro"}).p.text.strip()
    number_of_sub_products_string = container.find("a", {"class":"itemVarBtn"}).span.text.strip()
    number_of_sub_products = int(''.join(filter(str.isdigit, str(number_of_sub_products_string))))

    print(counter)
    print(product_name)
    print(product_short_description)
    print(product_image)
    print(product_stock_staus)
    print(number_of_sub_products)
    counter +=1

    f.write(product_name + ", "+ product_short_description +", "+ product_image +", "+ product_stock_staus +", " + str(number_of_sub_products) +"\n")
f.close()
