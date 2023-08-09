from django.db import models


class Event(models.Model):
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="host_events")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="events_for_game")
    date = models.DateField(null=True, auto_now=False, auto_now_add=True)
    attendees = models.ManyToManyField("Gamer", through = "Gamer_Event", related_name= "events_attending")

