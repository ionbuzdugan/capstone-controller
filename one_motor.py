import RPi.GPIO as GPIO
from time import sleep

# use pin number, not GPIO number
m1_pin = 32		
duty_cycle = 100
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(m1_pin,GPIO.OUT)
pi_pwm = GPIO.PWM(m1_pin,20)
pi_pwm.start(0)
pi_pwm.ChangeDutyCycle(duty_cycle)

# Need to keep this running or pwm stops 
while True:
    pi_pwm.ChangeDutyCycle(duty_cycle)
    sleep(1)