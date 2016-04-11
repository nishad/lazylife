# WiFi Reboot (TL-MR3020)
---
> A Python script to reboot TP-LINK TL-MR3020, 3G Wireless N Router

Optionally, this script will accept `-f` as a parameter to force reboot by avoiding [Y/n] prompt.

### Installation

```
sudo pip install -r requirements.txt
```

### Usage

```
python wifi-reboot.py
```

If you wants to avoid [Y/n} prompt 

```
python wifi-reboot.py -f
```

You can use this as a command line option as

```
cp wifi-reboot.py /usr/local/bin/wifi-reboot
chmod +x /usr/local/bin/wifi-reboot
```