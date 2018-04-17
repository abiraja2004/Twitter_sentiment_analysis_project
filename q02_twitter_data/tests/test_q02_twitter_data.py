import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q02_twitter_data
from inspect import getfullargspec
import pandas

df = q02_twitter_data()


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q02_twitter_data).args
        self.assertEqual(len(arg), 0, "Expected argument(s) %d, Given %d" % (0, len(arg)))

    def test_instance(self):
        self.assertIsInstance(df, pandas.core.frame.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_return_shape(self):
        self.assertEqual(df.shape, (200, 7), "The Expected return shape does not match with the given return shape")
