def on_button_pressed_a():
    if(urcenaDoba == 0):
            return
    basic.show_icon(IconNames.TARGET)
    music.play_tone(Note.C, urcenaDoba)
    basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)

def on_button_pressed_b():
    global urcenaDoba
    urcenaDoba = randint(5, 50)*100
    on_button_pressed_a()

def on_logo_touched():
    if(urcenaDoba == 0):
            return
    global dobaStartu
    dobaStartu = control.millis()
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_logo_released():
    if(urcenaDoba == 0):
        return
    global namerenaDoba
    namerenaDoba = control.millis() - dobaStartu
    odchylka = urcenaDoba - namerenaDoba
    basic.show_leds("""
    #####
    #####
    #####
    #####
    #####
    """)
    for a in range((abs(odchylka//100))):
        led.unplot(a//5, a-(a//5)*5)
    if abs(odchylka/100) <= 1:
        music.play_melody("C D E F A", 120)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)

urcenaDoba = 0
dobaStartu = 0
namerenaDoba = 0

def on_forever():
    if input.button_is_pressed(Button.A):
        on_button_pressed_a()
    if input.button_is_pressed(Button.B):
        on_button_pressed_b()
basic.forever(on_forever)