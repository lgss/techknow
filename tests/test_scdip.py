import unittest
import time
import random
from test_bootstrap import JerichoTest
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScdipTests(JerichoTest):
    CURRENT_PAGE_SELECTOR = '.assessment-page.current form .assessment-item'
    def page_home(self):
        self.browser.get(self.env["root"])
        try: 
            heading = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'.v-toolbar__title b'))
            )
            self.assertEqual(heading.text, self.env['title'], 'Title Check')
            assessmentbtn = self.browser.find_elements_by_id("btn-home-start-assessment")
            self.assertEqual(len(assessmentbtn), 1)
            assessmentbtn[0].click()
        except:
            raise Exception('Failed')
    
    def test_home(self):
        self.page_home()
    
    def page_parents(self):
        parent_page = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.CURRENT_PAGE_SELECTOR))
        )
        journey_parents = parent_page.find_elements_by_css_selector('.v-input--checkbox')
        self.assertGreater(len(journey_parents),0)
        for parent in journey_parents:
            parent.click()
        next = self.browser.find_element_by_css_selector('.assessment-page.current').find_element_by_name('btn-next')
        next.click()
    
    def test_parents_render(self):
        self.test_home()
        self.page_parents()

    def page_journeys(self):
        journey_page = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.CURRENT_PAGE_SELECTOR))
        )
        journeys = journey_page.find_elements_by_css_selector('.v-input--checkbox')
        self.assertGreater(len(journeys),0)
        for journey in journeys:
            journey.click()
        next = self.browser.find_element_by_css_selector('.assessment-page.current').find_element_by_name('btn-next')
        next.click()

    def test_journeys_render(self):
        self.page_home()
        self.page_parents()
        self.page_journeys()

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
        self.page_home()
        self.page_parents()
        self.page_journeys()
        #self.start_assessment()
        next = self.browser.find_elements_by_name("btn-next")
        next.pop() #no next button on last page
        for btn in next:
            assessment_items = self.browser.find_elements_by_css_selector(self.CURRENT_PAGE_SELECTOR)
            self.assertGreater(len(assessment_items),0)
            btn.click()
            time.sleep(1)

    def get_single_choice_input(self, assessment_item=0):
        if isinstance(assessment_item, int):
            return self.browser.find_elements_by_css_selector(f'{self.CURRENT_PAGE_SELECTOR} .v-input--radio-group')[assessment_item]
        else:
            return assessment_item

    def get_multi_choice_input(self, assessment_item=0):
        if isinstance(assessment_item, int):
            return self.browser.find_elements_by_css_selector(self.CURRENT_PAGE_SELECTOR)[assessment_item]
        else:
            return assessment_item

    def item_stimulus(self, index=0):
        return self.browser.find_elements_by_css_selector(f"{self.CURRENT_PAGE_SELECTOR} .item-stimulus")[index].text

    def fill_single_choice_input(self, value=None, assessment_item=0):
        group = self.get_single_choice_input(assessment_item)

        radios = group.find_elements_by_css_selector('.v-radio')
        self.assertIsNotNone(radios)

        if value is None:
            radio = random.choice(radios)
            radio.click()
        else:    
            for radio in radios:
                if radio.text == value:
                    radio.click()
                    break
                
        selected = "v-item--active" in radio.get_attribute('class')
        self.assertTrue(selected)
    
    def fill_multi_choice_input(self, value=None, assessment_item=0):
        group = self.get_multi_choice_input(assessment_item)
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
        self.page_home()
        #self.start_assessment()
        script = self.open_json(name)
        for step in script['steps']:
            numstep = step['step']

            if   numstep == "next":
                self.click_next()
            elif numstep == "finish":
                self.click_finish()
            elif numstep == "respond":
                if "type" in step:
                    typestep = step['type']
                else:
                    raise ValueError('Needs a type')

                if typestep == 'single-choice-input':
                    if "value_text" in step:
                        self.fill_single_choice_input(step["value_text"])
                    else:
                        self.fill_single_choice_input()
                    
                    if not 'do_next' in step or bool('do_next'):
                        self.click_next()
                elif typestep == 'multiple-choice-input':
                    self.fill_multi_choice_input(step["value_text"])

                    if not 'do_next' in step or bool('do_next'):
                        self.click_next()
            #elif numstep == 'assert':
            else:
                raise ValueError(f'Unrecognised step type: {numstep}')
            time.sleep(0.5)

    def test_script(self):
        self.run_script('tests/scripts/example_test_script.json')

    def test_choice_validation(self):
        self.run_script('tests/scripts/validation_test.json')

        self.assertEquals(self.env['validation_message'],  self.item_stimulus(0))

    def test_conditional_question(self, script=None):
        if not script == None:
            self.run_script(script)

        self.fill_single_choice_input('No')
        self.click_next()
        time.sleep(1)

        self.assertEquals(self.env["conditional_question"], self.item_stimulus(0))
        
    def test_conditional_question_neg(self, script=None):
        if not script == None:
            self.run_script(script)

        self.fill_single_choice_input('Yes')
        self.click_next()
        time.sleep(1)

        self.assertNotEquals(self.env["conditional_question"], self.item_stimulus(0))
    
    def test_conditional_question_back(self):
        self.test_conditional_question('tests/scripts/conditional_question_test.json')
        self.browser.find_element_by_css_selector(".v-stepper__content.assessment-page.current [name=btn-back]").click()
        time.sleep(1)
        self.test_conditional_question_neg()

    def test_halt_dialog_neg(self, script=None):
        if not script == None:
            self.run_script(script)

        self.fill_single_choice_input("Yes")
        self.click_next()
        time.sleep(1)

        self.assertEquals(self.env["halt_dialog"], self.browser.find_element_by_id('dialog-title').text)
    
    def test_halt_dialog_pass(self, script=None):
        if not script == None:
            self.run_script(script)

        self.fill_single_choice_input("No")
        self.click_next()
        time.sleep(1)

        halt_title = self.browser.find_elements_by_id('dialog-title')
        self.assertIsNotNone(halt_title)

    def test_halt_dialog_back(self):
        self.test_halt_dialog_neg('tests/scripts/halt_test.json')
        self.browser.find_element_by_class_name("v-btn").click()
        time.sleep(1)
        self.test_halt_dialog_pass()
             
    def start_assessment(self):
        self.browser.find_element_by_id("btn-home-start-assessment").click()

    def click_next(self):
        WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".v-stepper__content.assessment-page.current [name=btn-next]"))
        ).click()
        #self.browser.find_element_by_css_selector(".v-stepper__content.assessment-page.current [name=btn-next]").click()

    def click_finish(self):
        WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.NAME,"btn-finish"))
        ).click()
        
    def test_null_result_content(self):
        self.run_script('tests/scripts/no_journey.json')
        null_result_container = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.NAME, 'no_results'))
        )
        title = null_result_container.find_element_by_css_selector('h1')
        self.assertEqual(title.text,self.env['null_result']['title'])
        content = null_result_container.find_element_by_css_selector('.col')
        self.assertEqual(content.text, self.env['null_result']['content'])

    
