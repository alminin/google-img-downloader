import logging
from typing import List
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import uuid
from urllib.parse import urlparse
import argparse
import imghdr


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu") 
options.add_argument("--disable-software-rasterizer")
options.add_argument("--dns-prefetch-disable") 
options.add_argument("--disable-browser-side-navigation"); 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(executable_path=r"/home/alminin/WebDrivers/chromedriver_linux64/chromedriver", options=options)

def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('[%(asctime)s %(levelname)s %(module)s]: %(message)s'))
    logger.addHandler(handler)
    filehandler = logging.FileHandler("log.txt") 
    filehandler.setFormatter(
        logging.Formatter('[%(asctime)s %(levelname)s %(module)s]: %(message)s'))
    logger.addHandler(filehandler)

    return logger

logger = configure_logging()

def get_query_url(query):
    return 'https://www.google.com/search?q=%s&source=lnms&tbm=isch' % query

def parse_img_href(href: str) -> str:
    ''' Extracts img url from href and returns it '''
    full_query = urlparse(href).query
    imgurl = full_query.split('&')[0]
    url = imgurl.split('=')[1].replace(r'%2F', r'/').replace(r'%3A', ':')
    url = url.split(r'%3F')[0]
    return url

def get_img_urls(query_url, num_pages: int) -> List:  
    ''' Gets num images urls '''
    driver.get(query_url)
    logger.info(f'Extracting img urls on {query_url}')
    img_tags = driver.find_elements(By.CSS_SELECTOR, 'a.wXeWr')
    img_tags = img_tags[:num_pages]
    for tag in img_tags: tag.click()
    img_urls = []
    for tag in img_tags:
        href = tag.get_attribute('href')
        if href: 
            img_ulr = parse_img_href(href)
            img_urls.append(img_ulr)
        else: 
            continue
    driver.close()
    return img_urls

def get_img(url: str) -> requests.Response:
    ''' Makes get request to url and returns response '''

    req_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
    }

    try:
        with requests.get(url, headers=req_headers) as res:
            return res
    except requests.exceptions.Timeout:
        logger.info('Timed out to load page')
        logger.exception(e)
    except requests.exceptions.RequestException as e:
        logger.exception(e)
        raise SystemExit(e)  

def get_img_ext(url: str) -> str:
    path = urlparse(url).path
    ext = os.path.splitext(path)[1]
    #ext = ext if ext else '.jpg'
    return ext

def check_img_format(file_path: str):
    ''' Checks image file's type and change extension if needed '''
    ext = imghdr.what(file_path)
    if ext == None: ext = 'webp'
    file_name = os.path.splitext(os.path.abspath(file_path))[0]
    full_file_name = file_name+'.'+str(ext)
    os.rename(file_path, full_file_name)

def save_img(res: requests.Response, keyword: str, ext: str, dir: str):
    ''' Saves response raw to file with unique name and chosen extension.
    Args:
    res - Response object from GET request to img url
    ext - files extension with dot
    dir - directory to save img files'''

    file_name = keyword + '-' + str(uuid.uuid4()) + ext
    if not os.path.exists(dir):
        os.mkdir(os.path.join('.', dir))
    path = os.path.join(dir, file_name)
    if res.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in res:
                f.write(chunk)
        logger.info('Saving images')
        check_img_format(path)
    
def run(query: str, dir: str, num: int) -> None:
    ''' Runs script. 
    Args: 
    query - search keyword to find images 
    dir - directory to save img files 
    num - number of images'''
    query = '+'.join(query.split())
    query_url = get_query_url(query)
    img_urls = get_img_urls(query_url, num)
    for url in img_urls:
        res = get_img(url)
        ext = get_img_ext(url)
        save_img(res, query, ext, dir)
    logger.info(f'Finished! {num} {query} images have been saved.')

def main():
    parser = argparse.ArgumentParser(description='Search and download images')
    parser.add_argument('-s', '--search', default='nature', type=str, help='search keyword')
    parser.add_argument('-n', '--num_images', default=5, type=int, help='number of images to save')
    parser.add_argument('-d', '--directory', default='Download', type=str, help='save directory')
    args = parser.parse_args()
    run(args.search, args.directory, args.num_images)


if __name__ == '__main__':
    main()
