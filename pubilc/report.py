from BeautifulReport import BeautifulReport
import unittest, time
from pubilc import case

suit = unittest.TestSuite()
suit.addTest(case.YHDtest('test_search'))

if __name__ == '__main__':
    reportName = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) + '.html'
    BeautifulReport(suit).report(filename=reportName, description='Search')
