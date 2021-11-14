namerenaDoba = 0
urcenaDoba = 0



def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global urcenaDoba
    urcenaDoba = randint(300, 10000)
    music.play_tone(Note.C, urcenaDoba)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
