from __future__ import print_function

from utils.Adafruit_Thermal import *
import HTMLParser
import RPi.GPIO as IO
from unidecode import unidecode

# Initialize printer
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)


def mimo_printer_init():
    title = 'Weolcome to MiMo v4'
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

    IO.cleanup()


def mimo_setup():
    # LED configuration
    IO.setmode(IO.BOARD)
    IO.setup(33, IO.OUT)
    IO.setup(31, IO.OUT)
    IO.setup(29, IO.OUT)


def mimo_print(data):
    '''
    TODO: Implement JSON parse
    '''
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

    # IO.cleanup()


if __name__ == '__main__':
    while True:
        mimo_printer_init()
        cable = {
                'user': 'MiMo Console',
                'date': 'Oct 30  1982',
                'text': '>> INCOMING EVENT <<\n\nTHE PRESIDENTIAL CANDIDATE FULANO SAYS HE WILL ALWAYS SUPPORT TELMAR AS LONG AS THAT DOESN\'T JEOPARDIZE OUR RELATIONSHIP WITH HUNAGARA\'S GOVERMENT.'
        }
        mimo_print(cable)
        IO.cleanup()
