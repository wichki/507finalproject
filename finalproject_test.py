from finalproject import *
import unittest

class TestCSVImport(unittest.TestCase):
    def setUp(self):
        test1 = process_command("map state ca unemployment 2013")
        # print(test1)
        self.assertTrue(test1[1][1], "Alameda County, CA")
        self.assertTrue(test1[-1][1], "Yuba County, CA")

        test2 = process_command("map state mi unemployment 2013")
        # print(test2)
        self.assertTrue(test2[1][1], "Alcona County, MI")
        self.assertTrue(test2[-1][1], "Wexford County, MI")

        test3 = process_command("map state ia unemployment 2009")
        # print(test3)
        self.assertTrue(test3[1][1], "Adair County, IA")
        self.assertTrue(test3[-1][1], "Wright County, IA")

        test4 = process_command("map state sc unemployment 2011")
        # print(test4)
        self.assertTrue(test4[1][1], "Abbeville County, SC")
        self.assertTrue(test4[-1][1], "York County, SC")

    def test_database(self):
        # pass
        self.assertEqual(len(process_command("linechart state ca sacramento county 2007")), 1)
        self.assertEqual(len(process_command("linechart state mi washtenaw county 2007")), 1)
        self.assertEqual(len(process_command("linechart state ca los angeles county 2007")), 1)
        self.assertEqual(len(process_command("map state ca unemployment 2013")), 59)
        self.assertEqual(len(process_command("map state az unemployment 2013")), 16)
        self.assertEqual(len(process_command("map state fl unemployment 2013")), 68)
        self.assertEqual(len(process_command("map national poverty")), 3194)
        self.assertEqual(len(process_command("map national unemployment 2012")), 3275)

class Yelp_Function(unittest.TestCase):
    def TestYelp(self):
        try:
            pingYelp("groceries", "washtenaw")
            pingYelp("farmer's markets", "new york")
            pingYelp("markets", "94012")
            pingYelp("markets", "94012", offset=51)
        except:
            self.fail()


if __name__ == '__main__':
    unittest.main(verbosity=2)
