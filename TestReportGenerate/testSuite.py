import unittest

from TestReportGenerate.test_opencart_registration import Registration
from TestReportGenerate.test_opencart_login import Login
from HtmlTestRunner import HTMLTestRunner

class TestSuite(unittest.TestCase):
    def test_suite(self):
        self.loginTest = unittest.TestLoader().loadTestsFromTestCase(Login)
        self.registerTest = unittest.TestLoader().loadTestsFromTestCase(Registration)

        suite = unittest.TestSuite([self.loginTest, self.registerTest])

        runner = HTMLTestRunner(output='Report', open_in_browser=True)
        runner.run(suite)


if __name__ == '__main__':
    test_suite()