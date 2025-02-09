# Multi-Servo Control using Raspberry Pi and PCA9685

This project controls 7 servo motors using a Raspberry Pi and a PCA9685 PWM driver via I2C communication. The setup allows you to adjust servo angles interactively.

## Components Used
- **Raspberry Pi** (Any Model with I2C support)
- **PCA9685 16-Channel PWM Driver**
- **7x Servo Motors**
- **18650 Li-ion Battery Pack** (External Power Supply for Servos)
- **Jumper Wires**

## Circuit Connection
![image](https://github.com/user-attachments/assets/a778bbb2-d996-4a2a-8c0f-95562ea9340e)

### PCA9685 to Raspberry Pi:
- **VCC (PCA9685) → 5V (Raspberry Pi)**
- **GND (PCA9685) → GND (Raspberry Pi)**
- **SDA (PCA9685) → GPIO 2 (SDA, Raspberry Pi)**
- **SCL (PCA9685) → GPIO 3 (SCL, Raspberry Pi)**

### Servo Motors to PCA9685:
- **Signal Wire (Yellow/Orange) → PWM Channels (0 to 6) on PCA9685**
- **VCC (Red) → V+ on PCA9685**
- **GND (Brown/Black) → GND on PCA9685**

### Battery Connection:
- **Battery Positive (+) → V+ on PCA9685**
- **Battery Negative (−) → GND on PCA9685**

## Installation and Setup
### 1. Enable I2C on Raspberry Pi
```sh
sudo raspi-config
# Navigate to 'Interfacing Options' > Enable I2C
```

### 2. Install Required Libraries
```sh
pip install adafruit-circuitpython-servokit
```

### 3. Run the Script
```sh
python3 multi_servo_control.py
```

## Code Explanation
- **Initialize PCA9685 with 16 channels**
- **Set pulse width range for servos**
- **Interactive input to control servos**

```python
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
for i in range(7):
    kit.servo[i].set_pulse_width_range(500, 2500)
```

### Function to Control Servo Angle
```python
def set_servo_angle(servo_num, angle):
    if 0 <= angle <= 180 and 0 <= servo_num < 7:
        if kit.servo[servo_num].angle != angle:
            kit.servo[servo_num].angle = angle
            print(f"Servo {servo_num} set to {angle} degrees")
    else:
        print("Invalid angle or servo number")
```

## Error 
![image](https://github.com/user-attachments/assets/3d947cde-cb4f-4b62-9ff2-b0196ec34aa0)

