import unittest
from censys import *

class CensysIPv4(CensysAPIBase):

    def search(self, query, page=1, fields=[]):
        data = {
            "query":query,
            "page":page,
            "fields":fields
        }
        return self._get("ipv4", data=data)


    def get(self, ip):
        return self._get("/".join(("ipv4", str(ip))))

    def report(self, query, field, buckets):
        pass


class CensysIPv4Tests(unittest.TestCase):

    def setUp(self):
        self._api = CensysIPv4()

    def testGet(self):
        print self._api.get("23.202.141.251")

    def testSearch(self):
        print self._api.search("*")


if __name__ == "__main__":
    unittest.main()
