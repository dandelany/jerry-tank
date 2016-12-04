from time import sleep
import RPi.GPIO as GPIO
import pygame



# green - BCM 3 -> PWMA
# orange - BCM 6 -> AIN2
# blue - BCM 9 -> AIN1

# white - BCM 21 -> STBY
# (3v3 power -> VCC, Ground -> common GND)

pygame.init()


GPIO.setmode(GPIO.BCM)

PIN_PWMA = 3
PIN_AIN1 = 9
PIN_AIN2 = 6
PIN_PWMB = 14
PIN_BIN1 = 17
PIN_BIN2 = 22
PIN_STBY = 21

OUT_PINS = {
  'enable': 21, # STBY
  'a_speed': 3, # PWMA
  'a_forward': 9, # A01
  'a_reverse': 6, # A02
  'b_speed': 14, # PWMB
  'b_forward': 22, # B02 (backwards?)
  'b_reverse': 17 # B01
}

def drive_stop(pins):
  GPIO.output(pins['a_forward'], 0);
  GPIO.output(pins['a_reverse'], 0);
  GPIO.output(pins['b_forward'], 0);
  GPIO.output(pins['b_reverse'], 0);

def drive_forward(pins):
  GPIO.output(pins['a_forward'], 1);
  GPIO.output(pins['b_forward'], 1);

def drive_reverse(pins):
  GPIO.output(pins['a_reverse'], 1);
  GPIO.output(pins['b_reverse'], 1);

def drive_left_spin(pins):
  GPIO.output(pins['a_forward'], 1);
  GPIO.output(pins['b_reverse'], 1);

def drive_right_spin(pins):
  GPIO.output(pins['b_forward'], 1);
  GPIO.output(pins['a_reverse'], 1);

GPIO.setup(PIN_PWMA, GPIO.OUT)
GPIO.setup(PIN_AIN1, GPIO.OUT)
GPIO.setup(PIN_AIN2, GPIO.OUT)
GPIO.setup(PIN_PWMB, GPIO.OUT)
GPIO.setup(PIN_BIN1, GPIO.OUT)
GPIO.setup(PIN_BIN2, GPIO.OUT)
GPIO.setup(PIN_STBY, GPIO.OUT)

pwm_a = GPIO.PWM(PIN_PWMA, 50)
pwm_b = GPIO.PWM(PIN_PWMB, 50)

try:
  pwm_a.start(50)
  pwm_b.start(50)
  
  while not finished:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        finished = True

      if event.type == pygame.KEYDOWN:
        if event.key == 273:
          print('forward')
          drive_forward(OUT_PINS)

        elif event.key == 274:
          print('reverse')
          drive_reverse(OUT_PINS)

        elif event.key == 275:
          print('right')
          drive_right_spin(OUT_PINS)

        elif event.key == 276:
          print('left')
          drive_left_spin(OUT_PINS)

      if event.type == pygame.KEYUP:
        print('up', event)
        drive_stop(OUT_PINS)

except KeyboardInterrupt:
  print "exiting..."

finally:
  print "cleaning up..."
  pwm_a.stop()
  GPIO.cleanup()

