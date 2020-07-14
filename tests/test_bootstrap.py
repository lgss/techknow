import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os
import platform

environment = None

def loadenv(json_str):
    environment = json.loads(json_str)
    return environment

def loadenvfile(path):
    return loadenv(open(path).read())

class SetupTest(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        if environment == "local":
            self.env = loadenvfile("tests/config.json")
        else:
            self.env = loadenvfile("config.json")

    def setUp(self):
        chrome_options = Options()
        
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1600x1000')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--no-zygote')
        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--enable-logging')
        chrome_options.add_argument('--log-level=0')
        chrome_options.add_argument('--v=99')
        
        chrome_options.add_argument('--ignore-certificate-errors')
        if platform.system() != "Windows":
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--single-process')

        self.browser = webdriver.Chrome(os.path.join(self.env["chrome_driver_path"], "chromedriver" + (".exe" if platform.system() == "Windows" else "")), options=chrome_options)
            
        self.addCleanup(self.browser.quit)