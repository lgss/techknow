import unittest
import time
import random
from test_bootstrap import JerichoTest
import json

class ScdipTests(JerichoTest):
    CURRENT_PAGE_SELECTOR = '.assessment-page.current form .assessment-item'

    def test_home(self):
        self.browser.get(self.env["root"])

        heading = self.browser.find_element_by_id("title")
        self.assertEqual(heading.text, 'Welcome to techKNOW', 'Title Check')

        assessmentbtn = self.browser.find_elements_by_id("btn-home-start-assessment")
        self.assertEqual(len(assessmentbtn), 1)

    def test_results(self):
        self.test_home()
        self.start_assessment()

        next = self.browser.find_elements_by_name("btn-next")
        next.pop() #no next button on last page
        for btn in next:
            btn.click()
            time.sleep(1)
        
        finish = self.browser.find_elements_by_name("btn-finish")
        finish[-1].click()

        resultsList = self.browser.find_elements_by_id("container-results")
        self.assertEqual(1, len(resultsList))
    
    def test_questions_render(self):
        self.test_home()
        self.start_assessment()
        next = self.browser.find_elements_by_name("btn-next")
        next.pop() #no next button on last page
        for btn in next:
            assessment_items = self.browser.find_elements_by_css_selector(self.CURRENT_PAGE_SELECTOR)
            self.assertGreater(len(assessment_items),0)
            btn.click()
            time.sleep(1)

    def fill_single_choice_input(self, value=None, assessment_item=0):
        if isinstance(assessment_item, int):
            group = self.browser.find_elements_by_css_selector(f'{self.CURRENT_PAGE_SELECTOR} .v-input--radio-group')[assessment_item]
        else:
            group = assessment_item 

        radios = group.find_elements_by_css_selector('.v-radio')
        self.assertIsNotNone(radios)

        if value is None:
            radio = random.choice(radios)
        else:    
            for radio in radios:
                if radio.text == value:
                    radio.click()

                    selected = "v-item--active" in radio.get_attribute('class')
                    self.assertTrue(selected)
                    break
    
    def fill_multi_choice_input(self, value=None, assessment_item=0):
        if isinstance(assessment_item, int):
            group = self.browser.find_elements_by_css_selector(self.CURRENT_PAGE_SELECTOR)[assessment_item]
        else:
            group = assessment_item

        checkboxes = group.find_elements_by_css_selector('.v-input--checkbox')
        self.assertIsNotNone(checkboxes)

        if value is None:
            check = random.choice(checkboxes)
        else:
            for v in value:
                for check in checkboxes:
                    if check.text == v:
                        check.find_element_by_class_name('v-input--selection-controls__ripple').click()

                        selected = 'v-input--is-label-active' in check.get_attribute('class')
                        self.assertTrue(selected)
                    
    def fill_assessment_item(self, assessment_item, value=None):
        fieldtype = assessment_item.find_element_by_css_selector('.container').get_attribute('fieldtype')
        if (fieldtype == "single-choice-input"):
            self.fill_single_choice_input(assessment_item)
    
    def fill_assessment(self):
        assessment_pages = self.browser.find_elements_by_css_selector(".assessment-page")
        for (index, page) in enumerate(assessment_pages):
            assessment_items = self.browser.find_elements_by_css_selector(self.CURRENT_PAGE_SELECTOR)
            self.assertIsNotNone(assessment_items, 'No items are present on page {page}'.format(page=index+1))
            for assessment_item in assessment_items:
                self.fill_assessment_item(assessment_item)
            btn = page.find_elements_by_css_selector('*[name="btn-next"], *[name="btn-finish"]')
            btn[0].click()
            time.sleep(1)

    def test_resources_render(self):
        self.test_home()
        self.start_assessment()
        self.fill_assessment()
        time.sleep(1)
        resource_rows = self.browser.find_elements_by_css_selector("#container-results .row")
        self.assertIsNotNone(resource_rows,"No results were found")

    def open_json(self, path):
        with open(path) as f:
            return json.load(f)

    def run_script(self, name):
        self.test_home()
        self.start_assessment()
        script = self.open_json(name)
        for step in script['steps']:
            numstep = step['step']
            if numstep == "next":
                self.click_next()
            elif numstep == "respond":
                if "type" in step:
                    typestep = step['type']
                else:
                    raise ValueError('Needs a type')

                if typestep == 'single_choice':
                    self.fill_single_choice_input(step["value_text"])
                    
                    if not 'do_next' in step or bool('do_next'):
                        self.click_next()
                elif typestep == 'multi_choice':
                    self.fill_multi_choice_input(step["value_text"])

                    if not 'do_next' in step or bool('do_next'):
                        self.click_next()
            #elif numstep == 'assert':
            else:
                raise ValueError('Unrecognised kind of step')
            time.sleep(0.5)

    def test_script(self):
        self.run_script('tests/example_test_script.json')

    def test_choice_validation(self):
        self.assertEqual(1,1)
        # get to a choice question
        # click next
        # assert validation error

    def test_conditional_question(self):
        self.assertEqual(1,1)
        # get to condition question
        # select positive condition
        # get to conditionAL question
        # assert that it loads
        
    def test_conditional_question_neg(self):
        self.assertEqual(1,1)
        # get to condition question
        # select negative condition
        # get to conditionAL question
        # assert that it doesn't load
    
    def test_conditional_question_back(self):
        self.assertEqual(1,1)
        # get to condition question
        # select positive condition
        # get to conditionAL question
        # assert that it loads (?)
        # go back to condition
        # select negative condition
        # get to conditional question
        # assert that it doesn't load
             
    def start_assessment(self):
        self.browser.find_element_by_id("btn-home-start-assessment").click()

    def click_next(self):
        self.browser.find_element_by_css_selector(".v-stepper__content.assessment-page.current [name=btn-next]").click()