import unittest
import image_scraper as ims

class TestSum(unittest.TestCase):
    
    def test_url(self):
        self.assertEqual(ims.url_builder("dog"), 
        "https://www.google.com/search?q=dog&rlz=1C1SQJL_enKR858KR858&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjvyIThp8_qAhUcwosBHb2ZDwAQ_AUoAXoECBgQAw&biw=1920&bih=937",
         "Wrong URL")

if __name__ == '__main__':
    unittest.main()