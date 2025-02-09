from adafruit_servokit import ServoKit

# Initialize the PCA9685 with 16 channels
kit = ServoKit(channels=16)

# Configure each servo (Optional: Remove if unnecessary)
for i in range(7):
    kit.servo[i].set_pulse_width_range(500, 2500)

def set_servo_angle(servo_num, angle):
    """Set angle for a specific servo"""
    if 0 <= angle <= 180 and 0 <= servo_num < 7:
        if kit.servo[servo_num].angle != angle:  # Avoid redundant updates
            kit.servo[servo_num].angle = angle
            print(f"Servo {servo_num} set to {angle} degrees")
    else:
        print("Invalid angle or servo number")

def main():
    print("Multiple Servo Control")
    print("Enter 'q' to quit")
    
    while True:
        try:
            # Get servo number
            servo_input = input("\nEnter servo number (0-6): ")
            if servo_input.lower() == 'q':
                break
                
            servo_num = int(servo_input)
            
            # Get angle
            angle = float(input("Enter angle (0-180): "))
            
            # Set the servo
            set_servo_angle(servo_num, angle)
            
        except ValueError:
            print("Please enter valid numbers")
        except KeyboardInterrupt:
            break
    
    print("\nProgram ended")

if __name__ == "__main__":
    main()
