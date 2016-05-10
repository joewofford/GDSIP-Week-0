from datetime import datetime
import os
import sys


def read_game_info(filename):
    '''
    INPUT: string
    OUTPUT: tuple of string, string, string, int, int

    Given the filename of a game, return the time, team names and score for the
    game. Return these values:

        time: string representing time of game
        team1: first team name
        team2: second team name
        score1: score of first team
        score2: score of second team
    '''
    ind = 0
    with open(filename) as f:
        for line in f:
            line = line.strip('\n')

            if ind == 0:
                time = line
                #time = line[3:6] + ' ' + line[0:2]

            if ind == 3:
                hyphen = line.index('-')
                team1 = line[:(hyphen-1)]
                team2 = line[(hyphen+2):]

            if ind == 4:
                hyphen = line.index('-')
                score1 = int(line[0:hyphen])
                score2 = int(line[(hyphen+1):])

            ind += 1

    return (time, team1, team2, score1, score2)


def display_game(time, team, other, team_score, other_score):
    '''
    INPUT: string, string, string, int, int
    OUTPUT: string

    Given the time, names of the teams and score, return a one line string
    presentation of the results.
    '''
    return '{}: {} ({}) - {} ({})'.format(time, team, team_score, other, other_score)


def display_summary(team, data, detailed=False):
    '''
    INPUT: string, list of tuples, bool
    OUTPUT: string

    Given the data (list of tuples of game data), return a string containing
    the summary of results for the given team. This includes # games played,
    # wins, # losses, # ties, and # goals scored.

    If detailed is True, also include in the string all the games for the given
    team.
    '''

    wins = 0
    losses = 0
    ties = 0
    total_goals = 0
    games = 0

    for game in data:
        if team == game[1]:
            games += 1
            total_goals += game[3]
            if game[3] > game[4]:
                wins += 1
            if game[3] < game[4]:
                losses += 1
            if game[3] == game[4]:
                ties += 1
        if team == game[2]:
            games += 1
            total_goals += game[4]
            if game[3] > game[4]:
                losses += 1
            if game[3] < game[4]:
                wins += 1
            if game[3] == game[4]:
                ties += 1

    return '{} played a total of {} games.\n{} win(s), {} loss(es), {} tie(s), {} total goal(s)'.format(team, games, wins, losses, ties, total_goals)



def run(directory, team):
    '''
    INPUT: string, string
    OUTPUT: None

    Given the directory where the data is stored and the team name of interest,
    read the data from the directory and display the summary of results for the
    given team.
    '''
    data = []
    for filename in os.listdir(directory):
        data.append(read_game_info(os.path.join(directory, filename)))
    print display_summary(team, data, detailed=True)


def main():
    '''
    INPUT: None
    OUTPUT: None

    Get the directory name and team name from the arguments given. If arguments
    are valid, display the summary of results. Otherwise, exit the program.
    '''
    error_message = "Usage: python worldcup.py directory team\n" \
                    "       e.g. python worldcup.py worldcup USA"
    if len(sys.argv) != 3:
        print error_message
        exit()
    directory = sys.argv[1]
    if not os.path.exists(directory):
        print "{0} is not a valid directory.".format(directory)
        print error_message
        exit()
    team = sys.argv[2]
    run(directory, team)


if __name__ == '__main__':
    main()
