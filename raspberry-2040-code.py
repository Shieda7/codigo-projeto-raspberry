import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Inicializa o teclado USB HID
kbd = Keyboard(usb_hid.devices)

# Pinos GPIO ligados aos 9 switches (GP5 a GP13)
BUTTON_PINS = [
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13
]

# Teclas virtuais enviadas ao PC (F13 a F21)
# Úteis para OBS, Discord ou Premiere pois não entram em conflito com o teclado físico
KEY_MAP = [
    Keycode.F13,
    Keycode.F14,
    Keycode.F15,
    Keycode.F16,
    Keycode.F17,
    Keycode.F18,
    Keycode.F19,
    Keycode.F20,
    Keycode.F21
]

# Configura cada pino como entrada com resistor Pull-Up interno
buttons = []
for pin in BUTTON_PINS:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    buttons.append(btn)

# Guarda o estado anterior de cada botão
last_states = [True] * len(buttons)

print("Stream Deck pronto a ser utilizado!")

while True:
    for i, btn in enumerate(buttons):
        current_state = btn.value  # True = Solto, False = Pressionado (Pull-Up)
        
        # Botão acabou de ser pressionado
        if not current_state and last_states[i]:
            kbd.press(KEY_MAP[i])
            time.sleep(0.02)  # Debounce simples
            
        # Botão acabou de ser solto
        elif current_state and not last_states[i]:
            kbd.release(KEY_MAP[i])
            time.sleep(0.02)
            
        last_states[i] = current_state
        
    time.sleep(0.01)