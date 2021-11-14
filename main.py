namerenaDoba = 0
urcenaDoba = 0



def on_button_pressed_a():
    global urcenaDoba
    basic.show_icon(IconNames.YES)
    music.play_tone(Note.C, urcenaDoba)
    basic.show_icon(IconNames.HEART)

def on_button_pressed_b():
    global urcenaDoba
    urcenaDoba = randint(500, 5000)
    on_button_pressed_a()

def on_forever():
    if input.button_is_pressed(Button.A):
        on_button_pressed_a
    if input.button_is_pressed(Button.B):
        on_button_pressed_b
basic.forever(on_forever)
