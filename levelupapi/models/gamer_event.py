from django.db import models

class Gamer_Event(models.Model):
    type = models.CharField(max_length=55)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)