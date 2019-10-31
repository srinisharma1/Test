import unittest
from test.smoke.test_Google_Title import test_Sample
from test.smoke.HTMLTestRunner import HTMLTestRunner

# #Run the test suite
# unittest.TextTestRunner(verbosity=2).run(suit)


def suite():

    # Get all the test from TestOne & TestTwo
    Verify_Google_Title = unittest.TestLoader().loadTestsFromTestCase(test_Sample)


    #Create a test suite
    suite = unittest.TestSuite()
    suite.addTests(Verify_Google_Title)
    # suite.addTest(TestThree('test_Three_Three'))
    return suite



if __name__ == "__main__":
    # unittest.TextTestRunner(verbosity=2).run(suite())

    #Open The File To Which the Report Needs To Be Written
    outfile = open('Report.html', 'w')

    #Creating an object of HTMLTESTRUNNER CLASS
    runner = HTMLTestRunner(stream=outfile,verbosity=2,title='LinkedIn Report',description='This is a demo report')

    #Run the suit with the help of HTMLTESTRUNNER Object
    runner.run(suite())
