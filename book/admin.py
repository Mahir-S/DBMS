from django.contrib import admin
from django.contrib.auth.models import User

from .models import Match,Profile
admin.site.register(Match)
admin.site.register(Profile)



# Register your models here.
