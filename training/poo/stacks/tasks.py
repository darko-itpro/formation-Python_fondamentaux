#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime


class TaskManager(object):
    def __init__(self, name, stack):
        if name:
            self.name = name
        else:
            raise ValueError('Title needed')
        if


class Task(object):
    def __init__(self, title, add_date=datetime.now(), due_date=None):
        super(Task, self).__init__()

        if not title:
            raise ValueError("Title should not be empty")
        self._title = title
        self._add_date = add_date
        self._due_date = due_date

    def __lt__(self, other):
        """
        For ordering purpose, if the dates are equals, this object is considered
        smaller.

        :param other:
        :return:
        """
        if self._due_date == other._due_date:
            return self._add_date <= other._add_date

        if other._due_date and self._due_date:
            return self._due_date <= other._due_date
        elif self._due_date:
            return True
        else:
            return False

    def __gt__(self, other):
        if self._due_date == other._due_date:
            return self._add_date > other._add_date

        if other._due_date and self._due_date:
            return self._due_date > other._due_date
        elif self._due_date:
            return False
        else:
            return True

    def __str__(self):
        return self._title

    def __repr__(self):
        return self._title


