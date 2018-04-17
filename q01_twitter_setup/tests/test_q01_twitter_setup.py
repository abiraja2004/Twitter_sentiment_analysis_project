
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q01_twitter_setup
from inspect import getfullargspec


api_call = q01_twitter_setup()


class Test_twitter_setup(TestCase):
    def test_twitter_setup_to_df_args(self):
        arg = getfullargspec(q01_twitter_setup).args
        self.assertEqual(len(arg), 0, "Expected argument(s) %d, Given %d" % (0, len(arg)))

