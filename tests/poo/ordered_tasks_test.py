#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from training.poo.stacks.tasks import Task


class TestCompareDueDate(unittest.TestCase):

    def testBasic(self):
        from datetime import datetime
        t1 = Task("task1", datetime(2015, 01, 01), datetime(2016, 01, 01))
        t2 = Task("task2", datetime(2015, 01, 01), datetime(2016, 01, 02))
        self.assertGreater(t2, t1)

    def testNone(self):
        from datetime import datetime
        t1 = Task("task1", datetime(2015, 01, 01))
        t2 = Task("task2", datetime(2015, 01, 01), datetime(2016, 01, 02))
        self.assertGreater(t1, t2)

    def testSameDueDifferentCreation(self):
        from datetime import datetime
        t1 = Task("task1", datetime(2015, 01, 02), datetime(2016, 01, 01))
        t2 = Task("task2", datetime(2015, 01, 01), datetime(2016, 01, 01))
        self.assertGreater(t1, t2)

if __name__ == "__main__":
    unittest.main()
