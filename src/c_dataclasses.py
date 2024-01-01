from dataclasses import dataclass

import numpy


@dataclass
class MapData:
    name: str
    tile_set_path: str
    npc: list
    collision: numpy.array
    map_shape: numpy.array
