from django.shortcuts import render,redirect
from .models import Match,Match_book,Tickets,Team
from datetime import datetime as dt
from .forms import SignUpForm,Booking_form,Modify_form
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
	return render(request, 'book/home.html',)

def match(request):
	try:
		matchlist = Match.objects.filter(match_date__gt=dt.now()).order_by('match_date')
	except:
		matchlist = []
	return render(request, 'book/match2.html', {'matchlist': matchlist},{})
	
def createdictionary(id):
	a=['North','North-east','East','South-East','South','South-West','West','North-West']
	b=['North','North_east','East','South_East','South','South_West','West','North_West']
	descr={}
	mat=Match.objects.get(match_no=id)
	count=0
	for st in b:
		obj=Match_book.objects.get(match=mat,stand=a[count])
		descr[st+'_tier1_price']=obj.tier1_price
		descr[st+'_tier2_price']=obj.tier2_price
		descr[st+'_tier1_availability']=obj.tier1_availability
		descr[st+'_tier2_availability']=obj.tier2_availability
		count=count+1
	return descr

def signup(request):
	 if request.method == 'POST':
	 	form = SignUpForm(request.POST)
	 	if form.is_valid():
	 		user = form.save()
	 		user.refresh_from_db()  # load the profile instance created by the signal
	 		user.profile.last_name = form.cleaned_data.get('last_name')
	 		user.profile.first_name = form.cleaned_data.get('first_name')
	 		user.profile.email = form.cleaned_data.get('email')
	 		user.save()
	 		raw_password = form.cleaned_data.get('password1')
	 		user = authenticate(username=user.username, password=raw_password)
	 		login(request, user)
	 		return redirect('http://127.0.0.1:8000/home')
	 else:
	 	form = SignUpForm()
	 return render(request, 'book/signup.html', {'form': form})

@login_required
def book(request,id):
	#print(request.method)
	if request.method=='GET':
		form_north=Booking_form(prefix="form_north")
		form_north_east=Booking_form(prefix="form_north_east")
		form_south=Booking_form(prefix="form_south")
		form_south_east=Booking_form(prefix="form_south_east")
		form_south_west=Booking_form(prefix="form_south_west")
		form_north_west=Booking_form(prefix="form_north_west")
		form_east=Booking_form(prefix="form_east")
		form_west=Booking_form(prefix="form_west")
		#print(form_north)
		match=Match.objects.get(match_no=id)
		descr=createdictionary(id)
		return render(request,'book/22.html',{'descr':descr,'match':match,'form_north':form_north,'form_north_east':form_north_east,'form_south':form_south,'form_south_east':form_south_east,'form_north_west':form_north_west,'form_south_west':form_south_west,'form_east':form_east,'form_west':form_west})
	else:
		m=Match.objects.get(match_no=id)
		form_north=Booking_form(data=request.POST,prefix="form_north",dem1=Match_book.objects.get(match=m,stand='North').tier1_availability,dem2=Match_book.objects.get(match=m,stand='North').tier2_availability)
		form_north_east=Booking_form(request.POST,prefix="form_north_east",dem1=Match_book.objects.get(match=m,stand='North-east').tier1_availability,dem2=Match_book.objects.get(match=m,stand='North-east').tier2_availability)
		form_south=Booking_form(request.POST,prefix="form_south",dem1=Match_book.objects.get(match=m,stand='South').tier1_availability,dem2=Match_book.objects.get(match=m,stand='South').tier2_availability)
		form_south_east=Booking_form(request.POST,prefix="form_south_east",dem1=Match_book.objects.get(match=m,stand='South-East').tier1_availability,dem2=Match_book.objects.get(match=m,stand='South-East').tier2_availability)
		form_south_west=Booking_form(request.POST,prefix="form_south_west",dem1=Match_book.objects.get(match=m,stand='South-West').tier1_availability,dem2=Match_book.objects.get(match=m,stand='South-West').tier2_availability)
		form_north_west=Booking_form(request.POST,prefix="form_north_west",dem1=Match_book.objects.get(match=m,stand='North-West').tier1_availability,dem2=Match_book.objects.get(match=m,stand='North-West').tier2_availability)
		form_east=Booking_form(request.POST,prefix="form_east",dem1=Match_book.objects.get(match=m,stand='East').tier1_availability,dem2=Match_book.objects.get(match=m,stand='East').tier2_availability)
		form_west=Booking_form(request.POST,prefix="form_west",dem1=Match_book.objects.get(match=m,stand='West').tier1_availability,dem2=Match_book.objects.get(match=m,stand='West').tier2_availability)
		#print(request.POST)
		ch=1
		if form_north.is_valid():
			pass
		else :
			ch=0
		if form_south.is_valid():
			pass
		else :
			ch=0
		if form_east.is_valid():
			pass
		else :
			ch=0
		if form_west.is_valid():
			pass
		else :
			ch=0
		if form_south_west.is_valid():
			pass
		else :
			ch=0
		if form_south_east.is_valid():
			pass
		else :
			ch=0
		if form_north_west.is_valid():
			pass
		else :
			ch=0
		if form_north_east.is_valid():
			pass
		else :
			ch=0
		if ch==1:
			if form_north.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='North',user=request.user,tier_no=1)
					obj.number=obj.number+form_north.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North')
					ob.tier1_availability=ob.tier1_availability-form_north.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='North',tier_no=1,user=request.user,number=form_north.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North')
					ob.tier1_availability=ob.tier1_availability-form_north.cleaned_data.get('tier1_demand')
					ob.save()
			if form_north.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='North',user=request.user,tier_no=2)
					obj.number=obj.number+form_north.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North')
					ob.tier2_availability=ob.tier2_availability-form_north.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='North',tier_no=2,user=request.user,number=form_north.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North')
					ob.tier2_availability=ob.tier2_availability-form_north.cleaned_data.get('tier2_demand')
					ob.save()

			if form_south.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='South',user=request.user,tier_no=1)
					obj.number=obj.number+form_south.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South')
					ob.tier1_availability=ob.tier1_availability-form_south.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='South',tier_no=1,user=request.user,number=form_south.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South')
					ob.tier1_availability=ob.tier1_availability-form_south.cleaned_data.get('tier1_demand')
					ob.save()
			if form_south.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='South',user=request.user,tier_no=2)
					obj.number=obj.number+form_south.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South')
					ob.tier2_availability=ob.tier2_availability-form_south.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='South',tier_no=2,user=request.user,number=form_south.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South')
					ob.tier2_availability=ob.tier2_availability-form_south.cleaned_data.get('tier2_demand')
					ob.save()
			if form_east.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='East',user=request.user,tier_no=1)
					obj.number=obj.number+form_east.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier1_availability=ob.tier1_availability-form_east.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='East',tier_no=1,user=request.user,number=form_east.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier1_availability=ob.tier1_availability-form_east.cleaned_data.get('tier1_demand')
					ob.save()
			if form_east.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='East',user=request.user,tier_no=2)
					obj.number=obj.number+form_east.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier2_availability=ob.tier2_availability-form_east.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='East',tier_no=2,user=request.user,number=form_east.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='East')
					ob.tier2_availability=ob.tier2_availability-form_east.cleaned_data.get('tier2_demand')
					ob.save()
			if form_west.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='West',user=request.user,tier_no=1)
					obj.number=obj.number+form_west.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='West')
					ob.tier1_availability=ob.tier1_availability-form_west.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='West',tier_no=1,user=request.user,number=form_west.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='West')
					ob.tier1_availability=ob.tier1_availability-form_west.cleaned_data.get('tier1_demand')
					ob.save()
			if form_west.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='West',user=request.user,tier_no=2)
					obj.number=obj.number+form_west.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='West')
					ob.tier2_availability=ob.tier2_availability-form_west.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='West',tier_no=2,user=request.user,number=form_west.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='West')
					ob.tier2_availability=ob.tier2_availability-form_west.cleaned_data.get('tier2_demand')
					ob.save()
			if form_south_west.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='South-West',user=request.user,tier_no=1)
					obj.number=obj.number+form_south_west.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-West')
					ob.tier1_availability=ob.tier1_availability-form_south_west.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='South-West',tier_no=1,user=request.user,number=form_south_west.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-West')
					ob.tier1_availability=ob.tier1_availability-form_south_west.cleaned_data.get('tier1_demand')
					ob.save()
			if form_south_west.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='South-West',user=request.user,tier_no=2)
					obj.number=obj.number+form_south_west.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-West')
					ob.tier2_availability=ob.tier2_availability-form_south_west.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='South-West',tier_no=2,user=request.user,number=form_south_west.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-West')
					ob.tier2_availability=ob.tier2_availability-form_south_west.cleaned_data.get('tier2_demand')
					ob.save()
			if form_south_east.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='South-East',user=request.user,tier_no=1)
					obj.number=obj.number+form_south_east.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-East')
					ob.tier1_availability=ob.tier1_availability-form_south_east.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='South-East',tier_no=1,user=request.user,number=form_south_east.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-East')
					ob.tier1_availability=ob.tier1_availability-form_south_east.cleaned_data.get('tier1_demand')
					ob.save()
			if form_south_east.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='South-East',user=request.user,tier_no=2)
					obj.number=obj.number+form_south_east.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-East')
					ob.tier2_availability=ob.tier2_availability-form_south_east.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='South-East',tier_no=2,user=request.user,number=form_south_east.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='South-East')
					ob.tier2_availability=ob.tier2_availability-form_south_east.cleaned_data.get('tier2_demand')
					ob.save()
			if form_north_west.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='North-West',user=request.user,tier_no=1)
					obj.number=obj.number+form_north_west.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-West')
					ob.tier1_availability=ob.tier1_availability-form_north_west.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='North-West',tier_no=1,user=request.user,number=form_north_west.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-West')
					ob.tier1_availability=ob.tier1_availability-form_north_west.cleaned_data.get('tier1_demand')
					ob.save()
			if form_north_west.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='North-West',user=request.user,tier_no=2)
					obj.number=obj.number+form_north_west.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-West')
					ob.tier2_availability=ob.tier2_availability-form_north_west.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='North-West',tier_no=2,user=request.user,number=form_north_west.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-West')
					ob.tier2_availability=ob.tier2_availability-form_north_west.cleaned_data.get('tier2_demand')
					ob.save()
			if form_north_east.cleaned_data.get('tier1_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='North-east',user=request.user,tier_no=1)
					obj.number=obj.number+form_north_east.cleaned_data.get('tier1_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-east')
					ob.tier1_availability=ob.tier1_availability-form_north_east.cleaned_data.get('tier1_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='North-east',tier_no=1,user=request.user,number=form_north_east.cleaned_data.get('tier1_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-east')
					ob.tier1_availability=ob.tier1_availability-form_north_east.cleaned_data.get('tier1_demand')
					ob.save()
			if form_north_east.cleaned_data.get('tier2_demand')!=0:
				try:
					obj=Tickets.objects.get(match=m,stand='North-east',user=request.user,tier_no=2)
					obj.number=obj.number+form_north_east.cleaned_data.get('tier2_demand')
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-east')
					ob.tier2_availability=ob.tier2_availability-form_north_east.cleaned_data.get('tier2_demand')
					ob.save()
				except :
					obj=Tickets(match=m,stand='North-east',tier_no=2,user=request.user,number=form_north_east.cleaned_data.get('tier2_demand'))
					obj.save()
					ob=Match_book.objects.get(match=m,stand='North-east')
					ob.tier2_availability=ob.tier2_availability-form_north_east.cleaned_data.get('tier2_demand')
					ob.save()
			return redirect('http://127.0.0.1:8000/profile')
		else :
			messages.error(request,'You have requested for more number of tickets than they are avaialble.Please resubmit.')
			return redirect('http://127.0.0.1:8000/book/'+str(id))#check this out
@login_required			
def profile(request):
	tickets=Tickets.objects.filter(user=request.user)
	return render(request,'book/profile.html',{'tickets':tickets})

def delete_ticket(request,s,id,tno):
	m=Match.objects.get(match_no=id)
	obj=Tickets.objects.get(match=m,stand=s,tier_no=tno,user=request.user)
	ob=Match_book.objects.get(match=m,stand=s)
	if tno==1:
		ob.tier1_availability=ob.tier1_availability+obj.number
	else:
		ob.tier2_availability=ob.tier2_availability+obj.number
	ob.save()
	obj.delete()
	return redirect('http://127.0.0.1:8000/profile')

@login_required
def modify(request):
	if request.method=='POST':
		form = Modify_form(request.POST)
		if form.is_valid():
			request.user.profile.last_name = form.cleaned_data.get('last_name')
			request.user.profile.first_name = form.cleaned_data.get('first_name')
			request.user.profile.email = form.cleaned_data.get('email')
			request.user.save()
			return redirect('http://127.0.0.1:8000/profile')
	else :
		form=Modify_form()
		form.fields['first_name'].initial=request.user.profile.first_name
		form.fields['last_name'].initial=request.user.profile.last_name
		form.fields['email'].initial=request.user.profile.email
		return render(request,'book/mod.html',{'form':form})