from abc import abstractmethod, ABC


# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers


class FibonacciNumbers:
    number = 0
    number_two = 1

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        ret = self.number
        if self.value >= 0:
            self.value -= 1
            self.number, self.next_number = self.number_two, self.number + self.number_two
            return ret
        else:
            raise StopIteration


for i in FibonacciNumbers(10):
    print(i)

# 2 Implement generator for Fibonacci numbers


def fib_generator(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


# 3. Write generator expression that returns square numbers of integers from 0 to 10
square_numbers_generator = (numb ** 2 for numb in range(0, 11))

for i in square_numbers_generator:
    print(f'elem {i}')


# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def screen(self):
        return 'screen'

    def keyboard(self):
        return 'keyboard'

    def touchpad(self):
        return 'touchpad'

    def webcam(self):
        return 'webcam'

    def ports(self):
        return 'port-HDMI, type-C, port-USB,'

    def dynamics(self):
        return 'dynamics'


HP = HPLaptop()
print(HP.webcam())


# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.
class Car(ABC):
    def drive(self):
        return 'drive'

    def stop(self):
        return 'stop'

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError
