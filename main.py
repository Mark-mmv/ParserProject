import requests
from bs4 import BeautifulSoup

PAGES_COUNT = 1

def get_soup(url, **kwargs):
    headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"}
    response = requests.get(url, headers=headers)
    print(response.text)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features='html.parser')
    else:
        soup = None
    return soup

def crawl_apartments(pages_count):
    urls = []
    fshablon = 'https://www.sreality.cz/en/search/for-sale/apartments?page={page}/css/all.css?7163eb3'

    for page_number in range(1, pages_count+1):
        print('page: {}'.format(page_number))

        page_url = fshablon.format(page=page_number)
        soup = get_soup(page_url)
        #print(soup.body)
        if soup is None:
            break
        for tag in soup.select('h2'):
            href = tag.attrs['href']
            url = 'https://www.sreality.cz{}'.format(href)
            urls.append(url)

    return urls

def parse_apartments(urls):
    data = []
    return data


def main():
    urls = crawl_apartments(PAGES_COUNT)
    print('\n'.join(urls))
    print(322)
    data = parse_apartments(urls)


if __name__ == '__main__':
    main()


