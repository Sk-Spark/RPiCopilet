import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

# Disable warnings
GPIO.setwarnings(False)

# Set up servo
servo = GPIO.PWM(2, 50) # GPIO 2 for PWM with 50Hz
servo.start(0)

# Swipe servo
for i in range(3):
    for angle in range(0, 181, 1):
        duty_cycle = float(angle) / 10.0 + 2.5
        servo.ChangeDutyCycle(duty_cycle)
        time.sleep(0.01)
    for angle in range(180, -1, -1):
        duty_cycle = float(angle) / 10.0 + 2.5
        servo.ChangeDutyCycle(duty_cycle)
        time.sleep(0.01)

# Turn off servo and clean up GPIO
servo.stop()
GPIO.cleanup()