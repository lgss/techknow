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

    def assertDialog(self, title=None, content=None):
        dialog = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.v-dialog--fullscreen')),
            "Failed to locate dialog"
        )
        _title = dialog.find_element_by_id('dialog-title').text
        if title == None:
            self.assertIsNotNone(_title)
        else:
            self.assertEqual(_title, title)
            
        _content = dialog.find_element_by_id('dialog-content').text
        if content == None:
            self.assertIsNotNone(_content)
        else:
            self.assertEqual(_content, content)

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
        self.fill_category_input()
        self.confirm_categories()
        self.fill_journey_input()
        self.confirm_journies()

    def get_single_choice_input(self, assessment_item=0):
        if isinstance(assessment_item, int):
            return WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.CURRENT_PAGE_SELECTOR)),
                "Failed to locate a single choice input"
            )[assessment_item]
            #return self.browser.find_elements_by_css_selector(f'{self.CURRENT_PAGE_SELECTOR}')[assessment_item]
        else:
            return assessment_item

    def get_multi_choice_input(self, assessment_item=0):
        if isinstance(assessment_item, int):
            return WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.CURRENT_PAGE_SELECTOR)),
                "Failed to locate a multiple choice input"
            )[assessment_item]
            #return self.browser.find_elements_by_css_selector(self.CURRENT_PAGE_SELECTOR)[assessment_item]
        else:
            return assessment_item

    # def item_stimulus(self, index=0):
    #     return self.browser.find_elements_by_css_selector(f"{self.CURRENT_PAGE_SELECTOR} .item-stimulus")[index].text

    def validate_assertion_data(self, data, fields):
        missing = []
        for field in fields:
            if not field in data:
                missing.append(field)
        if len(missing):
            raise TypeError(f"Missing assertion data: {', '.join(missing)}")

    ## Fill responses

    def fill_single_choice_input(self, value=None, assessment_item=0):
        group = self.get_single_choice_input(assessment_item)
        choices = group.find_elements_by_css_selector('.choice')
        self.assertIsNotNone(choices)

        if value is None:
            choice = random.choice(choices)
            choice.click()
            selected = 'v-item--active' in choice.get_attributes('class')
            self.assertTrue(selected)
        elif isinstance(value,str):    
            v_found = False
            for choice in choices:
                if choice.text == value:
                    v_found = True
                    choice.click()
                    selected = 'v-item--active' in choice.get_attribute('class')
                    self.assertTrue(selected)
                    break
            self.assertTrue(v_found, f"Failed to find value {value} in available choices.")
        else:
            raise TypeError(f"Expected value arugment of type str or NoneType, not {type(value)}")
    def fill_multi_choice_input(self, value=None, assessment_item=0):
        group = self.get_multi_choice_input(assessment_item)
        choices = group.find_elements_by_css_selector('.choice')
        self.assertIsNotNone(choices)

        if value is None:
            choice = random.choice(choices)
            choice.check()
            selected = 'v-item--active' in choice.get_attributes('class')
            self.assertTrue(selected)
        elif isinstance(value, list):
            for v in value:
                v_found = False
                for choice in choices:
                    if choice.text == v:
                        v_found = True
                        choice.click()
                        selected = 'v-input--is-label-active' in choice.get_attribute('class')
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

    def fill_category_input(self, value=None):
        parent_page = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#parent-selection')),
            "Failed to locate category container"
        )
        choices = parent_page.find_elements_by_css_selector('.choice')
        self.assertIsNotNone(choices, "Failed to locate categories")
        
        if value is None:
            choice = random.choice(choices)
            choice.click()

        elif isinstance(value, list):
            for v in value:
                v_found = False
                for choice in choices:
                    text = choice.find_element_by_css_selector('.headline').text
                    if text == v:
                        v_found = True
                        choice.click()
                        selected = "v-item--active" in choice.get_attribute('class')
                        self.assertTrue(selected)
                self.assertTrue(v_found, f"Failed to locate value {v} in available categories")
        else:
            raise TypeError(f"Expected value argument of type list or NoneType, not {type(value)}")
        return
    
    def fill_journey_input(self, value=None):
        parent_page = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#journey-selection')),
            "Failed to locate journey container"
        )
        choices = parent_page.find_elements_by_css_selector('.choice')
        self.assertIsNotNone(choices, "Failed to locate categories")
        
        if value is None:
            choice = random.choice(choices)
            choice.click()
        elif isinstance(value, list):
            for v in value:
                v_found = False
                for choice in choices:
                    text = choice.find_element_by_css_selector('.headline').text
                    if text == v:
                        v_found = True
                        choice.click()
                        selected = "v-item--active" in choice.get_attribute('class')
                        self.assertTrue(selected)
                self.assertTrue(v_found, f"Failed to locate value {v} in available journies")
        else:
            raise TypeError(f"Expected value argument of type list or NoneType, not {type(value)}")
        return


    ## Common

    def open_json(self, path):
        with open(path) as f:
            return json.load(f)

    def run_script(self, name):
        self.page_home()
        #self.page_select()
        script = self.open_json(name)
        for step in script['steps']:
            numstep = step['step']
            if   numstep == "confirm_categories":
                self.confirm_categories()
            elif numstep == "confirm_journies":
                self.confirm_journies()
            elif numstep == "next":
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

                value_text = step["value_text"] if "value_text" in step else None

                if typestep == 'single-choice-input':
                    self.fill_single_choice_input(value_text)
                elif typestep == 'multiple-choice-input':
                    self.fill_multi_choice_input(value_text)
                elif typestep == 'category-input':
                    self.fill_category_input(value_text)
                elif typestep == 'journey-input':
                    self.fill_journey_input(value_text)
            #elif numstep == 'assert':
            else:
                raise ValueError(f'Unrecognised step type: {numstep}')
            time.sleep(0.5)
        if "data" in script:
            return script["data"]

    def click_next(self):
        WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".v-stepper__content.assessment-page.current [name=btn-next]")),
            'Failed to locate next button'
        ).click()

    def confirm_categories(self):
        WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name=btn-continue]")),
            'Failed to locate continue button'
        ).click()

    def confirm_journies(self):
        WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name=btn-begin]")),
            'Failed to locate begin button'
        ).click()

    def click_finish(self):
        WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".v-stepper__content.assessment-page.current [name=btn-finish]")),
            'Failed to locate finish button'
        ).click()
    
    def click_back(self):
        WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".v-stepper__content.assessment-page.current [name=btn-back]")),
            'Failed to locate back button'
        ).click()
        
    ## Tests

    #Test the home page loads
    def test_home(self):
        self.page_home()

    #Test selecting a random category and journey
    def test_select(self):
        self.page_home()
        self.page_select()

    #Test that resources are rendered
    def test_resources_render(self):
        self.run_script(f'tests/scripts/{self.func_name()}.json')
        resource_rows = self.browser.find_elements_by_css_selector("#container-results .row")
        self.assertIsNotNone(resource_rows,"No results were found")

    # def test_choice_validation(self):
    #     self.run_script('tests/scripts/validation_test.json')
    #     self.assertEquals(self.env['validation_message'],  self.item_stimulus(0))

    #Test that a conditional question is rendered when expected
    def test_conditional_question(self, script=None):
        data = self.run_script(f'tests/scripts/{self.func_name()}.json')
        self.validate_assertion_data(data, ["question_text"])
        item = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,f"{self.CURRENT_PAGE_SELECTOR}")),
            "Failed to locate item"
        )
        title = item.find_element_by_css_selector('h2')
        self.assertEqual(title.text, data['question_text'])
    
    #Test that a conditional question is not rendered when expected
    def test_conditional_question_neg(self, script=None):
        data = self.run_script(f'tests/scripts/{self.func_name()}.json')
        self.validate_assertion_data(data, ["question_text"])
        item = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,f"{self.CURRENT_PAGE_SELECTOR}")),
            "Failed to locate item"
        )
        title = item.find_element_by_css_selector('h2')
        self.assertNotEqual(title.text, data['question_text'])
    
    #Test that a conditional question that was not rendered is rendered once the selected choice is changed
    def test_conditional_question_back(self):
        data = self.run_script(f'tests/scripts/{self.func_name()}.json')
        self.validate_assertion_data(data, ["question_text"])
        item = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,f"{self.CURRENT_PAGE_SELECTOR}")),
            "Failed to locate item"
        )
        title = item.find_element_by_css_selector('h2')
        self.assertNotEqual(title.text, data['question_text'])

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
        data = self.run_script(f'tests/scripts/{self.func_name()}.json')
        self.validate_assertion_data(data, ["title","content"])
        null_result_container = WebDriverWait(self.browser,10).until(
            EC.presence_of_element_located((By.ID, 'no_results')),
            "Failed to result no_results container"
        )
        title = null_result_container.find_element_by_css_selector('h1')
        self.assertEqual(title.text,data['title'])
        content = null_result_container.find_element_by_css_selector('.col')
        self.assertEqual(content.text, data['content'])

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




