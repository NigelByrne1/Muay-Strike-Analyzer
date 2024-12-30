import BlynkLib
from config import BLYNK_AUTH

blynk = BlynkLib.Blynk(BLYNK_AUTH)

def update_blynk(kick_count, average_power, kick_intensity):
    blynk.virtual_write(0, kick_count)
    blynk.virtual_write(1, average_power)
    blynk.virtual_write(2, kick_intensity)
    
    # blynk console print for diagnostics 
    print("Updating Blynk...")
    print(f"Sent kick_count: {kick_count}")
    print(f"Sent intensities: {kick_intensity}")
    print(f"Sent average power: {average_power}")

def update_blynk_remaining_time(remaining_time):
    blynk.virtual_write(5, remaining_time)
