from twisted.trial import unittest
from imports.MainFactory import MainFactory
from imports.MainService import MainService


class TenshiTestCase(unittest.TestCase):

	def test_failed(self):

		print 'dfdsf'

		self.assertEqual(1,0)




