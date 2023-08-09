from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=55)
    creator = models.ForeignKey("Gamer", on_delete=models.DO_NOTHING, related_name = "created_games")
    game_type = models.ForeignKey("GameType", on_delete=models.DO_NOTHING, related_name = "games")
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    maker = models.CharField(max_length=55)

   