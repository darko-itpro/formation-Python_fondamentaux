#!/usr/bin/env python

"""
Ce script illustre le lancement et le comportement de deux threads.
"""

import threading
import time


class Worker(threading.Thread):
    def __init__(self, name, delay):
        self.delay = delay
        threading.Thread.__init__(self, name=name)

    def run(self):
        for i in range(5):
            print(f"{self.getName()}: Appel {i}, {time.ctime(time.time())}")
            time.sleep(self.delay)


if __name__ == "__main__":
    t1 = Worker("T1", 2)
    t2 = Worker("T2", 3)
    t1.start()
    t2.start()
