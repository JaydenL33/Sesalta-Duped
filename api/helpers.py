import firebase_routes


def retrieve_all_users_with_games_and_scores():
    all_users_data = firebase_routes.get_all_users()
    users_names = list(all_users_data.keys())
    all_users_with_games_and_scores = {}
    for users_name in users_names:
        all_users_with_games_and_scores[users_name] = extract_games_and_score_for_user(
            users_name)

    return all_users_with_games_and_scores


def extract_games_and_score_for_user(name):
    user_data = firebase_routes.get_user_by_id(name)
    game_count = user_data['gameIDs']['gameCount']

    if game_count == 0:
        return {}
    else:
        games_played = user_data['gameIDs']['gamesPlayed']
        game_number_and_score = {}

        for game_name, game_id in games_played.items():
            game_data = firebase_routes.get_game_data_by_id(game_id)
            game_number_and_score[game_name] = calculate_mode_score_and_date(
                game_data)

        return game_number_and_score


def calculate_mode_score_and_date(game_data):
    data = {}
    data["Mode"] = mode_string_to_id(game_data['mode'])
    data["Date"] = game_data['questions'][0]['time_asked']
    data["Score"] = 0
    for question in game_data['questions']:
        data["Score"] += question['points']
    return data


def filter_games_by_mode(all_users_with_games_and_scores, mode):
    name_list = list(all_users_with_games_and_scores.keys())
    filtered_games_and_scores_by_mode = {}
    for name in name_list:
        game_names = list(all_users_with_games_and_scores[name].keys())
        for game_name in game_names:
            if all_users_with_games_and_scores[name][game_name]["Mode"] == mode:
                if name not in filtered_games_and_scores_by_mode:
                    filtered_games_and_scores_by_mode[name] = {}
                if game_name not in filtered_games_and_scores_by_mode[name]:
                    filtered_games_and_scores_by_mode[name][game_name] = {}
                filtered_games_and_scores_by_mode[name][game_name] = all_users_with_games_and_scores[name][game_name]
    return filtered_games_and_scores_by_mode


def mode_string_to_id(mode_string):
    mode_map = {'Country->Map': 0, 'Map->Country': 1,
                'Capital->Country': 2, 'Country->Capital': 3, 'Flag->Country': 4}
    return mode_map[mode_string]


def update_user_data(user_name, new_game_id):
    if "not_a_user" == user_name:
        return
    user_data = firebase_routes.get_user_by_id(user_name)
    total_games_played = user_data["gameIDs"]["gameCount"] + 1
    game_number_string = "game" + str(total_games_played)
    user_data["gameIDs"]["gameCount"] = total_games_played
    if "gamesPlayed" not in user_data["gameIDs"]:
        user_data["gameIDs"]["gamesPlayed"] = {}
    user_data["gameIDs"]["gamesPlayed"][game_number_string] = new_game_id

    firebase_routes.update_user(user_name, user_data)


def rival_finder(sorted_list, this_user_name, index, this_game_score, return_string):
    print(index)
    if sorted_list[index]["name"] == this_user_name:
        if index == 0:
            return_string = "You are still the global leader!"
        else:
            return_string = rival_finder(
                sorted_list, this_user_name, index-1, this_game_score, return_string)
    else:
        return_string = "Your Rival is World Number " + \
            str(index+1) + " " + sorted_list[index]["name"] + ". Defeat them by getting " + str(
                sorted_list[index]["score"]-this_game_score) + " more points."

    return return_string
