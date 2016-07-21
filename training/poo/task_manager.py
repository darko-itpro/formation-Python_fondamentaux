#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Gestion des tâches
------------------


"""

from stack import OrderedStack

personnel = {}


def creer_gestionnaire_tache(nom):
    """
    Create a new stack item

    :param nom: name of the user
    :return: None
    """
    personnel[nom] = OrderedStack()


def add_task(name, task):
    """
    Add a Task object to item defined by name

    :param name: the item to which a task must be added
    :param task:
    :return: None
    """
    try:
        personnel.get(name).empile(task)
    except AttributeError:
        print 'User unknown, you gave %s' % name
        raise ValueError('name not found')


def get_task(nom):
    """
    Get the task for a given for the item given by name.

    :param nom:
    :return:
    """
    next_task = personnel.get(nom).depile()
    if next_task:
        print "{} doit realiser {}".format(nom, next_task)
    else:
        print "Plus rien à faire !!!"
