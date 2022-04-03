import unittest
from downloader.img_downloader import check_img_format
import imghdr
import os

class TestParseImgHref(unittest.TestCase):
    
    
    def test_check_img_format(self):
        file = '/home/alminin/Projects/GoogleImgDownloader/tests/polar+winter-e403f80d-b0b9-437e-aa55-1d957b2cd577.jpeg'
        check_img_format(file)
        self.assertEqual(file, '/home/alminin/Projects/GoogleImgDownloader/tests/polar+winter-e403f80d-b0b9-437e-aa55-1d957b2cd577.jpeg')

if __name__ == '__main__':
    unittest.main()
