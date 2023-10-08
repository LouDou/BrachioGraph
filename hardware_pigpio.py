import pigpio

class Driver():
    def __init__(self, s_pin=14, e_pin=15, p_pin=18):
        self._s_pin = s_pin
        self._e_pin = e_pin
        self._p_pin = p_pin

    def start(self):
        pigpio.exceptions = False
        self.rpi = pigpio.pi()
        self.rpi.set_PWM_frequency(self._s_pin, 50)
        self.rpi.set_PWM_frequency(self._e_pin, 50)
        self.rpi.set_PWM_frequency(self._p_pin, 50)
        pigpio.exceptions = True

    def set_servo_pulsewidth(self, gpio, angle):
        self.rpi.set_servo_pulsewidth(gpio, angle)
    
    def get_servo_pulsewidth(self, gpio):
        return self.rpi.get_servo_pulsewidth(gpio)

