# mahjong_db/models.py
from django.db import models

class MahjongRecord(models.Model):
    date = models.DateField()
    player = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.player} - {self.amount}"
