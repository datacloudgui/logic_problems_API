from django.db import models

class Players(models.Model):
    """
    Represent a player with the name as index
    """

    name            = models.CharField(max_length=50, blank=False, db_index=True)

class Second_losers(models.Model):
    """
    Represent a second loser founded
    """

    name                         = models.ForeignKey('Players', on_delete=models.PROTECT)
    date_data                    = models.DateField(blank=False, db_index=True)
    score                        = models.IntegerField(blank=False)