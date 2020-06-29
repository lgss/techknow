from test_bootstrap import SetupTest
import unittest
import time
import random
import json

class PlayerTests(SetupTest):

    def test_one(self):
        self.browser.get(self.env["root"])

        heading = self.browser.find_element_by_tag_name('h1')
        self.assertEqual(heading.text, 'Rekommend Management', 'Title check')

    def test_two(self):
        self.browser.get(self.env["root"])

        tab = self.browser.find_element_by_class_name('v-tab--active')
        self.assertEqual(tab.text, 'GENERAL', 'General tab check')        