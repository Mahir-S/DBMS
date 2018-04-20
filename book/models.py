from django.db import models

# Create your models here.
class Match(models.Model):
	match_date=models.DateTimeField('MATCH DATE')
	team1=models.CharField(max_length=30)
	team2=models.CharField(max_length=30)

	def __str__(self):
		return team1+" VS "+team2