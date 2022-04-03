import unittest
from downloader.img_downloader import get_img
from downloader.img_downloader import save_img
import os
import glob


class TestSaveImg(unittest.TestCase):

    def setUp(self):
        res = get_img('https://sferaglass.com/storage/images/ZCyNe6QvEf.jpeg')
        save_img(res, 'nature', '.jpeg', 'Download')
    
    def test_save_img(self):
        self.assertTrue(os.path.exists('Download'))
        self.assertTrue(glob.glob('Download/*.jpeg'))

if __name__ == '__main__':
    unittest.main()