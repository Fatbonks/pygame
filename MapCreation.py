import Pipe as game


def display_map(game_map, biome, x, y):
    print('-------------')
    print('|', game_map[y - 1][x - 1], '|', game_map[y - 1][x], '|', game_map[y - 1][x + 1], '|')
    print('|', game_map[y][x - 1], '|', game_map[y][x], '|', game_map[y][x + 1], '|')
    print('|', game_map[y + 1][x - 1], '|', game_map[y + 1][x], '|', game_map[y + 1][x + 1], '|')
    print('-------------')
    print('L: ' + biome[game_map[y][x]]['biome'])
    print('cords', + y, x)
    print('description: ' + biome[game_map[y][x]]['description'])


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
        if biome[game_map[y][x]]['biome'] == 'Unexplored Room':
            print('5 - interact')
        print('----------')
        print("6 - Shows your stats\n7 - To leave the game\n8 - save")

        try:
            ans = int(input('> '))
            if ans <= 0:
                print('please use numbers between 1 - 9')
            if ans >= 9:
                print('please use numbers between 1 - 9')

            if ans == 5:
                if biome[game_map[y][x]]['biome'] == 'Unexplored Room':
                    for i in biome:
                        if biome[i]['can_explore'] is True:
                            game.gameData.room.insert(0, i)
                    room = game.ran.choice(game.gameData.room)
                    game_map[y][x] = room
                    create_map(game_map, biome, x, y)
                    break
                else:
                    pass
            elif ans == 1:
                if biome[game_map[y - 1][x]]['is_wall'] is False and y > 0:
                    y -= 1
            elif ans == 2:
                if biome[game_map[y + 1][x]]['is_wall'] is False and y < y_len:
                    y += 1
            elif ans == 3:
                if biome[game_map[y][x - 1]]['is_wall'] is False and x > 0:
                    x -= 1
            elif ans == 4:
                if biome[game_map[y][x + 1]]['is_wall'] is False and x < x_len:
                    x += 1
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
            elif ans == 8:
                game.SavedGame.save_game()
                game.draw_line()
                print('the game is saving')
                game.print_dialogue('....')
                print('the game has saved')
        except ValueError:
            print('use a number')
            input('press enter to leave')


def dont_look_at_this_function_pls():
    pl = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
    x_len = len(game.gameData.dungeon_map) - 1
    y_len = len(game.gameData.dungeon_map[0]) - 1
    for i in range(11):
        a = game.gameData.dungeon_map[i + 1][1:17]
        a.insert(0, '#')
        a.insert(17, '#')
        pl.insert(1, a)
    print(pl)
    x_pl = len(pl[2])
    print(x_pl)




