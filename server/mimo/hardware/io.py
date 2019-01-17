from collections import OrderedDict

# Create an ordered dictionary of IO devices indexed by their pin number

# Buttons ordered dictionary
buttons = OrderedDict()
buttons[10] = 'BTN_GREEN'
buttons[11] = 'BTN_RED'
buttons[12] = 'BTN_A'
buttons[16] = 'BTN_B'
buttons[18] = 'BTN_C'
buttons[22] = 'BTN_D'
buttons[32] = 'BTN_E'
buttons[36] = 'BTN_F'
buttons[0] = 'BTN_0'
buttons[1] = 'BTN_1'
buttons[2] = 'BTN_2'
buttons[3] = 'BTN_3'

button_states = {
    10: False,
    11: False,
    12: False,
    16: False,
    18: False,
    22: False,
    32: False,
    36: False,
    0: False,
    1: False,
    2: False,
    3: False
}

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
