from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from first.models import Users
 
# Create your views here.
events = [
		{'name': 'ICC Cricket World cup', 'date': '25-feb-2018', 'organisors':'durga'},
		{'name': 'FIFA', 'date': '10-mar-2018', 'organisors':'suresh'},
		{'name': 'ICC Cricket World cup', 'date': '25-feb-2018', 'organisors':'durga'},
		{'name': 'FIFA', 'date': '10-mar-2018', 'organisors':'suresh'}
	]

organizors = [
		'durga', 'suresh', 'krishna', 'tiger', 'chaithanya'
	]
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def login(request):
	if request.method == "POST":
		print(request.POST['name'])
		print(request.POST['password'])
		role = verify_user(request.POST['name'], request.POST['password'])
		if role == 'error':
			return render(request, 'index.html', {'error': 'login errors'})
		if role == 'admin':
			return render(request, 'dashboard.html', {'result': {'name': request.POST['name'], 'events': get_events(), 'organizors': organizors}})
		else:
			return render(request, 'organizer.html', {'result': {'name': request.POST['name'], 'events': get_events(), 'organizors': organizors}})
	return render(request, 'index.html')

def dashboard(request):
	return render(request, 'dashboard.html', {'result': {'events': get_events()}})

def create_event(request):
	return render(request, 'create_event.html')

def get_events():
		return events

def verify_user(username, password):
	try:
		user = Users.objects.get(username=username, password=password)
		print(user)
	except:
		return 'error'
	else:
   		return user.role
		

def add_student(request):
    print (request.GET)
    return render(request, 'demo.html', {'result': {'students': get_students()}})

def get_students():
	students = ["sureshbabu", "durga", "sivaram", "krishna", "xyz", "zyx"]
	return students