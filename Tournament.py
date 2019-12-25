from Player import Player

class Tournament:
    def __init__(self, tournament_id, tournament_name, event_name):
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
        self.event_name = event_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)
    
    def sort_players_by_rating(self):
        self.players = sorted(self.players, key=lambda x: x.player_rating)
        self.players.reverse()
