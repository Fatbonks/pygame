import random
player_health = 10
player_damage = 1
enemy = 10
chest = 1
events = [enemy, chest]
is_event_happen = 0


def create_event():
    choice = random.choice(events)
    if choice == enemy:
        print("oh no an enemy")
    if choice == chest:
        print("chest!")

print("welcome to my game")

help = "how to play: up,down,left,right to move your character.\ninput 'player' to see your stats\nand 'help' will give you list of commands you can text"
print(help)

game_is_running =True

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
        
  
