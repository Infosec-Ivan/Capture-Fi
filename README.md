<h1 align="center">Capture-Fi 🛜</h1>

**Capture-Fi** is a lightweight tool built with **Python** and **HTML**, designed for **Wi-Fi phishing**.  
It enables the setup of an **Evil Twin attack**, allowing you to capture Wi-Fi credentials by mimicking a legitimate access point.

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

To set up **Capture-Fi**, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Infosec-Ivan/Capture-Fi.git
   cd Capture-Fi



## Setup Process

To set up your Evil Twin attack with a captive portal, follow these steps:

### 1. Install Required Tool

Choose one of the following tools for your setup:
- **Airgeddon**
- **Fluxion**
- **WiFi Phisher**

For this example, we'll use **Airgeddon**. Install it with:
```bash
sudo apt update
sudo apt install airgeddon



**nevigate to the Capture-Fi directory and start server.py:**

`python server.py`

**open new terminal and start airgeddon search for captive portal conf file and add your ip and server.py port**
`http://<your-IP:8000>`

After victim connected to your fake AP the captive portal will start in index.html and when victim enter the wifi passoword the cred will shown in the terminal