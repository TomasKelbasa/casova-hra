let namerenaDoba = 0
let urcenaDoba = 0
function on_button_pressed_a() {
    
    basic.showIcon(IconNames.Yes)
    music.playTone(Note.C, urcenaDoba)
    basic.showIcon(IconNames.Heart)
}

basic.forever(function on_forever() {
    if (input.buttonIsPressed(Button.A)) {
        on_button_pressed_a
    }
    
    if (input.buttonIsPressed(Button.B)) {
        on_button_pressed_b
    }
    
})
