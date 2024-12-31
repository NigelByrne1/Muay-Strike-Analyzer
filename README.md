# Muay Strike Analyzer

![Muay Strike Analyzer Logo](https://i.ibb.co/nnwXkkV/0101010101-1.png "Muay Strike Analyzer Logo")

#### Student Name: *Nigel Byrne*   Student ID: *20058969*

The ***Muay Strike Analyzer*** is a focused training tool developed to measure and analyze the power of kicks in Muay Thai training. By leveraging a Raspberry Pi equipped with a Sense HAT, this device captures motion data specifically to detect and evaluate kicks. The aim is to give fighters valuable insights into their kicking performance, helping them train smarter and track improvements over time.

## Tools, Technologies, and Equipment

### **Hardware:**
   - **Raspberry Pi 4:** The core of the device, running the analysis software.
   - **Sense HAT:** Captures motion data using its built-in accelerometer.
   - **Secure Straps:** Ensures the device is attached securely to the punching bag.
   - **Internet Connectivity:** Required for the Blynk app to provide real-time feedback.

### **Software:**
   - **Python:** Handles motion data collection, processing, and communication with the Blynk app.
   - **Blynk App:** A user-friendly interface for real-time monitoring and adjusting training parameters.

### **Networking/IoT:**
   - **Blynk Cloud:** Facilitates the live visualization of performance metrics and remote control of settings.

## Features

1. **Kick Detection and Analysis:**
   - Uses the Sense HAT’s accelerometer to identify kicks based on customizable thresholds.
   - Measures the intensity of each detected kick and tracks it throughout the session.

2. **Real-Time Feedback:**
   - Displays a countdown timer for training rounds using the Sense HAT LEDs.
   - Provides immediate feedback on kick intensity through the Blynk app.

3. **Performance Tracking:**
   - Tracks the total number of kicks, average kick intensity, and the intensity of each kick.
   - Offers a detailed summary of the training session at the end.

4. **Customizable Training Parameters:**
   - Adjust round duration and kick sensitivity thresholds directly from the Blynk app.

5. **Interactive Training Experience:**
   - Combines data-driven insights with a user-friendly experience to enhance training effectiveness.

## How It Works

The device is attached securely to a punching bag and starts tracking as soon as the round begins. Every detected kick is analyzed, and the data is sent to the Blynk app for real-time feedback. At the end of the session, users can review their performance metrics, including the total number of kicks and average intensity.

## How to Use It

1. **Setup:**
   - Attach the Raspberry Pi and Sense HAT securely to the punching bag.
   - Connect the Raspberry Pi to the internet for Blynk integration.

2. **Running the App:**
   - Open the Blynk app and ensure the Muay Strike Analyzer is connected.
   - Adjust training parameters such as round duration and kick threshold.
   - Start a session using the app’s virtual start button.

3. **During the Session:**
   - Observe the countdown timer on the Sense HAT LEDs.
   - View real-time feedback on kick count and intensity in the Blynk app.

4. **Review Performance:**
   - After the session, check the summary metrics printed in the console for a complete breakdown of your performance.

## Project Repository

#### [GitHub Repository](https://github.com/NigelByrne1/MuayStrikeAnalyzer)

## Project Graphic

![Muay Strike Analyzer Graphic](https://i.ibb.co/zhMck5D/2.png "Muay Strike Analyzer Graphic")

## Devices Images in Action
- Velcro was attached to device case and ratchet strap the ratchet strap was then wrapped around the bag
![Muay Strike Analyzer Graphic](https://i.ibb.co/MGDQXhS/3.png "Muay Strike Analyzer Graphic")

![Muay Strike Analyzer Graphic](https://i.ibb.co/tcwd9pY/4.png "Muay Strike Analyzer Graphic")

## Video of Device in Action

[![YouTube Video](https://img.youtube.com/vi/k_CgQP0xwYE/0.jpg)](https://youtu.be/k_CgQP0xwYE)

