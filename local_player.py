from player import Player
from point3 import Point3
from view_angles import ViewAngles


# Implementation of the local player (you if you are using, which is not recommended!) :P
class LocalPlayer(Player):

    # Current view angles of the local player
    view_angles: ViewAngles

    # Constructs a new enemy object with given arguments
    def __init__(self, position: Point3, team_id: int, view_angles: ViewAngles):
        self.view_angles = view_angles
        super().__init__(position, team_id)