from django.contrib import admin
from django.contrib.auth.models import User

from .models import Match,Profile,Match_book,Tickets
admin.site.register(Match)
admin.site.register(Profile)
admin.site.register(Match_book)
admin.site.register(Tickets)


# Register your models here.
