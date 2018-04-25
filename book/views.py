from django.shortcuts import render,redirect
from .models import Match
from datetime import datetime as dt
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


def home(request):
	return render(request, 'book/home.html',)

def match(request):
	    try:
	    	matchlist = Match.objects.filter(match_date__gt=dt.now()).order_by('match_date')    
	    except:
	        matchlist = []
	    return render(request, 'book/match.html', {'matchlist': matchlist})

def signup(request):
	 print("hi",request.method)
	 if request.method == 'POST':
	 	form = SignUpForm(request.POST)
	 	print("IN1")
	 	if form.is_valid():
	 		user = form.save()
	 		user.refresh_from_db()  # load the profile instance created by the signal
	 		user.profile.last_name = form.cleaned_data.get('last_name')
	 		user.profile.first_name = form.cleaned_data.get('first_name')
	 		user.profile.email = form.cleaned_data.get('email')
	 		print("hi2")
	 		user.save()
	 		raw_password = form.cleaned_data.get('password1')
	 		user = authenticate(username=user.username, password=raw_password)
	 		login(request, user)
	 		return redirect('http://127.0.0.1:8000/home')
	 else:
	 	form = SignUpForm()
	 return render(request, 'book/signup.html', {'form': form})
