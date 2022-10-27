import math 

from .simulator import simulate
from .utils import toRadians

class Tello():
    def __init__(self, name, position = (30, 25, 180), ground=(260, 260)):
        x, y, angle = position
        self.position = (x, y, 0, angle)
        self.ground = ground
        self.history = [self.position]
        self.photos = []
        
    def connect(self):
        print('Drone connected!')

    def takeoff(self):
        x, y, z, angle = self.position
        
        if z != 0:
            raise Exception("Drone is already flying!") 
        
        self.position = (x, y, 80, angle)

        self._pushState()
        print('Drone flying!')
        
    def land(self):
        x, y, z, angle = self.position
        
        if z == 0:
            raise Exception("Drone is already landed!") 
        
        self.position = (x, y, 0, angle)
        self._pushState()
        print('Drone landed!')

    def move_forward(self, distance: int):
        self._move(0, distance)

    def move_back(self, distance: int):
        self._move(180, distance)

    def move_left(self, distance: int):
        self._move(-90, distance)

    def move_right(self, distance: int):
        self._move(90, distance)

    def rotate_clockwise(self, direction: int):
        self._rotate(direction)

    def rotate_counter_clockwise(self, direction: int):
        self._rotate(-direction)

    def move_up(self, distance: int):
        self._move_z(distance)

    def move_down(self, distance: int):
        self._move_z(-distance)

    def flip_left(self):
        self._flip('left')

    def flip_right(self):
        self._flip('right')

    def flip_forward(self):
        self._flip('forward')

    def flip_back(self):
        self._flip('back')
        
    def take_photo(self):
        self.photos.append(self.position)
        
    def simulate(self):
        simulate(self)
        
    def _pushState(self):
        self.history.append(self.position)
        
    def _popState(self):
        self.history.pop()
        
    def _move(self, direction, distance):
        x, y, z, angle = self.position
        
        radians = toRadians(angle + direction)
        dx = math.sin(radians) * distance
        dy = math.cos(radians) * distance
        
        self.position = (x + dx, y + dy, z, angle)
        self._pushState()
        
    def _move_z(self, distance: int):
        x, y, z, angle = self.position
        
        self.position = (x, y, z + distance, angle)
        self._pushState()
        
    def _rotate(self, direction):
        x, y, z, angle = self.position
        
        newAngle = direction + angle
        
        while (newAngle < 0):
            newAngle += 360
            
        while (360 <= newAngle):
            newAngle -= 360
            
        self.position = (x, y, z, newAngle)
        self._popState()
        self._pushState()
        
    def _flip(self, direction: str):
        print('Flipped ' + direction + '!')
