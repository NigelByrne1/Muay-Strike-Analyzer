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

def get_average_power():
    # takes total power and devides by number of kicks to determine average power
    if kick_count > 1:
        return total_power / kick_count 
    elif kick_count == 0: 
        return 0

def print_metrics():
    # prints a summary of the round
    print(f"Total Kicks: {kick_count}")
    print(f"Average Power: {get_average_power():.2f}")
    print(f"Kick Intensities: {kick_intensities}")
