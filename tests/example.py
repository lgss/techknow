from test_bootstrap import JerichoTest
import time

class Example(JerichoTest):

    def check_title(self, title):
        self.assertEqual(self.browser.title, title, 'Browser title check')

    def example_flow(self):
        self.browser.get(self.env['root'])
        time.sleep(1)
        self.check_title('Example')
