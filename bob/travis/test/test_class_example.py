#!/usr/bin/env python
import unittest

from bob.travis.classes.class_example import ClassExample

class TestClassExample(unittest.TestCase):

    def test_class_example(self):
        assert 'Howdy, this works ;)' == ClassExample.get_greetings()
