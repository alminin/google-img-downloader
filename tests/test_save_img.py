import unittest
from downloader.img_downloader import get_img
from downloader.img_downloader import save_img
import os
import glob
import requests
import uuid


class TestSaveImg(unittest.TestCase):

    def setUp(self):
        # url = 'https://sferaglass.com/storage/images/ZCyNe6QvEf.jpeg'
        # req_headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
        # }
        # dir = 'Download'

        # with requests.get(url, headers=req_headers, stream=True) as res:
        #     if res.status_code == 200:
        #         file_name = str(uuid.uuid4()) + 'jpeg'
        #         if not os.path.exists('Download'):
        #             os.mkdir(os.path.join('.', dir))
        #         path = os.path.join(dir, file_name)
        #     with open(path, 'wb') as f:
        #         # res.raw.decode_content = True
        #         # shutil.copyfileobj(res.raw, f)
        #         for chunk in res:
        #            f.write(chunk)

        res = get_img('https://sferaglass.com/storage/images/ZCyNe6QvEf.jpeg')
        print(len(res.content))
        print(res.headers)
        save_img(res, '.jpeg', 'Download')
    
    def test_save_img(self):
        self.assertTrue(os.path.exists('Download'))
        self.assertTrue(glob.glob('Download/*.jpeg'))

if __name__ == '__main__':
    unittest.main()