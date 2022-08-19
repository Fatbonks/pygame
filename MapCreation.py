import Pipe as game
import random as ran


def display_map(game_map, biome, x, y):
    print('-------------')
    print('|', game_map[y - 1][x - 1], '|', game_map[y - 1][x], '|', game_map[y - 1][x + 1], '|')
    print('|', game_map[y][x - 1], '|', game_map[y][x], '|', game_map[y][x + 1], '|')
    print('|', game_map[y + 1][x - 1], '|', game_map[y + 1][x], '|', game_map[y + 1][x + 1], '|')
    print('-------------')
    print('Map: {}'.format(game.gameData.map))
    print('L: ' + biome[game_map[y][x]]['biome'])
    print('description: ' + biome[game_map[y][x]]['description'])
    if game.gameData.dungeon_enemies > 0:
        print('Kill {} enemies to leave the Dungeon'.format(game.gameData.dungeon_enemies))


def create_map(game_map, biome, x, y):
    x_len = len(game_map) - 1
    y_len = len(game_map[0]) - 1
    while True:
        game.clear()
        display_map(game_map, biome, x, y)
        print('----------')
        print('Movement')
        print('----------')
        if biome[game_map[y - 1][x]]['is_wall'] is False and y > 0:
            print('1 - up')
        if biome[game_map[y + 1][x]]['is_wall'] is False and y < y_len:
            print('2 - down')
        if biome[game_map[y][x - 1]]['is_wall'] is False and x > 0:
            print('3 - left')
        if biome[game_map[y][x + 1]]['is_wall'] is False and x < x_len:
            print('4 - right')
        if biome[game_map[y][x]]['Intractable'] is True:
            print('5 - interact')
        print('----------')
        print("6 - Shows your stats\n7 - To leave the game")

        try:
            ans = int(input('> '))

            if ans <= 0:
                print('please use numbers between 1 - 9')
            if ans >= 9:
                print('please use numbers between 1 - 9')

            elif ans == 1:
                if biome[game_map[y - 1][x]]['is_wall'] is False and y > 0:
                    if game_map[y - 1][x] != '@':
                        y -= 1
                    else:
                        print('There is a wall blocking you. Perhaps you can break it.....')
                        print('would you like to break the wall?\n1: Yes\n2: No')
                        break_wall = int(input('> '))
                        if break_wall == 1:
                            game_map[y - 1][x] = 'H'
                        else:
                            pass
            elif ans == 2:
                if biome[game_map[y + 1][x]]['is_wall'] is False and y < y_len:
                    if game_map[y + 1][x] != '@':
                        y += 1
                    else:
                        print('There is a wall blocking you. Perhaps you can break it.....')
                        print('would you like to break the wall?\n1: Yes\n2: No')
                        break_wall = int(input('> '))
                        if break_wall == 1:
                            game_map[y + 1][x] = 'H'
                        else:
                            pass
            elif ans == 3:
                if biome[game_map[y][x - 1]]['is_wall'] is False and x > 0:
                    if game_map[y][x - 1] != '@':
                        x -= 1
                    else:
                        print('There is a wall blocking you. Perhaps you can break it.....')
                        print('would you like to break the wall?\n1: Yes\n2: No')
                        break_wall = int(input('> '))
                        if break_wall == 1:
                            game_map[y][x - 1] = 'H'
                        else:
                            pass
            elif ans == 4:
                if biome[game_map[y][x + 1]]['is_wall'] is False and x < x_len:
                    if game_map[y][x + 1] != '@':
                        x += 1
                    else:
                        print('There is a wall blocking you. Perhaps you can break it.....')
                        print('would you like to break the wall?\n1: Yes\n2: No')
                        break_wall = int(input('> '))
                        if break_wall == 1:
                            game_map[y][x + 1] = 'H'
                        else:
                            pass
            elif ans == 6:
                while True:
                    game.clear()
                    print('1 - Display Stats\n2 - Display Spell\n3 - Display Skills\n4 - back')
                    try:
                        ans_2 = int(input('> '))
                        if ans_2 == 4:
                            game.clear()
                            break
                        if ans_2 <= 0:
                            print('please input a number between 1 - 3')
                        if ans_2 >= 4:
                            print('please input a number between 1 - 3')
                        if ans_2 == 1:
                            game.main.display_stats()
                        elif ans_2 == 2:
                            game.main.display_spell()
                            game.draw_line()
                            input('press enter to leave')
                            game.clear()
                        elif ans_2 == 3:
                            game.main.display_skills()
                            input('press enter to leave')
                    except ValueError:
                        print('please use a number')
            elif ans == 7:
                exit(0)
            event(game_map, biome, x, y, ans)
        except ValueError:
            print('use a number')
            input('press enter to leave')


def assign_biome(game_map):
    ran.seed()
    temp_list = ['#', '@', 'H']
    x_len = len(game_map)
    for i in range(x_len):
        x = len(game_map[i])
        for e in range(x):
            if game_map[i][e] == '*':
                a = ran.choice(temp_list)
                game_map[i][e] = a


def map_creation(map_size_y, map_size_x):
    game.gameData.dungeon_enemies = map_size_x + map_size_y
    game.gameData.dungeon_enemies = int(game.gameData.dungeon_enemies // 2)
    a = []
    asd = []
    bruh = ['@', 'H', '*']
    burh = ['M', 'E', 'D']
    has_hallway = False
    ran.seed()
    for map_sec_y in range(map_size_y):
        asd.insert(0, [])
    for i in range(len(asd)):
        for map_sec_x in range(map_size_x):
            asd[i].insert(0, '#')
    x = map_size_x - 1
    for m in range(len(asd) - 1):
        a.insert(0, asd[m][1: x])

    for l in range(len(a)):
        x_len = len(a[l])
        for f in range(x_len):
            if ran.random() < 0.2:
                a[l][f] = '?'
            else:
                if ran.random() < 0.2:
                    if ran.random() < 0.1:
                        a[l][f] = ran.choice(burh)
                    else:
                        a[l][f] = '#'
                else:
                    a[l][f] = ran.choice(bruh)
    assign_biome(a)
    for l in range(len(a)):
        x_len = len(a[l])

        for f in range(x_len):
            if a[l][f] == '?':
                try:
                    if a[l][f + 1] == 'H' or a[l + 1][f] == 'H' or a[l - 1][f] == 'H' or a[l][f - 1] == 'H':
                        has_hallway = True
                    else:
                        has_hallway = False
                except IndexError:
                    pass
                if has_hallway is not True:
                    while True:
                        ran.seed()
                        val = ran.randint(1, 4)
                        if val == 1:
                            try:
                                a[l][f + 1] = 'H'
                                has_hallway = False
                                break
                            except IndexError:
                                pass
                        elif val == 2:
                            try:
                                a[l + 1][f] = 'H'
                                has_hallway = False
                                break
                            except IndexError:
                                pass
                        elif val == 3:
                            try:
                                a[l][f - 1] = 'H'
                                has_hallway = False
                                break
                            except IndexError:
                                pass
                        elif val == 4:
                            try:
                                a[l - 1][f] = 'H'
                                has_hallway = False
                                break
                            except IndexError:
                                pass

    a[0][0] = '█'
    a[1][0] = 'H'
    a[0][1] = 'H'
    xlen = len(a)
    list_len = len(a[0])
    for bruhash in range(xlen):
        a[bruhash].insert(list_len, '#')
        a[bruhash].insert(0, '#')
    a.insert(0, asd[0])
    a[map_size_y - 1] = asd[0]
    game.gameData.dungeon_map = a


def event(game_map, biome, x, y, ans):
    if biome[game_map[y][x]]['enemy_can_spawn'] is True:
        if biome[game_map[y][x]]['biome'] == 'Forest':
            if ran.random() < 0.7:
                game.combatLogic.combat_display()
        elif biome[game_map[y][x]]['biome'] == 'Pathway':
            if ran.random() < 0.3:
                game.combatLogic.combat_display()
        else:
            if game.gameData.dungeon_enemies != 0:
                if ran.random() < 0.5:
                    game.gameData.dungeon_enemies -= 1
                    game.combatLogic.combat_display()

    if ans == 5 and biome[game_map[y][x]]['Intractable'] is True:
        if biome[game_map[y][x]]['biome'] == 'Unexplored Room':
            for i in biome:
                if biome[i]['can_explore'] is True:
                    game.gameData.room.insert(0, i)
            room = game.ran.choice(game.gameData.room)
            game_map[y][x] = room
            game.gameData.room.clear()
            create_map(game_map, biome, x, y)
        if biome[game_map[y][x]]['biome'] == 'Starting room':
            if game.gameData.dungeon_enemies == 0:
                print('Good job you have killed all the enemies')
                print('You are now being transported back')
                input('press enter')
                game.gameData.map = 'World Map'
                create_map(game.gameData.world_map, game.gameData.biome, game.gameData.player_x_world,
                           game.gameData.player_y_world)
            else:
                print('please kill all the enemies in the dungeon')
                input('press enter')
        elif biome[game_map[y][x]]['biome'] == 'Village':
            while True:
                print('1 - Shop\n2 - Church\n3 - Inn( Save Game )\n4 - back')
                try:
                    ans_2 = int(input('>'))
                    if ans_2 == 1:
                        while True:
                            ans_3 = int(input('1 - Buy drugs( $10 )\n2 - back\n>'))
                            if ans_3 == 1:
                                if game.gameData.player['bag']['gold'] >= 10:
                                    game.gameData.player['bag']['Drugs'] += 1
                                    game.gameData.player['bag']['gold'] -= 10
                                    input('you bought drugs!\npress enter')
                                else:
                                    print('you have no money')
                                    input('press enter')
                            if ans_3 == 2:
                                break
                    elif ans_2 == 2:
                        print('you are not a valid member of the Church of Ryan')
                        input('press enter')
                        game.clear()
                    elif ans_2 == 3:
                        game.SavedGame.save_game()
                        game.draw_line()
                        print('the game is saving')
                        game.print_dialogue('....')
                        print('the game has saved')
                    elif ans_2 == 4:
                        break
                except ValueError:
                    print('Use a number')
        elif biome[game_map[y][x]]['biome'] == 'Dungeon Selector':
            print('1 - small dungeon\n2 - medium dungeon\n3 - large dungeon\n4 - Back')
            try:
                ans_2 = int(input('>'))
                if ans_2 == 1:
                    game.gameData.map = 'Dungeon'
                    map_creation(5, 5)
                    game.gameData.player_x_dungeon = 1
                    game.gameData.player_y_dungeon = 1
                    create_map(game.gameData.dungeon_map, game.gameData.biome, game.gameData.player_x_dungeon,
                               game.gameData.player_y_dungeon)
                elif ans_2 == 2:
                    game.gameData.map = 'Dungeon'
                    game.gameData.player_x_dungeon = 1
                    game.gameData.player_y_dungeon = 1
                    map_creation(10, 10)
                    create_map(game.gameData.dungeon_map, game.gameData.biome, game.gameData.player_x_dungeon,
                               game.gameData.player_y_dungeon)
                elif ans_2 == 3:
                    game.gameData.map = 'Dungeon'
                    game.gameData.player_x_dungeon = 1
                    game.gameData.player_y_dungeon = 1
                    map_creation(15, 15)
                    create_map(game.gameData.dungeon_map, game.gameData.biome, game.gameData.player_x_dungeon,
                               game.gameData.player_y_dungeon)
                elif ans_2 == 4:
                    pass
            except ValueError:
                pass
        elif biome[game_map[y][x]]['biome'] == 'Merchant':
            while True:
                print('1 - Shop\n2 - back')
                try:
                    ans_2 = int(input('>'))
                    if ans_2 == 1:
                        while True:
                            ans_3 = int(input('1 - Buy drugs( $20 )\n2 - back\n>'))
                            if ans_3 == 1:
                                if game.gameData.player['bag']['gold'] >= 20:
                                    game.gameData.player['bag']['Drugs'] += 1
                                    game.gameData.player['bag']['gold'] -= 20
                                    input('you bought drugs!\npress enter')
                                else:
                                    print('you have no money')
                                    input('press enter')
                            elif ans_3 == 2:
                                break
                    elif ans_2 == 2:
                        break
                except ValueError:
                    print('Use a number')

        elif biome[game_map[y][x]]['biome'] == 'Dead adventurer':
            if ran.random() < 0.2:
                print('you looted the dead adventurer and you gain 10 SMECKLES')
                game.gameData.player['bag']['gold'] += 10
                game_map[y][x] = 'E'
                input('press enter')
            else:
                print('The dead adventurer was hiding a enemy!')
                game.time.sleep(2)
                game.combatLogic.combat_display()
        elif biome[game_map[y][x]]['biome'] == 'Treasure Room':
            if ran.random() < 0.8:
                print('you looted the treasure chest and you founded 40 SMECKLES')
                game.gameData.player['bag']['gold'] += 40
                game_map[y][x] = 'E'
                input('press enter')
            else:
                print('The treasure room contained nothing!')


if __name__ == '__main__':
    exit('Please run main.py')
