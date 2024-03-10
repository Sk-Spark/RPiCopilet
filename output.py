
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin = 2
servo_pin = 13

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)

led = GPIO.PWM(led_pin, 100)
led.start(0)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

for i in range(3):
    for angle in range(0, 181, 5):
        servo.ChangeDutyCycle(2 + (angle / 18))
        led.ChangeDutyCycle(angle / 1.8)
        print("Servo angle: ", angle)
        time.sleep(0.1)
    for angle in range(180, -1, -5):
        servo.ChangeDutyCycle(2 + (angle / 18))
        led.ChangeDutyCycle(angle / 1.8)
        print("Servo angle: ", angle)
        time.sleep(0.1)

servo.stop()
led.stop()
GPIO.cleanup()
