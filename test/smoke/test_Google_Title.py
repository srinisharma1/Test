# self.assertEqual(self.widget.size(), (100,150),
#                          'wrong size after resize')



from lib.ui.google_page import GooglePage as CSP
import unittest
import pytest
import time
import sys
import traceback


@pytest.mark.usefixtures("oneTimeSetUp")#, "setUp")
class test_Sample(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.csp = CSP(self.driver)

    # @pytest.mark.run(order=0)
    def test_01(self):
        value=CSP.getPageTitle(self.csp)
        assert value=='Google', 'The Title Are Not The Same'



