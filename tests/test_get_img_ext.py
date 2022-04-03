import unittest
from downloader.img_downloader import get_img_ext



class TestGetImgExt(unittest.TestCase):

    def test_parse_img_href(self):
        url_jpeg = 'https://sferaglass.com/storage/images/ZCyNe6QvEf.jpeg'
        url_png = 'https://sferaglass.com/storage/images/ZCyNe6QvEf.png'
        url_none = 'https://www.eea.europa.eu/themes/biodiversity/state-of-nature-in-the-eu/state-of-nature-2020-subtopic/image_print'
        self.assertEqual(get_img_ext(url_jpeg), '.jpeg')
        self.assertEqual(get_img_ext(url_png), '.png')
        self.assertEqual(get_img_ext(url_none), '.jpg')

if __name__ == '__main__':
    unittest.main()
