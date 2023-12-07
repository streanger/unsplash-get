"""script for scraping unsplash; only for educational purposes"""
import os
import sys
import lxml
import requests
from bs4 import BeautifulSoup as bs


def save_img(url: str, path: str) -> bool:
    """save image from specified url, to specified local path"""
    response = requests.get(url)
    if response.status_code != 200:
        return False
    with open(path, 'wb') as f:
        f.write(response.content)
    return True


def get_image(url: str) -> bytes:
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.content


def search(phrase: str) -> list:):
    """get urls of unsplash images for specified phrase"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    search_url = 'https://unsplash.com/s/photos/' + phrase
    res = requests.get(search_url, headers=headers)
    soup = bs(res.text, "lxml")
    
    base_url = 'https://unsplash.com'
    urls = soup.find_all('a', href=True)
    urls = [(base_url + url['href']) for url in urls if url['href'].startswith('/photos/')]
    post_script = '/download?force=true'
    urls = [(url + post_script) for url in urls]
    return urls


def example():
    """example of use"""
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    word = 'cherry'
    urls = search(word)
    print('word: {}, urls number: {}'.format(word, len(urls)))

    for key, url in enumerate(urls[:3]):
        out = '{}_{:03}.jpg'.format(word, key)
        print('{:03}.{} -> {}'.format(key, url, out))
        save_img(url, out)
    return None


if __name__ == "__main__":
    example()
