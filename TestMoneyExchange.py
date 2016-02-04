# TestMoneyExchange.py
# by Your Teacher
# A series of tests for all the money exhanges

import unittest

import MoneyExchange

class KnownValues(unittest.TestCase):

    def test_eurosToDollars_forPositiveAmount(self):
        result = MoneyExchange.eurosToDollars(10)
        self.assertEqual(11.100000000000001, result)

    def test_eurosToDollars_forNegativeAmount(self):
        result = MoneyExchange.eurosToDollars(-10)
        self.assertEqual(0, result)
        
    def test_dollarsToEuros_forPositiveAmount(self):
        result = MoneyExchange.dollarsToEuros(10)
        self.assertEqual(9.0, result)

    def test_dollarsToEuros_forNegativeAmount(self):
        result = MoneyExchange.dollarsToEuros(-10)
        self.assertEqual(0, result)

    def test_yenToDollars_forPositiveAmount(self):
        result = MoneyExchange.yenToDollars(10)
        self.assertEqual(0.085, result)

    def test_yenToDollars_forNegativeAmount(self):
        result = MoneyExchange.yenToDollars(-10)
        self.assertEqual(0, result)
        
    def test_dollarsToYen_forPositiveAmount(self):
        result = MoneyExchange.dollarsToYen(10)
        self.assertEqual(1180.6, result)

    def test_dollarsToYen_forNegativeAmount(self):
        result = MoneyExchange.dollarsToYen(-10)
        self.assertEqual(0, result)

    def test_yuanToDollars_forPositiveAmount(self):
        result = MoneyExchange.yuanToDollars(10)
        self.assertEqual(1.5, result)

    def test_yuanToDollars_forNegativeAmount(self):
        result = MoneyExchange.yuanToDollars(-10)
        self.assertEqual(0, result)
        
    def test_dollarsToYuan_forPositiveAmount(self):
        result = MoneyExchange.dollarsToYuan(10)
        self.assertEqual(68.5, result)

    def test_dollarsToYuan_forNegativeAmount(self):
        result = MoneyExchange.dollarsToYuan(-10)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
