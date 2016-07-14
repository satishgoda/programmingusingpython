import argparse

def isButton(button):
    return button if button in "BUTTON_X BUTTON_Y BUTTON_A BUTTON_B".split() else None

print isButton('BUTTON_X')

parser = argparse.ArgumentParser()
parser.add_argument('button', metavar='BUTTON', type=isButton)
pressed = parser.parse_args(['BUTTON_X'])

if pressed.button:
    print pressed.button
