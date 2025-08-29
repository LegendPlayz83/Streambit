import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_rgb import RGB, AnimationModes

keyboard = KMKKeyboard()

# Diode direction
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Matrix pins
keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4,
    board.GP5, board.GP6, board.GP7, board.GP8, board.GP9,
    board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15
)

keyboard.row_pins = (
    board.GP16, board.GP17, board.GP18, board.GP19, board.GP20
)

# Encoder setup
encoder = EncoderHandler()
encoder.pins = ((board.GP27, board.GP28, board.GP26),)
encoder.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)
keyboard.modules.append(encoder)

# Layers support
layers = Layers()
keyboard.modules.append(layers)

# RGB Setup (SK6812)
rgb = RGB(
    pixel_pin=board.GP22,
    num_pixels=4,  # You have 4 SK6812MINI
    hue_default=180,
    sat_default=255,
    val_default=64,
    animation_mode=AnimationModes.SOLID,
)
keyboard.extensions.append(rgb)

# Keymap (trimmed for brevity; same as before)
keyboard.keymap = [
    [
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.NO, KC.NO,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.NO, KC.NO,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENTER, KC.NO, KC.NO, KC.NO,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.SPC, KC.RALT, KC.FN0, KC.RCTL, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.NO, KC.NO, KC.NO, KC.NO
    ]
]

if __name__ == '__main__':
    keyboard.go()
