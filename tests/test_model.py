import unittest

from ..model import Predictor


class TestPredictor(unittest.TestCase):

    def setUp(self):
        self.presenter = Predictor()

    def test_output_type(self):
        input_ = list(range(10))
        output_ = self.presenter(input_)
        self.assertTrue(output_ is float)
