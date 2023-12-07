"""script for scraping unsplash; only for educational purposes"""
import os
import sys
from enum import Enum
from pathlib import Path

import lxml
import requests
from bs4 import BeautifulSoup as bs


class Colors(Enum):
    """colors escape codes
    https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803
    """
    BLACK = "\u001b[30m"
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    RESET = "\u001b[0m"


def colored(text: str, color: str) -> str:
    """return colored text"""
    if color in Colors.__members__:
        color = Colors[color].value
        return f"{color}{text}{Colors.RESET.value}"
    return text


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
        return False
    return response.content


def search(phrase: str) -> list:
    """get urls of unsplash images for specified phrase

    for now (v.0.1.1) 25% of urls are not available for download
    in case of 20 unique urls only 15 will be downloaded
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    search_url = f'https://unsplash.com/s/photos/{phrase}' 
    res = requests.get(search_url, headers=headers)
    soup = bs(res.text, "lxml")
    base_url = 'https://unsplash.com'
    urls = soup.find_all('a', href=True)
    SUFFIX_LEN = 11
    urls = [
        f"{base_url}/photos/{url['href'][-SUFFIX_LEN:]}"
        for url in urls
        if url['href'].startswith('/photos/')
    ]
    download_suffix = '/download?force=true'
    urls = [f"{url}{download_suffix}" for url in urls]
    urls = sorted(set(urls))  # remove duplicates
    return urls


def example():
    """example of use"""
    main(args=['cherry'])
    return None


def main(args=None):
    """main cli function"""
    if args is None:
        args = sys.argv[1:]
        if not args:
            print('usage: unsplash_get.py <word>')
            sys.exit(1)
    if os.name == 'nt':
        os.system('color')
    word = args[0]
    urls = search(word)
    print(f"word: {colored(word, 'GREEN')}, unique urls found: {len(urls)}")
    directory = Path(word)
    directory.mkdir(parents=True, exist_ok=True)
    for index, url in enumerate(urls, start=1):
        out = f'{word}_{index:03}.jpg'
        path = directory / out
        status = save_img(url, path)
        color = 'GREEN' if status else 'RED'
        print(f"{index:03}.{colored(url, 'CYAN')} -> {path} ({colored(status, color)})")


if __name__ == "__main__":
    example()
