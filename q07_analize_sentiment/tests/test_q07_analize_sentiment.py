import sys, os
import pandas
import numpy as np

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q07_analize_sentiment
from q02_twitter_data.build import q02_twitter_data
from inspect import getfullargspec


data = q02_twitter_data()
data['SA'] = np.array([q07_analize_sentiment(tweet) for tweet in data['Tweets']])


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q07_analize_sentiment).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_instance(self):
        self.assertIsInstance(data, pandas.core.frame.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_return_shape(self):
        self.assertEqual(data.shape, (200, 8), "The Expected return shape does not match with the given return shape")
