import unittest
from selenium import webdriver
from downloader.img_downloader import get_img_urls
import validators


class TestGetImgUrls(unittest.TestCase):

    def test_get_img_urls(self):
        query_url = 'https://www.google.com/search?q=rose&source=lnms&tbm=isch'
        urls_list = get_img_urls(query_url, 10)
        self.assertEqual(len(urls_list), 10) # must return 10 urls in a list
        for url in urls_list:
            self.assertTrue(validators.url(url)) # validate strings as urls in urls_list

if __name__ == '__main__':
    unittest.main()



