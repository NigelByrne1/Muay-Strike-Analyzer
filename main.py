from metrics import update_metrics, print_metrics, calculate_acceleration_sum
from config import KICK_THRESHOLD_LOW, BLYNK_AUTH
from clearsensehat import clear_sense_hat
from sense_hat import SenseHat
from blynk_updater import update_blynk, update_blynk_remaining_time
import BlynkLib
import time

sense = SenseHat()
blynk = BlynkLib.Blynk(BLYNK_AUTH)
start_round_flag = False

@blynk.on("V3")  # Virtual pin for the start button
def handle_start_button(value):
    global start_round_flag
    if value[0] == "1":  # Button pressed
        start_round_flag = True
        print("Start button pressed!")

@blynk.on("V4")  # Virtual pin for round duration slider
def handle_duration_input(value):
    global round_duration
    round_duration = int(value[0])  # Directly assign the value since Blynk has default/min/max values
    print(f"Updated round duration to {round_duration} seconds")

def wait_for_start():
    global start_round_flag
    print("Waiting for start button press...")
    while start_round_flag == False:
        blynk.run()
        time.sleep(0.1)

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
    print("Starting the App")
    clear_sense_hat()
    update_blynk(0 , 0 , 0) #initialise blynk values
    global start_round_flag
    while True:
        wait_for_start() #wait for button to be true
        print("Starting round...")
        start_round_flag = False # reset the start round flag
        remaining_time = round_duration

        # Show countdown on Sense HAT LEDs and colsole
        while remaining_time>0:
            blynk.run()
            start_led_timer(remaining_time)
            start_console_timer(remaining_time)
            update_blynk_remaining_time(remaining_time)
            
            # Detect kicks and update metrics.  while i with time.sleep built in to make sure it can detect upto 5 kicks a second
            i=0
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