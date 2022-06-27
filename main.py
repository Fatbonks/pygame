import Pipe as game


def event_picker():
    if game.ran.random() < 1:
        game.combatLogic.in_combat()


if __name__ == '__main__':
    game = GameLogic()

    # Runs at the start of the game
    game.playerCreation.player_class()
    # Main game loop
    while True:
        option = ['up', 'left', 'right', 'stats', 'exit']
        print('----------------------------')
        print("Up: Move up\nStats: Shows your stats\nExit: To leave the game")
        answer = input("> ").lower().strip()
        if answer in option:
            # up is debug command to trigger combat
            if answer == 'up':
                # 100% chance to get into a fight
                game.event_picker()
                game.player['stats']['mana'] = old_mana

            elif answer == 'stats':
                print("----------------------------")
                print(
                    "Level: {}\nMax health: {}\nHealth: {}\nMana: {}\nDamage: {} Min damage {} Max damage\nEXP: {}\n"
                    "Speed: {}\nDodge: {}\nLevel next: {}\n".format(
                        game.player['level']['level'],
                        game.player['stats']['max_health'],
                        game.player['stats']['health'],
                        game.player['stats']['mana'],
                        game.player['stats']['damage']['min_damage'],
                        game.player['stats']['damage']['max_damage'],
                        game.player['level']['exp'],
                        game.player['stats']['speed'],
                        game.player['stats']['dodge'],
                        game.player['level']['level_next']
                    ))
            elif answer == 'exit':
                exit(0)
        else:
            print('please use an word to select your choices')
