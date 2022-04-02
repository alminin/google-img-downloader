import unittest
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from img_downloader import get_img_urls


# def get_img_urls(driver, num):
#     img_tags = driver.find_elements(By.CSS_SELECTOR, 'a.wXeWr')
#     img_tags = img_tags[:num]
#     for tag in img_tags: tag.click()
#     img_urls = []
#     for tag in img_tags:
#         href = tag.get_attribute('href')
#         if href: 
#             #img_ulr = parse_img_href(href)
#             img_urls.append(href) # change to img_url
#         else: 
#             continue
#     return img_urls

class TestGetImgUrls(unittest.TestCase):

    def setUp(self):
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
        self.driver = webdriver.Chrome(executable_path=r"/home/alminin/WebDrivers/chromedriver_linux64/chromedriver", options=options)
        
        self.driver.get('https://www.google.com/search?q=rose&source=lnms&tbm=isch')


    def test_get_img_urls(self):
        urls_list = get_img_urls(self.driver, 10)
        self.assertEqual(len(urls_list), 10) # must return 10 urls in a list
        #self.assertIn('wXeWr', tags_list[0].get('class')) # a tag in a list has class wXeWr

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
