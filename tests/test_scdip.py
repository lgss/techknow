import unittest
import time
import random
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

        resultsList = self.browser.find_elements_by_id("container-results")
        self.assertEqual(1, len(resultsList))
    
    def test_questionsRender(self):
        self.test_home()
        assessmentbtn = self.browser.find_element_by_id("btn-home-start-assessment")
        assessmentbtn.click()
        next = self.browser.find_elements_by_name("btn-next")
        next.pop() #no next button on last page
        for btn in next:
            assessment_items = self.browser.find_elements_by_css_selector('.assessment-page.current form .assessment-item')
            self.assertGreater(len(assessment_items),0)
            btn.click()
            time.sleep(1)

    def fill_single_choice_input(self, assessment_item):
        radios = assessment_item.find_elements_by_css_selector('.v-radio')
        self.assertIsNotNone(radios)
        radio = random.choice(radios)
        radio.find_elements_by_css_selector('.v-label')[0].click()
        time.sleep(1)
        selected = "v-item--active" in radio.get_attribute('class')
        self.assertTrue(selected)
        return

    def fill_assessment_item(self, assessment_item):
        fieldtype = assessment_item.find_element_by_css_selector('.container').get_attribute('fieldtype')
        if (fieldtype == "single-choice-input"):
            self.fill_single_choice_input(assessment_item)
    
    def fill_assessment(self):
        assessment_pages = self.browser.find_elements_by_css_selector(".assessment-page")
        for (index, page) in enumerate(assessment_pages):
            assessment_items = self.browser.find_elements_by_css_selector('.assessment-page.current form .assessment-item')
            self.assertIsNotNone(assessment_items, 'No items are present on page {page}'.format(page=index+1))
            for assessment_item in assessment_items:
                self.fill_assessment_item(assessment_item)
            btn = page.find_elements_by_css_selector('*[name="btn-next"], *[name="btn-finish"]')
            btn[0].click()
            time.sleep(1)

    def test_resources_render(self):
        self.test_home()
        assessmentbtn = self.browser.find_element_by_id("btn-home-start-assessment")
        assessmentbtn.click()
        self.fill_assessment()
        time.sleep(1)
        resource_rows = self.browser.find_elements_by_css_selector("#container-results .row")
        self.assertIsNotNone(resource_rows,"No results were found")
    





