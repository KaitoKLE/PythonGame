from collections import namedtuple
from dataclasses import dataclass

from pygame import Surface
from numpy import array


@dataclass
class MapData:
    """To store map information"""
    map_name: str
    ts_path: str
    player_spawn: list
    npc_locations: list
    map_size: tuple
    layers: list


@dataclass
class MapLayer:
    array: array
    image: Surface


class Size(namedtuple('Size', ['width', 'height'])):
    def __str__(self):
        return f'{self.width}x{self.height}'


class Position(namedtuple('Position', ['x', 'y'])):
    def __str__(self):
        return f'({self.x}, {self.y})'


UIColors = namedtuple('UIColors', ['primary', 'secondary'])
