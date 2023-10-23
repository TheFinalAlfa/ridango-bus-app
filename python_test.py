import unittest
import main

class TestMain(unittest.TestCase):
    def test_greater_then_time_n1h(self):
        self.assertTrue(main.greater_then_time("02:00:00", "01:00:00"))
    def test_greater_then_time_n2h(self):
        self.assertTrue(main.greater_then_time("02:00:00", "00:00:00"))
    def test_greater_then_time_equal(self):
        self.assertFalse(main.greater_then_time("02:00:00", "02:00:00"))
    def test_greater_then_time_1h(self):
        self.assertFalse(main.greater_then_time("02:00:00", "03:00:00"))
    def test_greater_then_time_n1m(self):
        self.assertTrue(main.greater_then_time("02:00:00", "01:59:00"))
    def test_greater_then_time_1m(self):
        self.assertFalse(main.greater_then_time("02:00:00", "02:01:00"))
    def test_greater_then_time_n1s(self):
        self.assertTrue(main.greater_then_time("02:00:00", "01:059:059"))
    def test_greater_then_time_1s(self):
        self.assertFalse(main.greater_then_time("02:00:00", "02:00:01"))