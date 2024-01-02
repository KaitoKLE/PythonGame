 # Python Game

![image](https://github.com/KaitoKLE/PythonGame/assets/106547815/750fdf22-9a3c-44ad-9281-2ad76fb8a63b)

This is a WIP simple Python game built with Pygame.

### Prerequisites
You will need Python 3 and Pygame installed.

### Running the Game
The main entry point for the game is `main.py`. To run it:
```
python3 main.py
```
Use the arrow keys to move the player sprite around the map.
You cannot pass through Red tiles. The game has NPC sprites.
Player and NPC collides.

### Some (interesting?) features
- Player and NPC.
- Camera that follows the player. In the future, it will detect in-screen elements.
- Player and NPC can collide, plus, no one can step out of the map.
- Read map from json file. In the future, more data will be read from json files, like game configuration and such.
- Relatively modular. Still a WIP and getting better.
- Actually the tiles are 64x64, but you can change it by updating the global constant TILES_SIZE. Map tiles and everyone in it, player and NPC included, will be of that size. However, the images will need to be rescaled to the new size.
- More incoming soon!

## License
This project is open source and available under the [MIT License](https://opensource.org/license/mit/).
