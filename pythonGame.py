import random
import sys
import time
import classes as cl
import function
warrior = cl.Player("Fatbonks", 13.0, 5.0, {'min_damage': 1.0, 'max_damage': 5.0}, 24, 1, 0, 1, 25, "warrior")
mage = cl.Player("Fatbonks", 5.0, 10.0, {'min_damage': 1.0, 'max_damage': 2.0}, 0, 2, 0, 1, 25, "mage")
archer = cl.Player("Fatbonks", 8.0, 5.0, {'min_damage': 2.0, 'max_damage': 3.0}, 0, 4, 0, 1, 25, "archer")
thief = cl.Player("Fatbonks", 10.0, 5.0, {'min_damage': 1.0, 'max_damage': 1.0}, 0, 3, 25, 1, 25, "thief")
troll = cl.Enemy("Troll", 15.0, {'min_damage': 1.0, 'max_damage': 5.0}, 10, 1, 0, 0)
wolf = cl.Enemy("Wolf", 5.0, {'min_damage': 1.0, 'max_damage': 2.0}, 5, 2, 10, 0)
zombie = cl.Enemy("Zombie", 2.0, {'min_damage': 1.0, 'max_damage': 1.0}, 1, 1, 0, 0)
skeleton = cl.Enemy("Skeleton", 4.0, {'min_damage': 1.0, 'max_damage': 4.0}, 10, 1, 0, 0)

# name, health, mana, damage, exp, speed, dodge, level, level_next, class_type
