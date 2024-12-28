from blynk_updater import update_blynk

# Metrics state variables
total_power = 0.0
kick_count = 0
kick_intensities = []  # use an array to store kick intensities 

def calculate_acceleration_sum(motion_data):
    #use motion date from 3 axis xyz to make a acceraltion sum
    x = abs(motion_data['x'])
    y = abs(motion_data['y'])
    z = abs(motion_data['z'])
    return x + y + z

def update_metrics(intensity):
    #update the metrics every time there is a kick detected in main.py
    global total_power, kick_count, kick_intensities
    kick_count += 1 
    total_power += intensity #adds the intensity to the total power measurement
    kick_intensities.append(intensity) # adds the intensity to the kick intensities array
    update_blynk_metrics(kick_count, intensity)
 
def update_blynk_metrics(kick_count, intensity):
    kick_count_blynk = get_kick_count(kick_count)
    average_power = get_average_power()
    kick_intensity_blynk = intensity
    update_blynk(kick_count_blynk, average_power, kick_intensity_blynk)

def get_kick_count(kick_count):
    return kick_count
    
def get_kick_intensity(kick_intensity):
    if kick_intensity > 1:
        kick_intensity 
    elif kick_intensity == 0: 
        return 0

def get_average_power():
    # takes total power and devides by number of kicks to determine average power
    if kick_count >= 1:
        return total_power / kick_count 
    else:
        return 0

def print_metrics():
    # prints a summary of the round
    print(f"Total Kicks: {kick_count}")
    
    print(f"Average Power: {get_average_power():.2f}")
    
    print(f"Kick Intensities: {kick_intensities}")
    
