from __future__ import print_function

from utils.Adafruit_Thermal import *
import HTMLParser
# import os
import RPi.GPIO as IO
import time
from unidecode import unidecode


title = 'Weolcome to MiMo v3'
subtitle = 'Latest news from MiMo feed'
author = 'MiMo Team'

# Initialize printer
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

# Print welcome message
printer.print(unidecode(
        HTMLParser.HTMLParser().unescape(title)
    )
)

printer.feed(1)

printer.print(unidecode(
        HTMLParser.HTMLParser().unescape(subtitle)
    )
)

printer.feed(1)

printer.print(unidecode(
        HTMLParser.HTMLParser().unescape(author)
    )
)

printer.feed(1)

printer.print(unidecode(
        HTMLParser.HTMLParser().unescape('2018')
    )
)

printer.feed(4)


IO.setmode(IO.BOARD)
IO.setup(29, IO.OUT)
IO.output(29, True)
time.sleep(2)
IO.output(29, False)
IO.cleanup()


def setup():
    # LED configuration
    IO.setmode(IO.BOARD)
    IO.setup(33, IO.OUT)
    IO.setup(31, IO.OUT)
    IO.setup(29, IO.OUT)


def print_data(data):
    '''
    TODO: Implement JSON parse
    '''
    # Printer LED on
    IO.output(31, True)
    time.sleep(1)

    # Start printing
    printer.inverseOn()
    printer.print(' ' + '{:<31}'.format(data['user']))
    printer.inverseOff()

    printer.underlineOn()
    printer.print('{:<32}'.format(data['date']))
    printer.underlineOff()

    # Remove HTML escape sequences
    # and remap Unicode values to nearest ASCII equivalents
    printer.print(unidecode(
            HTMLParser.HTMLParser().unescape(data['text'])
        )
    )

    printer.feed(6)

    # Printer LED off
    IO.output(31, False)

    time.sleep(5)

    IO.output(29, True)
    time.sleep(1.5)
    IO.output(29, False)

    IO.cleanup()
    time.sleep(10)


while True:
    setup()
    cable = {
            'user': 'MiMo Console',
            'date': 'Oct 30  1982',
            'text': 'I saw the best minds of my generation destroyed by madness...'
    }
    print_data(cable)
