from sense_hat import SenseHat
import time

duration = 15  # Set countdown duration (in seconds)

sense = SenseHat()

def start_timer_led(duration):
    #shows countdown timer on the rpi and then done when reaches 0 uses duration variable
    remaining_time = duration
    step = 255 / duration  # Calculate step for smooth color transition so it doesnt go out of 255 range
    red = 0
    green = 255
    blue = 0

    while remaining_time > 0:
        sense.clear()

        if remaining_time >= 10:
            # For >10 numbers use message
            sense.show_message(str(remaining_time), text_colour=[int(red), int(green), int(blue)], scroll_speed=0.05)
        else:
            # For <10 numbers use letter
            sense.show_letter(str(remaining_time), text_colour=[int(red), int(green), int(blue)])

        time.sleep(1)  # Wait for 1 second
        remaining_time -= 1  # Decrement the countdown

        red += step
        green -= step

    # Show "Done!" at the end
    sense.show_message("Done!", text_colour=[0, 0, 255])  # Final color blue
    sense.clear()

def main():
    print("Starting round...")
    start_timer_led(duration)
    print("Round complete!")

if __name__ == "__main__":
    main()
