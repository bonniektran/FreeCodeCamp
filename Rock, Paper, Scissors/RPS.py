# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# def player(prev_play, opponent_history=[]):
#     opponent_history.append(prev_play)

#     guess = "R"
#     if len(opponent_history) > 2:
#         guess = opponent_history[-2]

#     return guess

def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'S' # default move

    opponent_history.append(prev_play)
    prediction = 'R' # predicted opponent move

    if len(opponent_history) >= 5:
        last_five = "".join(opponent_history[-5:]) # look back at last  moves if opponent history is at least 5 moves
        play_order[last_five] = play_order.get(last_five, 0) + 1 # empty dictionary filled with last 5 moves
        
        potential_plays = [
            "".join([*opponent_history[-4:], v]) # all combinations of plays based on last 4 moves
            for v in ['R', 'P', 'S']
        ]

        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order # check if empty
        }

        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:] # make predictions based on recorded moves

        if prediction[-1] == "P": # counter moves accordingly
            prev_play = "S"
        if prediction[-1] == "R":
            prev_play = "P"
        if prediction[-1] == "S":
            prev_play = "R"

    return prev_play
