from player import Player
from point3 import Point3


# Implementation of an enemy.
class Enemy(Player):

    # Health points of the enemy
    hp: int

    # Active status
    dormant: int

    # Constructs a new enemy object with given arguments
    def __init__(self, position: Point3, team_id: int, hp: int, dormant: int):
        self.hp = hp
        self.dormant = dormant
        super().__init__(position, team_id)

    # Return a textual representation of an enemy
    def __str__(self):
        return "Enemy: " + super().__str__() + str(self.hp) + ", " + str(self.dormant)