import csv

from bs4 import BeautifulSoup as BS
import requests
import lxml


def get_response(url, headers):
    return requests.get(url=url, headers=headers)


def return_soup(html):
    return BS(html, "lxml")


def get_product_card(soup, item=1):
    product_items = soup.find("div", "products-grid").find_all("li")
    return product_items[item]


def get_products_list_size(soup):
    product_items = soup.find("div", "products-grid").find_all("li")
    return len(product_items)


def get_name_card_product(soup):
    return soup.find("div", "product-item-details").find("strong", "product-item-name").find("a").text.strip()


def get_link_card_product(soup):
    return soup.find("div", "product-item-details").find("strong", "product-item-name").find("a").get("href").strip()


def get_price_card_product(soup):
    return soup.find("div", "product-item-details").find("span", "price").text.strip()


def get_category_name(soup):
    return soup.find("div", "page-title-wrapper").find("span", "base").text.strip()


def crete_csv():
    with open("cards.csv", 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(('Назва',
                         'Категрія',
                         'Ціна',
                         'Посилання'
                         ))


def write_csv(data):
    with open("cards.csv", 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow((data['name'],
                         data['category'],
                         data['price'],
                         data['href']
                         ))


def get_data(url, headers):
    crete_csv()
    soup = return_soup(get_response(url, headers).text)
    for item in range(get_products_list_size(soup)):
        card = get_product_card(soup, item)
        name = get_name_card_product(card)
        price = get_price_card_product(card)
        category = get_category_name(soup)
        link = get_link_card_product(card)
        print(f"Товар №{item} \nКатегорія '{category}' - Назва: '{name}' \nЦіна: {price}")
        print(f"Посилання: {link}")
        print()
        data = {
            'name': name,
            'category': category,
            'price': price,
            'href': link
        }
        write_csv(data)


def main():
    headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0'
            }
    url = "https://magento.softwaretestingboard.com/men/tops-men.html"
    print(get_response(url, headers).status_code)

    get_data(url=url, headers=headers)


if __name__ == "__main__":
    main()
