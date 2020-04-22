import sys
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1')
from BeautifulReport import BeautifulReport
import unittest, time
from pubilc.case import YHDtest

suit = unittest.TestSuite()
suit.addTest(YHDtest('test_search'))

if __name__ == '__main__':
    reportName = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) + '.html'
    BeautifulReport(suit).report(filename=reportName, description='Search')