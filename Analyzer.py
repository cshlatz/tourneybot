from Player import Player 
from Tournament import Tournament
from tabulate import tabulate

import json
import sys
import urllib.request

API_KEY = "81679e956c958d83340bec3335c0a2a7"

def get_tournament_by_id(tournament_id):
    print("sending request for tournament_id: " + str(tournament_id))
    contents = urllib.request.urlopen("https://api.ifpapinball.com/v1/tournament/" + str(tournament_id) + "/results?api_key=" + API_KEY)
    print("received tournament")
    return contents;

def generate_player():
    player = Player(id, name, player_rating)

t1 = get_tournament_by_id(sys.argv[1]) # IFPA Vermont State Pinball Championship 2018
t1_json = t1.read().decode('utf-8')
t1_json_object = json.loads(t1_json)

tournament = Tournament(t1_json_object["tournament"]["tournament_id"], t1_json_object["tournament"]["tournament_name"], t1_json_object["tournament"]["event_name"])
print("tournament object generated")

for i in t1_json_object["tournament"]["results"]:
    if i["ratings_value"] == "Not Rated":
        ratings_value = 1500
    else:
        ratings_value = float(i["ratings_value"])

    player = Player(i["player_id"], i["first_name"] + " " + i["last_name"], ratings_value, int(i["position"]))
    tournament.add_player(player)

print("")
print(tournament.tournament_name)
print("Number of players: " + str(len(tournament.players)))
print("--------------------")
tournament.sort_players_by_rating()
plus_minus = 0
counter = 1
data = []

for player in tournament.players:
    player_row = [player.player_name, player.player_rating, counter, player.position, counter - player.position]
    data.append(player_row)
    plus_minus = counter - player.position
    counter += 1

print(tabulate(data, headers=["Player", "Player Rating (GLICKO)", "Expected Position", "Actual Position", "+/-"]))
print("")
print("plus minus of tournament: " + str(plus_minus) + " = " + str(plus_minus / len(tournament.players)))
