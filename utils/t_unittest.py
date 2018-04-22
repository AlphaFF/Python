import unittest
import logging

logging.basicConfig(level=logging.INFO)

def f(x):
	return x+1

class Test(unittest.TestCase):
	def setUp(self):
		logging.info('setUp')

	def tearDown(self):
		logging.info('tearDown')

	def test_abs(self):
		self.assertEqual(2,2)

	def test_f(self):
		self.assertEqual(f(3),4)


if __name__ == '__main__':
	unittest.main()