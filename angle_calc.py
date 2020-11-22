from math import pi, atan, asin

from enemy import Enemy
from local_player import LocalPlayer


# Class for calculating the angles to the closest enemy
class AngleCalc:

    # Local player
    player: LocalPlayer

    # Closest Enemy
    enemy: Enemy

    # Yaw of the local player
    yaw: float

    # Pitch of the local player
    pitch: float

    # Constructs a new angle calc object with given arguments
    def __init__(self, player: LocalPlayer, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.yaw = self.player.view_angles.yaw
        self.pitch = self.player.view_angles.pitch

    # Normalizing yaw it only can be between [-180, 180]
    @staticmethod
    def normalize_yaw(yaw):
        if yaw > 180:
            yaw -= 360
        elif yaw < -180:
            yaw += 360
        return yaw

    # Calculating the yaw of the enemy
    def calc_yaw_to_enemy(self):
        delta_x = self.player.position.delta_x(self.enemy.position)
        delta_y = self.player.position.delta_y(self.enemy.position)
        yaw_to_enemy = atan(delta_y / delta_x) * 180 / pi
        if delta_x >= 0.0:
            yaw_to_enemy += 180
        return yaw_to_enemy

    # Calculting the distance from the yaw of the local player to yaw of the enemy
    def calc_dist_yaw(self):
        distance_yaw = self.calc_angle_yaw() - self.yaw
        if distance_yaw < -180:
            distance_yaw += 360
        elif distance_yaw > 180:
            distance_yaw -= 360
        return distance_yaw

    # Normalizing the pitch it only can be between [-89, 89]
    @staticmethod
    def normalize_pitch(pitch):
        if pitch > 89:
            pitch -= 360
        elif pitch < -89:
            pitch += 360
        return pitch

    # Check if a angle is in a valid range
    @staticmethod
    def check_angles(yaw, pitch):
        if yaw > 180 or yaw < -180 or pitch > 89 or pitch < -89:
            return False
        else:
            return True

    # CAlculationg the pitch of the enemy
    def calc_pitch_to_enemy(self):
        delta_z = self.player.position.delta_z(self.enemy.position)
        hyp = self.player.position.distance(self.enemy.position)
        return asin(delta_z / hyp) * 180 / pi
