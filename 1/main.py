import time

from bs4 import BeautifulSoup as BS
import requests
import lxml


def get_response(url, headers):
    return requests.get(url=url, headers=headers)


def return_soup(html):
    return BS(html, "lxml")


def get_h2_data(soup):
    h2 = soup.find("div", "content-heading").find("h2")
    return h2.text


def main():
    headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0'
            }
    url = "https://magento.softwaretestingboard.com"
    print(get_response(url, headers).status_code)
    soup = return_soup(get_response(url, headers).text)
    h2 = get_h2_data(soup)
    print(h2)


if __name__ == "__main__":

    main()