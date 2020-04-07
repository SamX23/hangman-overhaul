import time
import sys
from random import randrange


class Printer:
    def __init__(self, text,
                 tm='0.02'):
        # print('Running Text!')
        # text = input
        sec = tm + str(randrange(1, 4, 1))
        sec = float(sec)

        for x in text:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(sec)