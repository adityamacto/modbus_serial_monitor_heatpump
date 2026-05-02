# Modbus Serial Monitor for Heat Pump (Python)

A simple Python-based serial monitoring tool to capture and classify Modbus RTU packets in real time.

## Features

* Reads live data from serial port using PySerial
* Displays packets in readable HEX format
* Classifies packets into:

  * Query (Master → Slave)
  * Response (Slave → Master)
* Timestamped logging

## 🛠 Tech Stack

* Python
* PySerial

## 📷 Sample Output

```
[12:45:10] Query: 01 03 00 00 00 02 C4 0B
[12:45:11] Response: 01 03 04 00 64 00 C8 F1 84
```

## ⚙️ Setup & Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the script:

```
python app.py
```

3. Enter your COM port when prompted

## Use Cases

* Debugging Modbus communication
* PLC / Arduino serial monitoring
* Industrial protocol learning

Built for learning and real-time debugging of serial communication.
