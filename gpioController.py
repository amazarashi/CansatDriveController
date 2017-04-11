import RPi.GPIO as GPIO

class GPIO(object):

    def __init__(self):
        self.pin1 = 11 #p0
        self.pin2 = 12 #p5
        self.pin3 = 13 #p3
        self.pin3 = 15 #p4
        self.initGPIO()

    def initGPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pin3, GPIO.OUT)
        GPIO.setup(self.pin4, GPIO.OUT)

    def GoStraight(self):
        return
