import json
from pynput import keyboard
from clouds import Clouds
from map import Map
import time
import os
from helicopter import Helicopter

TICK_SLEEP = 0.105
TREE_UPDATE = 10
FIRE_UPDATE = 100
CLOUDS_UPDATE = 30
MAP_W, MAP_H = 16, 8

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helicopter = Helicopter(MAP_W, MAP_H)

MOVES = {'a': (-1, 0), 's': (0, 1), 'd': (1, 0), 'w': (0, -1)}


# f - export, g - import
def process_key_release(key):
    global helicopter,tick,clouds,field
    c = key.char.lower()
    if c in MOVES.keys():
        helicopter.move(MOVES[c][0], MOVES[c][1])
    elif c == 'f':
        data = {"h": helicopter.export_data(), "f": field.export_data(), "c": clouds.export_data(), "t": tick}
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    elif c == 'g':
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            helicopter.import_data(data["h"])
            field.import_data(data["f"])
            clouds.import_data(data["c"])
            tick = data["t"]



listener = keyboard.Listener(on_release=process_key_release)
listener.start()

tick = 1

while True:
    os.system('clear')

    field.process_helicopter(helicopter, clouds)
    helicopter.print_stats()
    field.print_map(helicopter, clouds)

    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRE_UPDATE == 0:
        field.update_fires()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()
    print("TICK", tick)
    print("")
