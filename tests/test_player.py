from test_bootstrap import SetupTest
import unittest
import time
import random
import json

class PlayerTests(SetupTest):

    def test_one(self):
        self.browser.get(self.env["root"])

        heading = self.browser.find_element_by_id("title")
        self.assertEqual(heading.text, 'Welcome to techKNOW', 'Title Check')

    def test_two(self):
        self.browser.get(self.env["root"])
        time.sleep(10)
        assessmentbtn = self.browser.find_elements_by_id("btn-home-start-assessment")
        self.assertEqual(len(assessmentbtn), 1)       