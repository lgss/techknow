import unittest
from jericho_config import jconfig
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os
import platform

environment = None

def getenv(test_module):
    return environment[test_module]


def setenv(env):
    environment = env

def loadenv(json_str):
    environment = json.loads(json_str)
    return environment


def loadenvfile(path):
    return loadenv(open(path).read())


class JerichoTest(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        if environment is not None:
            self.env = environment[self.__class__.__module__]
        else:
            self.env = loadenvfile("tests/config.json")


    def screen_shot(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        for method, error in self._outcome.errors:
            if error:
                self.browser.get_screenshot_as_file("screenshot" + self.id() + ".png")

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1200,1000')
        chrome_options.add_argument('--ignore-certificate-errors')

        if jconfig.use_system_chrome:
            self.browser = webdriver.Chrome(os.path.join(jconfig.function_root, "./chromedriver" + (".exe" if platform.system() == "Windows" else "")), options=chrome_options)
        else:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--no-zygote')
            chrome_options.add_argument('--hide-scrollbars')
            chrome_options.add_argument('--enable-logging')
            chrome_options.add_argument('--log-level=0')
            chrome_options.add_argument('--v=99')
            chrome_options.add_argument('--single-process')
            chrome_options.add_argument('--data-path=/tmp/data-path')
            chrome_options.add_argument('--user-data-dir=/tmp/user-data')
            chrome_options.add_argument('--homedir=/tmp')
            chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
            chrome_options.binary_location = config.chromium_dir + "chrome"
            self.browser = webdriver.Chrome(config.chromium_dir + 'chromedriver', options=chrome_options)
        self.addCleanup(self.browser.quit)