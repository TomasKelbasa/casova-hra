function on_button_pressed_a() {
    if (urcenaDoba == 0) {
        return
    }
    
    basic.showIcon(IconNames.Target)
    music.playTone(Note.C, urcenaDoba)
    basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    `)
}

function on_button_pressed_b() {
    
    urcenaDoba = randint(5, 50) * 100
    on_button_pressed_a()
}

input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    if (urcenaDoba == 0) {
        return
    }
    
    
    dobaStartu = control.millis()
})
input.onLogoEvent(TouchButtonEvent.Released, function on_logo_released() {
    if (urcenaDoba == 0) {
        return
    }
    
    
    namerenaDoba = control.millis() - dobaStartu
    let odchylka = urcenaDoba - namerenaDoba
    basic.showLeds(`
    #####
    #####
    #####
    #####
    #####
    `)
    for (let a = 0; a < Math.abs(Math.idiv(odchylka, 100)); a++) {
        led.unplot(Math.idiv(a, 5), a - Math.idiv(a, 5) * 5)
    }
    if (Math.abs(odchylka / 100) <= 1) {
        music.playMelody("C D E F A", 120)
    }
    
})
let urcenaDoba = 0
let dobaStartu = 0
let namerenaDoba = 0
basic.forever(function on_forever() {
    if (input.buttonIsPressed(Button.A)) {
        on_button_pressed_a()
    }
    
    if (input.buttonIsPressed(Button.B)) {
        on_button_pressed_b()
    }
    
})
