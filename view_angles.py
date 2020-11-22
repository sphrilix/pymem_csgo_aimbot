# Implementation of the view angles
class ViewAngles:

    # Pitch of the view angles
    pitch: float

    # Yaw of the view angles
    yaw: float

    # Roll of the view angles
    roll: float

    # Constructs a new object of view angles with given arguments
    def __init__(self, pitch: float, yaw: float, roll: float):
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll

    # Returns a textual representation of view angles
    def __str__(self):
        return "pitch: " + str(self.pitch) + "\\nyaw: " + str(self.yaw) + "\\nroll: " + str(self.roll)
