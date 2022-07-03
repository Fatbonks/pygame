import Pipe as game


def skill_slot_adder(skill, ans):
    if len(game.gameData.player_skills['physical_skills']) >= ans >= 1:
        if game.gameData.player_skills['physical_skills']['slot_{}'.format(ans)]['name'] == '':
            game.gameData.player_skills['physical_skills']['slot_{}'.format(ans)] = skill
