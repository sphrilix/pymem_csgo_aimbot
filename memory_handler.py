import sys
import pymem
from enemy import Enemy
from point3 import Point3
from view_angles import ViewAngles
from local_player import LocalPlayer


# Class which handles everything with the memory using pymem
class MemoryHandler:

    # Offsets from the game
    DW_ENTITY_LIST = 0x4D5239C
    DW_LOCAL_PLAYER = 0xD3DD14
    DW_BONE_MATRIX = 0x26A8
    DW_CLIENT_STATE = 0x58DFE4
    DW_CLIENT_STATE_VIEW_ANGLES = 0x4D90
    M_VEC_ORIGIN = 0x138
    M_I_TEAM_NUM = 0xF4
    M_I_HEALTH = 0x100
    M_B_DORMANT = 0xED
    M_VEC_VIEW_OFFSET = 0x108

    # Object from pymem which reading the memory
    pm: pymem.Pymem()

    # Base offset of the "client.dll"
    client: int

    # Base offset of the "engine.dll"
    engine: int

    # Constructs a new MemoryHandler
    def __init__(self):
        self.pm = pymem.Pymem("csgo.exe")
        self.client = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
        self.engine = pymem.process.module_from_name(self.pm.process_handle, "engine.dll").lpBaseOfDll

    # Returns the local player
    def get_local_player(self):
        return LocalPlayer(self.get_local_player_coords(), self.get_local_player_team_id(),
                           self.get_local_player_view_angles())

    # Returns the offset of the local player
    def get_local_player_offset(self):
        return self.pm.read_int(self.client + self.DW_LOCAL_PLAYER)

    # Returns the coords of the local player
    def get_local_player_coords(self):
        player = self.get_local_player_offset()
        x = self.pm.read_float(player + self.M_VEC_ORIGIN)
        y = self.pm.read_float(player + self.M_VEC_ORIGIN + 0x4)
        z = self.pm.read_float(player + self.M_VEC_ORIGIN + 0x8) + self.get_local_player_view_angles().roll
        return Point3(x, y, z)

    # Returns the view angles of the local player
    def get_local_player_view_angles(self):
        view_angles = self.pm.read_int(self.engine + self.DW_CLIENT_STATE)
        pitch = self.pm.read_float(view_angles + self.DW_CLIENT_STATE_VIEW_ANGLES)
        yaw = self.pm.read_float(view_angles + self.DW_CLIENT_STATE_VIEW_ANGLES + 0x4)
        roll = self.pm.read_float(self.get_local_player_offset() + self.M_VEC_VIEW_OFFSET + 0x8)
        return ViewAngles(pitch, yaw, roll)

    # Returns the id of the team of the local player
    def get_local_player_team_id(self):
        return self.pm.read_int(self.get_local_player_offset() + self.M_I_TEAM_NUM)

    # Returns all alive enemies which are in the entity list
    def get_alive_enemies(self, team_id):
        enemies = []
        for i in range(1, 32):
            entity = self.pm.read_int(self.client + self.DW_ENTITY_LIST + i * 0x10)
            if entity:
                entity_bones = self.pm.read_int(entity + self.DW_BONE_MATRIX)
                try:
                    entity_pos_x = self.pm.read_float(entity_bones + 0x30 * 8 + 0xC)
                    entity_pos_y = self.pm.read_float(entity_bones + 0x30 * 8 + 0x1C)
                    entity_pos_z = self.pm.read_float(entity_bones + 0x30 * 8 + 0x2C)
                    entity_team_id = self.pm.read_int(entity + self.M_I_TEAM_NUM)
                    entity_hp = self.pm.read_int(entity + self.M_I_HEALTH)
                    entity_dormant = self.pm.read_int(entity + self.M_B_DORMANT)
                except:
                    continue
                if team_id != entity_team_id and entity_hp > 0 and not entity_dormant:
                    enemies.append(Enemy(Point3(entity_pos_x, entity_pos_y, entity_pos_z), entity_team_id, entity_hp,
                                         entity_dormant))
        return enemies

    # Returns the closest enemy
    def get_closest_alive_enemy(self):
        player = self.get_local_player()
        enemies = self.get_alive_enemies(player.team_id)
        dist = sys.maxsize * 2 + 1
        enemy = None
        for e in enemies:
            if dist > player.position.distance(e.position):
                dist = player.position.distance(e.position)
                enemy = e
        return enemy

    # Writes a given yaw to the memory
    def write_yaw(self, yaw: float):
        view_angles = self.pm.read_int(self.engine + self.DW_CLIENT_STATE)
        self.pm.write_float(view_angles + self.DW_CLIENT_STATE_VIEW_ANGLES + 0x4, yaw)

    # Writes a given pitch to the memory
    def write_pitch(self, pitch: float):
        view_angles = self.pm.read_int(self.engine + self.DW_CLIENT_STATE)
        self.pm.write_float(view_angles + self.DW_CLIENT_STATE_VIEW_ANGLES, pitch)