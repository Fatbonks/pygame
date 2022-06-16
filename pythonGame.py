import random
player_health = 10
player_damage = 1
is_event_happen = 0
enemy_health = 10
enemy_damage = 1

print("welcome to my game")


def create_event():
    random.seed()
    choice = random.randint(1, 2)
    if choice == 2:
        print("An enemy!")
        enemy()
    if choice == 1:
        print("chest!")

def enemy():
    while enemy_health > 0 or player_health > 0:
        print(enemy_health = 10)
        print( enemy_damage = 1)
        attack_first = random.randint(0, 1)



help = "how to play: up,down,left,right to move your character.\ninput 'player' to see your stats\nand 'help' will give you list of commands you can text"
print(help)

game_is_running = True

while game_is_running:
    player = input("Input here: ").lower().strip()
    if player == "player":
        print("{} health, {} damage".format(player_health, player_damage))
    if player == "up":
        random.seed()
        is_event_happen = random.randint(0, 1)
        if is_event_happen == 1:
            create_event()
    if player == "help":
        print(help)

  
