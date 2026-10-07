# Aster

A simple Asteroids-style arcade game built with Python and Pygame as a
Boot.dev learning project.

## Gameplay

Pilot your ship, dodge asteroids, and shoot them to split larger rocks into
smaller ones. The game ends when your ship collides with an asteroid.

### Controls

| Key | Action |
| --- | --- |
| `A` | Turn left |
| `D` | Turn right |
| `W` | Move forward |
| `S` | Move backward |
| `Space` | Fire |

Close the game window to quit.

## Requirements

- Python 3.13 or later
- [uv](https://docs.astral.sh/uv/)

Pygame is installed automatically from the project dependencies.

## Run the game

From the project directory, install the dependencies and start the game:

```bash
uv sync
uv run python main.py
```

## Project layout

| File | Purpose |
| --- | --- |
| `main.py` | Initializes Pygame and runs the game loop |
| `player.py` | Player ship movement, rotation, and shooting |
| `asteroid.py` | Asteroid movement, collision shape, and splitting |
| `asteroidfield.py` | Spawns asteroids at the edges of the screen |
| `shot.py` | Player projectiles |
| `circleshape.py` | Shared circular sprite and collision logic |
| `constants.py` | Screen size and gameplay settings |
| `logger.py` | Writes sampled game state and gameplay events to JSONL files |

## Logging

While the game is running, it writes `game_state.jsonl` and
`game_events.jsonl` in the project directory. These files are local runtime
logs and are excluded from version control, the logger is also provided by boot dev for evaluation and testing
