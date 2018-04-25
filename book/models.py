from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Match(models.Model):
	match_date=models.DateTimeField('MATCH DATE')
	team1=models.CharField(max_length=30)
	team2=models.CharField(max_length=30)
	day=models.CharField(max_length=20,)
	match_no=models.IntegerField()
	image1=models.ImageField(default='/images/srh.png',unique=False)
	image2=models.ImageField(default='/images/srh.png',unique=False)
	def __str__(self):
		return self.team1+" VS "+self.team2

	class Meta:
		ordering = ('match_date',)
"""
class Match(models.Model):
	match_date=models.DateTimeField('MATCH DATE')
	team1=models.CharField(max_length=30)
	team2=models.CharField(max_length=30)

	def __str__(self):
		return self.team1+" VS "+self.team2

	class Meta:
		ordering = ('match_date',)
"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70,blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name=models.CharField(max_length=30,blank=True)

    

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()