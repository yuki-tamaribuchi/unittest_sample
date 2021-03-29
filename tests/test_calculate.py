from unittest import TestCase
from scripts.calculate import Calculate


class TestCalculate(TestCase):

    def setUp(self):
        self.c=Caluculate(10,2)

    def test_add(self):
        self.assertEqual(self.c.add(),12)

    def test_sub(self):
        self.assertEqual(self.c.sub(),8)

    def test_mul(self):
        self.assertEqual(self.c.mul(),20)

    def test_div(self):
        self.assertEqual(self.c.div(),5)

    def test_mod(self):
        self.assertEqual(self.c.mod(),0)

    def test_double_plus_one(self):
        self.assertEqual(self.c.double_plus_one(),25)

