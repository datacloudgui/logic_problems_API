#This file contain the logic to solve the Ping Pong Game problem
#
#

def find_second_loser(player1, player2, player3):
    """
    Wrap the process to find the second loser

            Parameters:
                    player1 (int): Score of the first player
                    player2 (int): Score of the second player
                    player3 (int): Score of the third player

            Returns:
                    loser_name (str): The name of the second loser
                    lost_games (list): List with the number of lost games
    """

    #Validate the scores received
    validation_error, message, loser_score, num_games = validate_data(player1, player2, player3)

    if not validation_error:
        return "Second loser can't be founded: " + message, []
    else:
        return second_loser([player1, player2, player3], loser_score, num_games)

def validate_data(player1, player2, player3):
    """
    Validate if the player's scores are valid according to the rules

            Parameters:
                    (int) player1 score first player
                    (int) player2 score second player
                    (int) player3 score third player

            Returns:
                    (bool) validation result
                    (string) error message
    """

    num_plays = player1 + player2 + player3
    num_games = num_plays / 2
    loser_score = min(player1, player2, player3)

    # Validate if the scores sum is even, else is impossible.
    if num_plays % 2 != 0:
        return False, "The scores are not possible according to the rules", loser_score, num_games

    if num_games % 2 == 0:
        return False, "The second loser only can be calculated if the total games is odd", loser_score, num_games

    # A player must participate at least num_games//2 according to the rules.
    if loser_score < num_games//2:
        return False, "Loser games are not possible according to the rules", loser_score, num_games

    # If the loser participate more than num_games//2 the second game loser can be any player.
    if loser_score > num_games//2:
        return False, "Too many options to the second game loser", loser_score, num_games

    return True, "", loser_score, num_games

def second_loser(scores, loser_score, num_games):
    """
    Return

            Parameters:
                    scores (list) a list with the scores ordered by player
                    loser_score (int) score of the loser player
                    num_games (float) Number of games obtained

            Returns:
                    second_loser_name (bool) name of the second loser
                    second_loser_list (list) list of the lost games of the loser
    """
    names = ["Ana", "Jose", "Juan"]

    second_loser_name = names[scores.index(loser_score)]
    second_loser_list = [i for i in range(1,int(num_games)) if i % 2 == 0]

    return second_loser_name, second_loser_list, loser_score