import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.output(2, False)
GPIO.output(3, False)
GPIO.output(4, False)
GPIO.output(5, False)
GPIO.output(6, False)
GPIO.output(7, False)
GPIO.output(8, False)
GPIO.output(9, False)
GPIO.output(10, False)
GPIO.output(11, False)
GPIO.output(12, False)
GPIO.output(25, False)
GPIO.output(14, False)
GPIO.output(15, False)
GPIO.output(16, False)
GPIO.output(17, False)
GPIO.output(23, False)
GPIO.output(24, False)

GPIO.cleanup()
