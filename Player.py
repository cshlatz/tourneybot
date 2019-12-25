class Player:
    def __init__(self, player_id, player_name, player_rating, position):
        self.player_name = player_name
        self.player_id = player_id
        self.player_rating = player_rating
        self.position = position;
    
    def print_player(self):
        print("Player " + str(self.player_id) + ": " + self.player_name + " - " + str(self.player_rating))
