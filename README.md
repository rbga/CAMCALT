# CAMCALT - Complex Animal Movement Capture and Live Transmission
<img src="https://github.com/rbga/CAMCALT/assets/75168756/da957696-42fb-4374-9681-9680f4005885" alt="Image Alt Text" width="300" height="200">


## Introduction

CAMCALT (Complex Animal Movement Capture and Live Transmission) is a forest surveillance and monitoring system designed to capture complex animal movements and provide live video feed wirelessly from any part of the world. It aims to prevent hunting and poaching, enhancing forest security like a military restricted area.

## Features

- Live video feed and remote monitoring from any location via Internet of Things (IoT).
- Motion detection with automatic camera and GPS activation, sending notifications to the security personnel.
- High-quality photo capture and 10-second video recording on demand.
- Poacher detection using advanced image processing algorithms.
- Train Poacher to CAMCALT to recognize specific poachers in the future.
- GPS location tracking of the device for precise monitoring.

## Components

CAMCALT consists of the following key components:

- Central Microcontroller: Raspberry Pi 3 Model B with ARMv7 Quad Core Processor and integrated Wi-Fi and Bluetooth.
- Pi Camera Module: Captures high-resolution images and supports 1080p video recording.
- GPS Module: Tracks the location of the device.
- Motion Sensor: Utilizes a passive infrared sensor (PIR) for motion detection.
- USB Power In: Rechargeable power bank provides the necessary power supply.

## Graphical User Interface

The user-friendly GUI offers various functionalities:

- **Take Picture**: Capture high-quality photos of the detected motion.
- **Record Video**: Record 10-second videos of the live feed.
- **Live Feed**: Obtain real-time video feed from the camera.
- **Poacher Detection**: Detect known poachers using image processing algorithms.
- **Train Poacher to CAMCALT**: Train the device to recognize specific poachers for future detection.
- **GPS Location**: Get the current GPS coordinates of the device for precise tracking.

## How to Use

To use CAMCALT, simply execute the main Python file "errorda.py," which will launch the graphical user interface. The application will provide options to capture photos, record videos, and detect poachers when motion is detected.

Please refer to the provided User Manual for detailed instructions and setup guidelines.

## Code Descriptions

### `camcalt.sh`

A clickable shell script that executes the main Python file "errorda.py" and branches into other Python files to run various functionalities.

### `camcalt.py`

Python script responsible for motion detection using PIR sensor. Upon detection, it triggers other Python scripts for capturing photos, recording videos, and detecting poachers.

### `notify.py`

Python script that sends a notification message when motion is detected. It uses the Pushetta API for this purpose.

### `cap1.py`

Python script that captures a series of burst images using the Pi Camera Module. The number of images to capture is set by user input.

### `errorda.py`

Main Python script that runs the CAMCALT system. It contains the user interface and provides options to interact with various functionalities.

### `picam.txt`

Python script that runs the Pi Camera Module to provide a live video feed at 25 fps and a resolution of 640x480 pixels.

### `record.py`

Python script that records a 5-second video using the Pi Camera Module with a resolution of 640x480 pixels and a frame rate of 90 fps.

### `face_rec.py`

Python script that performs face recognition using the Pi Camera Module. It detects and recognizes known poachers by comparing captured images with stored samples.

### `gps.py`

Python script that reads GPS data from the Neo 6M GPS module connected to the Raspberry Pi and displays the latitude and longitude coordinates.

### `connector.py`

Python script that sends an alert/notification when a poacher is detected. It uses the Pushetta API for this purpose.

### Other Supporting Files

- `haarcascade_frontalface_default.xml`: Haar Cascade classifier file used for face detection in poacher detection.

## Requirements

- Raspberry Pi 3 Model B with Raspbian OS
- Python (OpenCV, Tkinter, and other required libraries)
- Pi Camera Module and GPS Module
- Internet connectivity for remote monitoring

## Documentation and Contact

- User Manual: [Link to User Manual](https://www.slideshare.net/GaneshaanandBalasubr/camcalt-user-manual-91811327)
- For any inquiries or assistance, feel free to contact the project developer on LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/ganeshaanand/)

## License

CAMCALT is an open-source project, and the code is available under the [MIT License](link_to_license).

**Note**: For photos and videos from the project presentation/demo, visit [Project's Website](https://ssr1996.wixsite.com/shreyas-ssr/projects-patents).
