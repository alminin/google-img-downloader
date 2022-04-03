import unittest
from downloader.img_downloader import parse_img_href

href = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fsferaglass.com%2Fstorage%2Fimages%2FZCyNe6QvEf.jpeg&imgrefurl=https%3A%2F%2Fsferaglass.com%2Fprojects%2Fnature&tbnid=r5CavR1d3332DM&vet=12ahUKEwivsODUwPP2AhXAVPEDHW5TAvAQMygAegUIARC8AQ..i&docid=Xy1hGEdh1neuIM&w=1100&h=734&q=nature&ved=2ahUKEwivsODUwPP2AhXAVPEDHW5TAvAQMygAegUIARC8AQ'
href2 = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fnatureconservancy-h.assetsadobe.com%2Fis%2Fimage%2Fcontent%2Fdam%2Ftnc%2Fnature%2Fen%2Fphotos%2FWOPA160517_D056-resized.jpg%3Fcrop%3D864%2C0%2C1728%2C2304%26wid%3D600%26hei%3D800%26scl%3D2.88 '
href3 = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fth-thumbnailer.cdn-si-edu.com%2FvSnitgUqCQCRSx7mkHZtHZHry4U%3D%2F1072x720%2Ffilters%3Ano_upscale()%2Fhttps%3A%2F%2Ftf-cmsv2-smithsonianmag-media.s3.amazonaws.com%2Ffiler%2F04%2F8e%2F048ed839-a581-48af-a0ae-fac6fec00948%2Fgettyimages-168346757_web.jpg&imgrefurl=https%3A%2F%2Fwww.smithsonianmag.com%2Fscience-nature%2Fwhy-listening-sounds-nature-can-be-restorative-180977397%2F&tbnid=_aZds14GQGy_fM&vet=12ahUKEwij8Jyt__X2AhWhQvEDHcveD50QMygJegUIARDKAQ..i&docid=CislBCIV4PvswM&w=1072&h=720&q=nature&ved=2ahUKEwij8Jyt__X2AhWhQvEDHcveD50QMygJegUIARDKAQ'
class TestParseImgHref(unittest.TestCase):

    def test_parse_img_href(self):
        url = parse_img_href(href)
        url2 = parse_img_href(href2)
        url3 = parse_img_href(href3)
        self.assertEqual(url, "https://sferaglass.com/storage/images/ZCyNe6QvEf.jpeg")
        self.assertEqual(url2, "https://natureconservancy-h.assetsadobe.com/is/image/content/dam/tnc/nature/en/photos/WOPA160517_D056-resized.jpg")
        self.assertEqual(url3, 'https://th-thumbnailer.cdn-si-edu.com/vSnitgUqCQCRSx7mkHZtHZHry4U%3D/1072x720/filters:no_upscale()/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/04/8e/048ed839-a581-48af-a0ae-fac6fec00948/gettyimages-168346757_web.jpg')

if __name__ == '__main__':
    unittest.main()

