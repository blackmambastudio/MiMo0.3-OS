from collections import OrderedDict

# Create an ordered dictionary of IO devices indexed by their pin number

# Buttons ordered dictionary
buttons = OrderedDict()
# buttons[10] = 'BTN_GREEN'
# buttons[11] = 'BTN_RED'

# Material buttons
buttons[12] = 'BTN_A'
buttons[16] = 'BTN_B'
# buttons[13] = 'BTN_C'
# buttons[15] = 'BTN_D'
# buttons[19] = 'BTN_E'
# buttons[21] = 'BTN_F'

# Optimization buttons
# buttons[0] = 'BTN_0'
# buttons[1] = 'BTN_1'
# buttons[2] = 'BTN_2'
# buttons[3] = 'BTN_3'

button_states = {
    10: False,
    11: False,
    12: True,
    16: True,
    18: False,
    22: False,
    32: False,
    36: False,
    0: False,
    1: False,
    2: False,
    3: False
}

button_leds = OrderedDict()

# Material buttons LEDs
button_leds[29] = 'BTN_A'
button_leds[31] = 'BTN_B'
button_leds[33] = 'BTN_C'
button_leds[35] = 'BTN_D'
button_leds[37] = 'BTN_E'
button_leds[27] = 'BTN_F'


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


