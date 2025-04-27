from machine import Pin, PWM
import time

#servos
servo1 = PWM(Pin(32), freq=50)
servo2 = PWM(Pin(33), freq=50)

def set_servo_angle(pwm, angle):
    duty = int(40 + (angle / 180) * 75)
    pwm.duty(duty)

#motors(IN-PINS)
motor1 = Pin(13, Pin.OUT)
motor2 = Pin(12, Pin.OUT)
motor3 = Pin(14, Pin.OUT)
motor4 = Pin(27, Pin.OUT)

#speedcontrol
ENA = PWM(Pin(21), freq=1000, duty=1000)
ENB = PWM(Pin(22), freq=1000, duty=1000)
ENC = PWM(Pin(26), freq=1000, duty=1000)
END = PWM(Pin(25), freq=1000, duty=1000)

#buttons
button1 = Pin(16, Pin.IN, Pin.PULL_UP)
button2 = Pin(17, Pin.IN, Pin.PULL_UP)
button3 = Pin(18, Pin.IN, Pin.PULL_UP)
button4 = Pin(19, Pin.IN, Pin.PULL_UP)
servo_button = Pin(5, Pin.IN, Pin.PULL_UP)
confirm_button = Pin(15, Pin.IN, Pin.PULL_UP)

#queue to store button presses
queue = []

while True:
    if button1.value() == 0:
        queue.append(1)
        print("Button 1 pressed")
        time.sleep(0.3)

    if button2.value() == 0:
        queue.append(2)
        print("Button 2 pressed")
        time.sleep(0.3)

    if button3.value() == 0:
        queue.append(3)
        print("Button 3 pressed")
        time.sleep(0.3)

    if button4.value() == 0:
        queue.append(4)
        print("Button 4 pressed")
        time.sleep(0.3)

    if servo_button.value() == 0:
        queue.append(5)
        print("Button 5 (servo sequence) pressed")
        time.sleep(0.3)

    if confirm_button.value() == 0 and queue:
        print("Confirmation pressed. Queue:", queue)
        time.sleep(0.3)

        for item in queue:
            print("Dispensing item", item)

            if item == 1:
                motor1.on()
                print("Motor 1 ON")
                time.sleep(1)
                motor1.off()

            elif item == 2:
                motor2.on()
                print("Motor 2 ON")
                time.sleep(1)
                motor2.off()

            elif item == 3:
                motor3.on()
                print("Motor 3 ON")
                time.sleep(1)
                motor3.off()

            elif item == 4:
                motor4.on()
                print("Motor 4 ON")
                time.sleep(1)
                motor4.off()

            elif item == 5:
                print("Servo 1 to 90°")
                set_servo_angle(servo1, 90)
                time.sleep(1.5)

                print("Servo 1 back to 0°")
                set_servo_angle(servo1, 0)
                time.sleep(1)

                print("Servo 2 to 90°")
                set_servo_angle(servo2, 90)
                time.sleep(1)

                print("Servo 2 back to 0°")
                set_servo_angle(servo2, 0)
                time.sleep(1)

        #clearqueue
        queue = []

