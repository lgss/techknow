import unittest
import time
from test_bootstrap import JerichoTest

class ScdipTests(JerichoTest):

    def test_home(self):
        self.browser.get(self.env["root"])

        heading = self.browser.find_element_by_id("title")
        self.assertEqual(heading.text, 'Welcome to techKNOW', 'Title Check')

        assessmentbtn = self.browser.find_elements_by_id("btn-home-start-assessment")
        self.assertEqual(len(assessmentbtn), 1)

    def test_results(self):
        self.test_home()
        assessmentbtn = self.browser.find_element_by_id("btn-home-start-assessment")
        assessmentbtn.click()

        next = self.browser.find_elements_by_name("btn-next")
        next.pop() #no next button on last page
        for btn in next:
            btn.click()
            time.sleep(1)

        finish = self.browser.find_elements_by_name("btn-finish")
        finish[-1].click()

        dtable = self.browser.find_elements_by_class_name("v-data-table")
        self.assertEqual(1, len(dtable))