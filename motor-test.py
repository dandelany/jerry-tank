import RPi.GPIO as GPIO

counter = 0

try:
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(25, GPIO.IN)
  
  print "port 25 is", GPIO.input(25)
  
except KeyboardInterrupt:
  print "exiting at", counter

finally:
  GPIO.cleanup()

