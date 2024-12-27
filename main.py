from metrics import update_metrics, print_metrics, calculate_acceleration_sum
from config import ROUND_DURATION, KICK_THRESHOLD_LOW
from clearsensehat import clear_sense_hat
import time
from sense_hat import SenseHat

sense = SenseHat()

def get_motion_data():
    # collect the raw date using the sense hat
    return sense.get_accelerometer_raw()

def detect_kick(motion_data):
    # detect a kick then return the acceleration to 3 decimal places
    acceleration = calculate_acceleration_sum(motion_data)
    if acceleration >= KICK_THRESHOLD_LOW:
       rounded_acceleration = round(acceleration, 3)  # Return raw acceleration to 3 decimal places for further scaling
       return rounded_acceleration
    return None

def start_console_timer(remaining_time):
    #countdown timer printed in console (based on the remaining_time variable)
    print(f"{remaining_time} seconds remaining")
    
def start_led_timer(remaining_time):
    # displays a countdown timer on sense hat leds 
    if remaining_time >= 10:
            sense.show_message(str(remaining_time), text_colour=[255, 255, 0], scroll_speed=0.05)
    else:
            sense.show_letter(str(remaining_time), text_colour=[255, 255, 0])

def main():
    print("Starting round...")
    clear_sense_hat()

    remaining_time = ROUND_DURATION

    # Show countdown on Sense HAT LEDs and colsole
    while remaining_time>0:

        start_led_timer(remaining_time)
        start_console_timer(remaining_time)

        i=0
        # Detect kicks and update metrics
        while i<5:
            motion_data = get_motion_data()
            kick_intensity = detect_kick(motion_data)
            if kick_intensity:
                update_metrics(kick_intensity)  # Store raw intensity for analysis
            time.sleep(0.2)
            i+=1
        
        remaining_time -= 1
    clear_sense_hat()
    # Display final summary after the round
    print_metrics()
    print("Round complete!")


if __name__ == "__main__":
    main()