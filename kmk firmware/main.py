print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP1, GP2, GP3, GP4, GP26, GP27)
keyboard.row_pins = (board.GP0,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.Q, KC.W, KC.E, KC.U, KC.I, KC.O, ]
]

if __name__ == '__main__':
    keyboard.go()