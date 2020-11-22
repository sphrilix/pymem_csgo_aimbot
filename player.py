from point3 import Point3

# Implementation of a general player of the game
class Player:

    # Position of the player
    position: Point3

    # Team id of the player
    team_id: int

    # Constructs a new object of a player with the given arguments
    def __init__(self, position: Point3, team_id: int):
        self.position = position
        self.team_id = team_id

    # Returns a textual representation of a player
    def __str__(self):
        return str(self.position) + ", " + str(self.team_id)