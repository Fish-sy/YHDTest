import sys
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1\\pubilc')
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1')
sys.path.append('C:\\Program Files\\JetBrains\\PyCharm 2019.1.2\\helpers\\pycharm_display')
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1\\venv\\Scripts\\python36.zip')
sys.path.append('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python36\\DLLs')
sys.path.append('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python36\\lib')
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1\\venv')
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1\\venv\\lib\\site-packages')
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1\\venv\\lib\\site-packages\\setuptools-40.8.0-py3.6.egg')
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1\\venv\\lib\\site-packages\\pip-19.0.3-py3.6.egg')
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1\\venv\\lib\\site-packages\\win32')
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1\\venv\\lib\\site-packages\\win32\\lib')
sys.path.append('C:\\Users\\admin\\PycharmProjects\\untitled1\\venv\\lib\\site-packages\\Pythonwin')
sys.path.append('C:\\Program Files\\JetBrains\\PyCharm 2019.1.2\\helpers\\pycharm_matplotlib_backend')
from BeautifulReport import BeautifulReport
import unittest, time
from pubilc.case import YHDtest

suit = unittest.TestSuite()
suit.addTest(YHDtest('test_search'))

if __name__ == '__main__':
    reportName = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) + '.html'
    BeautifulReport(suit).report(filename=reportName, description='Search')