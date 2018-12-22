from django.shortcuts import render

posts = [
	{
	 'author': 'Saroj Bhattarai',
	 'title': 'Django Project 1',
	 'content': 'First Project ',
	 'date_posted':'Dec-22-2018'
	},
	{
	 'author': 'Dell Computer',
	 'title':'Django Project 2',
	 'content': 'Dell Project ',
	 'date_posted':'Dec-23-2018'
	}

]

def home(request):
	context = {
		'posts': posts
		}
	return render(request,'blog/home.html',context)



def about(request):
	return render(request,'blog/about.html',{'title': 'About'})
	



