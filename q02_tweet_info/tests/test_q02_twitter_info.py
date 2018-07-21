from unittest import TestCase
from ..build import q02_tweet_info
from inspect import getfullargspec
import pandas

info1, info2, info3 = q02_tweet_info()


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q02_tweet_info).args
        self.assertEqual(len(arg), 0, "Expected argument(s) %d, Given %d" % (0, len(arg)))

    def test_instance(self):
        self.assertIsInstance(info1, pandas.core.series.Series,
                              "The Expected return type does not match with the given return type")

    def test_instance_1(self):
        self.assertIsInstance(info2, pandas.core.series.Series,
                              "The Expected return type does not match with the given return type")

    def test_instance_2(self):
        self.assertIsInstance(info3, pandas.core.series.Series,
                              "The Expected return type does not match with the given return type")
