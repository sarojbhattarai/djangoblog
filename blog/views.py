from django.shortcuts import render
from .models import Posts



def home(request):
	context = {
		'posts': Posts.objects.all()
			  }
	return render(request,'blog/home.html',context)



def about(request):
	return render(request,'blog/about.html',{'title': 'About'})
	



