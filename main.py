degrees = 0
basic.show_string("COMPASS")
basic.clear_screen()

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45:
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . . # . .
            . . # . .
            """)
    elif degrees < 135:
        basic.show_leds("""
            . . # . .
            . . # # .
            # # # # #
            . . # # .
            . . # . .
            """)
    elif degrees < 225:
        basic.show_leds("""
            . . # . .
            . . # . .
            # # # # #
            . # # # .
            . . # . .
            """)
    elif degrees < 315:
        basic.show_leds("""
            . . # . .
            . # # . .
            # # # # #
            . # # . .
            . . # . .
            """)
    else:
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            . . # . .
            . . # . .
            """)
basic.forever(on_forever)
