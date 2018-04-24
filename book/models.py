from django.db import models

# Create your models here.
class Match(models.Model):
	match_date=models.DateTimeField('MATCH DATE')
	team1=models.CharField(max_length=30)
	team2=models.CharField(max_length=30)

	def __str__(self):
		return self.team1+" VS "+self.team2

	class Meta:
		ordering = ('match_date',)