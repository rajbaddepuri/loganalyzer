from unittest.mock import patch

from django.test import TestCase
import unittest

# Create your tests here.

class Math(object):

    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a - b

    def div(self, a, b):
        return a/b

class LogAnalyzerTest(unittest.TestCase):
    def setUp(self):
        self.math_obj = Math()
        print("This is setup method")

    def tearDown(self):
        print("This is tear down method")

    def test_addition(self):
        self.assertEqual(self.math_obj.add(4,5), 9, "Addition is not working as expected")

    def test_sub(self):
        self.assertEqual(self.math_obj.sub(7,5), 2, "Not properly validated")

    @patch("django.db.connection")
    def test_insert_log_path(self, conn):
        from loganalyzerapp.dbOperations import insert_log_path
        a = insert_log_path("c://tte.log")
        self.assertTrue(a, "Unable to insert log path")

    @patch("django.db.connection")
    def test_get_log_path(self,conn):
        from loganalyzerapp.dbOperations import get_log_path
        a = get_log_path()
        self.assertTrue(a,"unable to get log path")

    @patch("django.db.connection")
    def test_get_count_db(self, conn):
        from loganalyzerapp.dbOperations import get_count_db
        a = get_count_db()
        self.assertTrue(a, "unable to get db count")

    @patch("django.db.connection")
    def test_clean_log_analyzer(self, conn):
        from loganalyzerapp.dbOperations import clean_log_analyzer
        a = clean_log_analyzer()
        self.assertTrue(a, "unable to clean db ")



    @patch("django.db.connection")
    def test_get_ip_adress(self, conn):
        from loganalyzerapp.dbOperations import get_ip_adress
        conn.cursor().__enter__().fetchall.return_value = [["192.168.1.1"]]
        a = get_ip_adress()
        self.assertEqual(a, ["192.168.1.1"], "unable to get ip values ")

    @patch("django.db.connection")
    def test_get_all_values(self, conn):
        from loganalyzerapp.dbOperations import get_all_values
        a = get_all_values("192.30.1.1")
        self.assertTrue(a, "unable to get ip values ")

    @patch("django.db.connection")
    def test_get_group_by_ip_address(self, conn):
        from loganalyzerapp.dbOperations import get_group_by_ip_address
        a = get_group_by_ip_address
        self.assertTrue(a, "unable to get ip values ")

    @patch("django.db.connection")
    def test_insert_log_values(self, conn):
        from loganalyzerapp.dbOperations import insert_log_values
        a = [insert_log_values('192.0.10.219')]
        self.assertTrue(a, "able to insert value into db ")


    @patch("django.db.connection")
    def test_process_file_data(self, conn):
        from loganalyzerapp.dbOperations import process_file_data
        dummy_data = ['189.16.1.18 - - [12/Dec/2015:19:12:26 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"'.split( )]
        a = process_file_data(dummy_data)
        self.assertTrue(a, "able to insert value into db ")


if __name__ == '__main__':
    unittest.main()



