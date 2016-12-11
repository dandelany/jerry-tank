from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

OUT_PINS = {
  'enable': 14, # STBY
  'a_speed': 17, # PWMA
  'a_forward': 15, # AIN1
  'a_reverse': 18, # AIN2
  'b_speed': 2, # PWMB
  'b_forward': 3, # BIN2 (backwards?)
  'b_reverse': 4 # BIN1
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

def setup_pins(out_pins, pwm_pin_keys=[], pwm_freq=100):
  for key, pin in out_pins:
    GPIO.setup(pin, GPIO.OUT)
  for key in pwm_pin_keys:
    GPIO.PWM(out_pins[key], pwm_freq)

def main():
  try:
    setup_pins(OUT_PINS, ['a_speed', 'b_speed'], 100);
    pwm_a.start(50)
    pwm_b.start(50)
    GPIO.output(PIN_STBY, 1)

    drive_forward(OUT_PINS)
    sleep(0.5)
    drive_stop(OUT_PINS)
    sleep(0.5)
    drive_reverse(OUT_PINS)
    sleep(0.5)
    drive_stop(OUT_PINS)
    sleep(0.5)
    drive_right_spin(OUT_PINS)
    sleep(0.9)
    drive_stop(OUT_PINS)
    sleep(0.5)
    drive_left_spin(OUT_PINS)
    sleep(0.9)
    drive_stop(OUT_PINS)
    sleep(0.5)

    GPIO.output(PIN_STBY, 0);
    pwm_a.stop()

  except KeyboardInterrupt:
    print "exiting..."

  finally:
    print "cleaning up..."
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()

main()
