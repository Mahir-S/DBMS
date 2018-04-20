from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'book/home.html',)
	#return render(request,'book/home.html')