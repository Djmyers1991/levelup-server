from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=55)
    creator = models.ForeignKey("Gamer", on_delete=models.DO_NOTHING, related_name = "created_games")
    game_type = models.ForeignKey("Game_Type", on_delete=models.DO_NOTHING, related_name = "games")
   