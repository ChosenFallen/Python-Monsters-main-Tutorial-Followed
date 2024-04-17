from enum import Enum, auto
from sys import exit

import pygame
from pygame.math import Vector2 as vector

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
TILE_SIZE = 64
ANIMATION_SPEED = 6
BATTLE_OUTLINE_WIDTH = 4


class COLORS(Enum):
    WHITE = "#f4fefa"
    PURE_WHITE = "#ffffff"
    DARK = "#2b292c"
    LIGHT = "#c8c8c8"
    GRAY = "#3a373b"
    GOLD = "#ffd700"
    LIGHT_GRAY = "#4b484d"
    FIRE = "#f8a060"
    WATER = "#50b0d8"
    PLANT = "#64a990"
    BLACK = "#000000"
    RED = "#f03131"
    BLUE = "#66d7ee"


class WORLD_LAYER(Enum):
    WATER = auto()
    BG = auto()
    SHADOW = auto()
    MAIN = auto()
    TOP = auto()


class BATTLE_POSITIONS(Enum):
    class LEFT(Enum):
        TOP = (360, 260)
        CENTER = (190, 400)
        BOTTOM = (410, 520)

    class RIGHT(Enum):
        TOP = (900, 260)
        CENTER = (1110, 390)
        BOTTOM = (900, 550)


class BATTLE_LAYERS(Enum):
    OUTLINE = auto()
    NAME = auto()
    MONSTER = auto()
    EFFECTS = auto()
    OVERLAY = auto()


class BATTLE_CHOICES(Enum):
    class FULL(Enum):
        class FIGHT(Enum):
            POS = vector(30, -60)
            ICON = "sword"

        class DEFEND(Enum):
            POS = vector(40, -20)
            ICON = "shield"

        class SWITCH(Enum):
            POS = vector(40, 20)
            ICON = "arrows"

        class CATCH(Enum):
            POS = vector(30, 60)
            ICON = "hand"

    class LIMITED(Enum):
        class FIGHT(Enum):
            POS = vector(30, -40)
            ICON = "sword"

        class DEFEND(Enum):
            POS = vector(40, 0)
            ICON = "shield"

        class SWITCH(Enum):
            POS = vector(30, 40)
            ICON = "arrows"
