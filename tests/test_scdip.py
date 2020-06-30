import unittest
import time
import random
from test_bootstrap import SetupTest
import json
import inspect

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScdipTests(SetupTest):
    ## Definitions
    CURRENT_PAGE_SELECTOR = '.assessment-page.current form .assessment-item'
    
    ## Utility functions
    def func_name(self):
        return inspect.stack()[1].function

    def assertDialog(self):
        dialog = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'.v-dialog--fullscreen'))
        )
        self.assertIsNotNone(dialog.find_element_by_id('dialog-title').text)
        self.assertIsNotNone(dialog.find_element_by_id('dialog-content').text)

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
    
    def page_select(self):
        parent_page = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#parent-selection'))
        )
        time.sleep(5)
        if parent_page.get_attribute("style") == "":
            journey_parents = parent_page.find_elements(By.CSS_SELECTOR, '.choice')
            self.assertGreater(len(journey_parents),0)
            for parent in journey_parents:
                parent.click()
            next = self.browser.find_element(By.CSS_SELECTOR, '[name="btn-continue"]')
            next.click()

        journey_page = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.ID, 'journey-selection'))
        )
        time.sleep(5)
        journeys = journey_page.find_elements(By.CSS_SELECTOR, '.choice')
        self.assertGreater(len(journeys),0)
        for journey in journeys:
            journey.click()
        next = self.browser.find_element(By.CSS_SELECTOR, '[name="btn-begin"]')
        next.click()

    def get_single_choice_input(self, assessment_item=0):
        if isinstance(assessment_item, int):
            return self.browser.find_elements_by_css_selector(f'{self.CURRENT_PAGE_SELECTOR} .v-input--radio-group')[assessment_item]
        else:
            return assessment_item

    def get_multi_choice_input(self, assessment_item=0):
        if isinstance(assessment_item, int):
            return WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.CURRENT_PAGE_SELECTOR))
            )[assessment_item]
            #return self.browser.find_elements_by_css_selector(self.CURRENT_PAGE_SELECTOR)[assessment_item]
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
            radio_found = False
            for radio in radios:
                if radio.text == value:
                    radio_found = True
                    radio.click()
                    break
            self.assertTrue(radio_found, f"Failed to find value {value} in available choices.")
                
        selected = "v-item--active" in radio.get_attribute('class')
        self.assertTrue(selected)
    
    def fill_multi_choice_input(self, value=None, assessment_item=0):
        group = self.get_multi_choice_input(assessment_item)
        checkboxes = group.find_elements_by_css_selector('.v-input--checkbox')
        self.assertIsNotNone(checkboxes)

        if value is None:
            check = random.choice(checkboxes)
        elif isinstance(value, list):
            for v in value:
                v_found = False
                for check in checkboxes:
                    if check.text == v:
                        v_found = True
                        check.find_element_by_class_name('v-input--selection-controls__ripple').click()
                        selected = 'v-input--is-label-active' in check.get_attribute('class')
                        self.assertTrue(selected)
                self.assertTrue(v_found,f"Failed to find value {v} in available choices.")
        else:
            raise TypeError(f"Expected value argument of type list or NoneType, not {type(value)}")
                    
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

    def open_json(self, path):
        with open(path) as f:
            return json.load(f)

    def run_script(self, name):
        self.page_home()
        self.page_select()
        #self.start_assessment()
        script = self.open_json(name)
        for step in script['steps']:
            numstep = step['step']

            if   numstep == "next":
                self.click_next()
            elif numstep == "finish":
                self.click_finish()
            elif numstep == "back":
                self.click_back()
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
                elif typestep == 'multiple-choice-input':
                    self.fill_multi_choice_input(step["value_text"])
            #elif numstep == 'assert':
            else:
                raise ValueError(f'Unrecognised step type: {numstep}')
            time.sleep(0.5)
        if "data" in script:
            return script["data"]


    def start_assessment(self):
        self.browser.find_element_by_id("btn-home-start-assessment").click()

    def click_next(self):
        WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".v-stepper__content.assessment-page.current [name=btn-next]"))
        ).click()

    def click_finish(self):
        WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".v-stepper__content.assessment-page.current [name=btn-finish]"))
        ).click()
    
    def click_back(self):
        WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".v-stepper__content.assessment-page.current [name=btn-back]"))
        ).click()
        
    ## Tests   
    def test_home(self):
        self.page_home()

    def test_select(self):
        self.page_home()
        self.page_select()

    def test_resources_render(self):
        self.run_script('tests/scripts/simple_positive_results.json')
        resource_rows = self.browser.find_elements_by_css_selector("#container-results .row")
        self.assertIsNotNone(resource_rows,"No results were found")

    def test_choice_validation(self):
        self.run_script('tests/scripts/validation_test.json')
        self.assertEquals(self.env['validation_message'],  self.item_stimulus(0))

    #Test that a conditional question is rendered when expected
    def test_conditional_question(self, script=None):
        data = self.run_script(f'tests/scripts/{self.func_name()}.json')
        if data is None or not 'page_title' in data or not 'item_label' in data:
            raise ValueError("Insufficient assertion data has been provided")
        title = self.browser.find_element_by_css_selector(f'.assessment-page.current form h2')
        self.assertEqual(title.text, data['page_title'])
        item = self.browser.find_element_by_css_selector(f'{self.CURRENT_PAGE_SELECTOR} label')
        self.assertEqual(item.text, data['item_label'])
    
    #Test that a conditional question is not rendered when expected
    def test_conditional_question_neg(self, script=None):
        data = self.run_script(f'tests/scripts/{self.func_name()}.json')
        if data is None or not 'page_title' in data or not 'item_label' in data:
            raise ValueError("Insufficient assertion data has been provided")
        title = self.browser.find_element_by_css_selector(f'.assessment-page.current form h2')
        self.assertNotEqual(title.text, data['page_title'])
        item = self.browser.find_element_by_css_selector(f'{self.CURRENT_PAGE_SELECTOR} label')
        self.assertNotEqual(item.text, data['item_label'])
    
    #Test that a conditional question that was not rendered is rendered once the selected choice is changed
    def test_conditional_question_back(self):
        data = self.run_script(f'tests/scripts/{self.func_name()}.json')
        if data is None or not 'page_title' in data or not 'item_label' in data:
            raise ValueError("Insufficient assertion data has been provided")
        title = self.browser.find_element_by_css_selector(f'.assessment-page.current form h2')
        self.assertEqual(title.text, data['page_title'])
        item = self.browser.find_element_by_css_selector(f'{self.CURRENT_PAGE_SELECTOR} label')
        self.assertEqual(item.text, data['item_label'])

    #Test an assessment is halted when finishing with a form ending choice
    def test_halt_dialog_finish(self):
        self.run_script(f'tests/scripts/{self.func_name()}.json')
        self.assertDialog()
    
    #Test an assessment is halted when nexting with a form ending choice
    def test_halt_dialog_next(self):
        self.run_script(f'tests/scripts/{self.func_name()}.json')
        self.assertDialog()
    
    #Test an assessment is halted when backing with a form ending choice
    def test_halt_dialog_back(self):
        self.run_script(f'tests/scripts/{self.func_name()}.json')
        self.assertDialog()

    #Test the content when no resources were found         
    def test_no_resources_content(self):
        self.run_script(f'tests/scripts/{self.func_name()}.json')
        null_result_container = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.NAME, 'no_results'))
        )
        title = null_result_container.find_element_by_css_selector('h1')
        self.assertEqual(title.text,self.env['null_result']['title'])
        content = null_result_container.find_element_by_css_selector('.col')
        self.assertEqual(content.text, self.env['null_result']['content'])

    #Test that a mandatory item may not be skipped
    def test_try_skip_mandatory_item(self):
        self.run_script(f'tests/scripts/{self.func_name()}.json')
        error_elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'{self.CURRENT_PAGE_SELECTOR} .error--text'))
        )
        error_text = error_elem.find_element_by_class_name('v-messages__message')
        self.assertEqual(error_text.text, "Please select a response")

    #Test that a stimulus renders
    def test_render_stimulus(self):
        self.run_script(f'tests/scripts/{self.func_name()}.json')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'{self.CURRENT_PAGE_SELECTOR} .stimulus'))
        )
    
    #Test that a single-choice-input renders
    def test_render_single_choice_input(self):
        self.run_script(f'tests/scripts/{self.func_name()}.json')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'{self.CURRENT_PAGE_SELECTOR} .single-choice-input'))
        )
    
    #Test that a multiple-choice-input renders
    def test_render_multiple_choice_input(self):
        self.run_script(f'tests/scripts/{self.func_name()}.json')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'{self.CURRENT_PAGE_SELECTOR} .multiple-choice-input'))
        )




