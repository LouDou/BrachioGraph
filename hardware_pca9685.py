from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685


class PWMServo(servo._BaseServo):
    def set_pulse_width_range(self, min_pulse: int = 750, max_pulse: int = 2250):
        self._pmin = min_pulse
        self._pmax = max_pulse
        self._prange = float(max_pulse - min_pulse)
        super().set_pulse_width_range(min_pulse, max_pulse)

    @property
    def pulsewidth(self):
        return int((self.fraction * self._prange) + self._pmin)

    @pulsewidth.setter
    def pulsewidth(self, value):
        frac = (value - self._pmin) / self._prange
        self.fraction = (value - self._pmin) / self._prange


class Driver():
    def __init__(self, s_pin=14, e_pin=15, p_pin=18):
        self.i2c = busio.I2C(SCL, SDA)
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 50
        self.servos = {
            s_pin: PWMServo(self.pca.channels[0], min_pulse=600),
            e_pin: PWMServo(self.pca.channels[1], min_pulse=600),
            p_pin: PWMServo(self.pca.channels[2], min_pulse=600)
        }

    def start(self):
        pass

    def set_servo_pulsewidth(self, num, angle):
        self.servos[num].pulsewidth = angle

    def get_servo_pulsewidth(self, num):
        return self.servos[num].pulsewidth

