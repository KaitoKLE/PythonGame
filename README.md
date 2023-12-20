 # Python Game

This is a WIP simple Python game built with Pygame.
WARNING: The current state of the project may require to make some modifications before being able to fully run.

## Getting Started

These instructions will help you run the game on your local machine.

### Prerequisites

You will need Python 3 and Pygame installed. 

To install Pygame:

```
python3 -m pip install pygame
```

### Running the Game

The main entry point for the game is `main.py`. To run it:

```
python3 main.py
```

Use the arrow keys to move the player sprite around the screen. 

The game has NPC sprites of different colors. If the player collides with an NPC, they will be pushed back.

## Code Overview

**main.py** - Handles game initialization, logging, and manages the main game loop.

**game.py** - Contains the Game class which handles game logic like movement, collisions, etc.

**character.py** - Character class to represent player and NPCs. Stores position and sprite data.

**display.py** - Display class handles rendering the Pygame display and sprites.

**tiles.py** - Contains TileSet and TileMap classes for rendering tilemap backgrounds.

## Known prolems:
- **X & Y inverted**: I accidentally inverted the X and Y coordinates in the game logic, so there will be some confusing logic there... The TileSet and TileMap classes are the only ones that process then correctly. Sorry about that, I promise I will fix it, eventually :P

## License

This project is open source and available under the [MIT License](https://opensource.org/license/mit/).
