import logging
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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
driver = webdriver.Chrome(executable_path=r"/home/alminin/WebDrivers/chromedriver_linux64/chromedriver", options=options) #chrome-webdriver must be present in the same directory

driver.get('https://www.google.com/search?q=rose&source=lnms&tbm=isch')

def cfigure_logging():
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

req_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}

session = requests.Session()

def get_query_url(query):
    return 'https://www.google.com/search?q=%s&source=lnms&tbm=isch' % query

def get_soup(url, headers):
    try:
        res = session.get(url, headers=req_headers)
    except requests.exceptions.Timeout:
        logger.info('Timed out to load page')
        logger.exception(e)
    except requests.exceptions.RequestException as e:
        logger.exception(e)
        raise SystemExit(e)  
    soup = BeautifulSoup(res, 'html.parser')
    return soup

def parse_img_href(href):
        pass

def get_img_urls(soup):  
    img_tags = driver.find_elements(By.CSS_SELECTOR, 'a.wXeWr')
    img_tags = img_tags[:num]
    for tag in img_tags: tag.click()
    img_urls = []
    for tag in img_tags:
        href = tag.get_attribute('href')
        if href: 
            print(href) #debug
            #img_ulr = parse_img_href(href)
            img_urls.append(href) # change to img_url
        else: 
            continue
    return img_urls


# /imgres?imgurl=https%3A%2F%2Fwww.greenqueen.com.hk%2Fwp-content%2Fuploads%2F2021%2F06%2FWEF-Investments-In-Nature-Based-Solutions-Have-To-Triple-By-2030-To-Address-Climate-Change-Biodiversity-Loss.jpg&imgrefurl=https%3A%2F%2Fwww.greenqueen.com.hk%2Fnature-climate-investments%2F&tbnid=Py7tBByreru1OM&vet=12ahUKEwi9xZ7-jvD2AhWdAGMBHfE8CywQMygAegUIARC8AQ..i&docid=oCFheJp3fCwmAM&w=1024&h=768&q=nature&ved=2ahUKEwi9xZ7-jvD2AhWdAGMBHfE8CywQMygAegUIARC8AQ

# https%3A%2F%2Fwww.greenqueen.com.hk%2Fwp-content%2Fuploads%2F2021%2F06%2FWEF-Investments-In-Nature-Based-Solutions-Have-To-Triple-By-2030-To-Address-Climate-Change-Biodiversity-Loss.jpg


def main():
    pass

if __name__ == '__main__':
    main()
