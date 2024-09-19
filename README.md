![Static Badge](https://img.shields.io/badge/Capture-Fi-black?style=for-the-badge)

<h1 align="center">Capture-Fi 🛜</h1>

**Capture-Fi** is a lightweight tool built with **Python** and **HTML** It is a Wi-Fi Phishing Template with a Python server that can capture Wi-Fi password through **evil twin method**

## Features
```- Wi-Fi phishing using an Evil Twin method.```<br>
```- Customizable fake login page using HTML.```<br>
```- Lightweight and easy to use.```<br>
```- Built-in Python server to host the phishing page.```<br>
```- Compatible with a wide range of devices, including Raspberry Pi Zero W, M5StickC Plus, and ESP32/ESP8266.```

## Prerequisites
- Python 3.x
- Wi-Fi adapter with monitor mode and packet injection support (necessary)
- Parrot OS or any other Linux distribution (necessary)
- If you want to create a portable Wi-Fi phishing device, you can choose from the following devices:
  - **Raspberry Pi Zero W**: Compact and versatile, ideal for various hacking projects.
  - **M5StickC Plus**: A small, easy-to-use microcontroller with built-in display.
  - **ESP32/ESP8266**: Popular microcontrollers with Wi-Fi capabilities, suitable for a range of IoT applications.
  
## Installation

1. **Clone the Repository**:<br>
   ```git clone https://github.com/Infosec-Ivan/Capture-Fi.git```<br>
   ```cd Capture-Fi```<br>
   ```python server.py```<br>
   <img src="https://github.com/Infosec-Ivan/Capture-Fi/blob/main/Screenshot_20240919_203508.png" alt="Screenshot" width="400"/>

**Open Browser**<br>
`http://<yourIP:8080>`

<img src="https://github.com/Infosec-Ivan/Capture-Fi/blob/main/IMG_20240919_204551.JPG" alt="Screenshot" width="100"/>

```As victim POV he will enter the password```

<img src="https://github.com/Infosec-Ivan/Capture-Fi/blob/main/IMG_20240919_204540.JPG" alt="Screenshot" width="100"/>

```The password will be captured and will be shown in terminal```

<img src="https://github.com/Infosec-Ivan/Capture-Fi/blob/main/Screenshot_20240919_204327.png" alt="Screenshot" width="400"/>
