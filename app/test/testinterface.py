#coding= utf-8
__author__ = '201512010283'

import requests
import unittest
params = {'mark1':'val1', 'mark2':'val2'}

class myclass(unittest.TestCase):
    def testGateway(self):
        r = requests.get("http://localhost:5000/fgateway", params=params)
        print r.url





if __name__ == '__main__':
    unittest.main()
