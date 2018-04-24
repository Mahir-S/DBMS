from django.shortcuts import render
from .models import Match
from datetime import datetime as dt

def home(request):
	return render(request, 'book/home.html',)

def match(request):
	    try:
	    	matchlist = Match.objects.filter(match_date__gt=dt.now()).order_by('match_date')    
	    except:
	        matchlist = []
	    return render(request, 'book/match.html', {'matchlist': matchlist})