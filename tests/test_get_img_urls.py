import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
from downloader.img_downloader import get_img_urls


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
        self.assertTrue(re.search(r'imgurl', urls_list[2])) # href string has 'imgurl' substring

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()



