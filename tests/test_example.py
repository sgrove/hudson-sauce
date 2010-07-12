from selenium import selenium
import unittest

raw = open("saucelabs_account", "r").read().partition("\n")

saucelabs_username = raw[0]
saucelabs_password = raw[2][0:-1]

class sauce(unittest.TestCase):
    def setUp(self):
        print """{\
                "username": "%s",\
                "access-key": "%s",\
                "os": "Windows 2003",\
                "browser": "firefox",\
                "browser-version": "3.",\
                "job-name": "This is an example test"\
                }""" % (saucelabs_username, saucelabs_password)
                 
        self.browser = selenium(
                'saucelabs.com',
                4444,
                """{\
                        "username": "%s",\
                        "access-key": "%s",\
                        "os": "Windows 2003",\
                        "browser": "firefox",\
                        "browser-version": "3.",\
                        "job-name": "This is an example test"\
                    }""" % (saucelabs_username, saucelabs_password),
                    'http://www.saucehudson.com/')
        self.browser.start()
        self.browser.set_timeout(90000)
        
    def test_sauce(self):
        browser = self.browser
        browser.open("/")
        while True:
            self.assertEqual("Hello, Hudson and Sauce!",
                    browser.get_title())
    
    def tearDown(self):
        self.browser.stop()

if __name__ == "__main__":
    unittest.main()
