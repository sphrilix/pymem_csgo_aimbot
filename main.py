import keyboard
from memory_handler import MemoryHandler
from angle_calc import AngleCalc
from local_player import LocalPlayer


def main():
    mh = MemoryHandler()
    while 1:
        player = LocalPlayer(mh.get_local_player_coords(), mh.get_local_player_team_id(),
                             mh.get_local_player_view_angles())
        enemy = mh.get_closest_alive_enemy()
        if keyboard.is_pressed("n") and enemy is not None:
            ac = AngleCalc(player, enemy)
            mh.write_yaw(ac.normalize_yaw(ac.calc_yaw_to_enemy()))
            mh.write_pitch(ac.normalize_pitch(ac.calc_pitch_to_enemy()))


if __name__ == "__main__":
    main()
