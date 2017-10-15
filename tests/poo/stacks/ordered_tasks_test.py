#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from training.projects.stacks.tasks import Task


class TestCompareDueDate(unittest.TestCase):

    def testBasic(self):
        from datetime import datetime
        t1 = Task("task1", datetime(2015, 1, 1), datetime(2016, 1, 1))
        t2 = Task("task2", datetime(2015, 1, 1), datetime(2016, 1, 2))
        self.assertGreater(t2, t1)

    def testNone(self):
        from datetime import datetime
        t1 = Task("task1", datetime(2015, 1, 1))
        t2 = Task("task2", datetime(2015, 1, 1), datetime(2016, 1, 2))
        self.assertGreater(t1, t2)

    def testSameDueDifferentCreation(self):
        from datetime import datetime
        t1 = Task("task1", datetime(2015, 1, 2), datetime(2016, 1, 1))
        t2 = Task("task2", datetime(2015, 1, 1), datetime(2016, 1, 1))
        self.assertGreater(t1, t2)


if __name__ == "__main__":
    unittest.main()
