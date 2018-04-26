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
	match_no=models.IntegerField(primary_key=True)
	image1=models.ImageField(default='/images/srh.png',unique=False)
	image2=models.ImageField(default='/images/srh.png',unique=False)
	def __str__(self):
		return self.team1+" VS "+self.team2

	class Meta:
		ordering = ('match_date',)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70,blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name=models.CharField(max_length=30,blank=True)

    def __str__(self):
    	return first_name

class Match_book(models.Model):
	match=models.ForeignKey(Match,on_delete=models.CASCADE)
	stand=models.CharField(max_length=30)
	tier1_price=models.IntegerField(default=1000)
	tier2_price=models.IntegerField(default=1000)
	tier1_availability=models.IntegerField(default=500)
	tier2_availability=models.IntegerField(default=500)

	
	class Meta:
		unique_together=(('match', 'stand'),)

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Tickets(models.Model):
	match=models.ForeignKey(Match,on_delete=models.CASCADE)
	stand=models.CharField(max_length=30)
	tier_no=models.IntegerField(unique=False)
	user=models.ForeignKey(User,unique=False,on_delete=models.SET(get_sentinel_user))
	number=models.IntegerField()

	class Meta:
		unique_together=(('match','user','stand','tier_no'),)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()