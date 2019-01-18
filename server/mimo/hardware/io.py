from collections import OrderedDict

# Create an ordered dictionary of IO devices indexed by their pin number

# Buttons ordered dictionary
buttons = OrderedDict()
# buttons[10] = 'BTN_GREEN'
# buttons[11] = 'BTN_RED'

# Material buttons
buttons[12] = 'BTN-A'
buttons[16] = 'BTN-B'
buttons[18] = 'BTN-C'
buttons[22] = 'BTN-D'
buttons[24] = 'BTN-E'
buttons[26] = 'BTN-F'

# Optimization buttons
# buttons[0] = 'BTN-0'
# buttons[1] = 'BTN-1'
# buttons[2] = 'BTN-2'
# buttons[3] = 'BTN-3'

button_state = {
    12: True,
    16: True,
    18: True,
    22: True,
    24: True,
    26: True
}

button_pressed = {
    12: False,
    16: False,
    18: False,
    22: False,
    24: False,
    26: False
}

button_leds = OrderedDict()

# Material buttons LEDs
button_leds[15] = 'BTN-A'
button_leds[29] = 'BTN-B'
button_leds[31] = 'BTN-C'
button_leds[33] = 'BTN-D'
button_leds[35] = 'BTN-E'
button_leds[37] = 'BTN-F'


button_leds_code = OrderedDict()

# Material buttons LEDs
# button_leds[12] = 'BTN-A'
button_leds_code[16] = 29
button_leds_code[18] = 31
button_leds_code[22] = 33
button_leds_code[24] = 35
button_leds_code[26] = 37


# LCD screens ordered dictionary
lcd_screens = OrderedDict()
lcd_screens[22] = {'address': 0x22, 'instance': None}
lcd_screens[23] = {'address': 0x23, 'instance': None}
lcd_screens[24] = {'address': 0x24, 'instance': None}
lcd_screens[25] = {'address': 0x25, 'instance': None}
lcd_screens[26] = {'address': 0x26, 'instance': None}
lcd_screens[27] = {'address': 0x27, 'instance': None}

# ON/OFF switches
switch = 'SWITCH'

# RGB LEDs

rgb_leds = {
    0: {
            'pins': {'r': 16, 'g': 18, 'b': 22},
            'status': [1, 1, 1]
        }
}
