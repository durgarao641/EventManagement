from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
 
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def login(request):
	if request.method == "POST":
		print(request.POST['name'])
		print(request.POST['password'])
		role = verify_user(request.POST['name'], request.POST['password'])
		if role == 'admin':
			return render(request, 'dashboard.html', {'result': {'name': request.POST['name'], 'events': get_events()}})
		else:
			return render(request, 'dashboard.html', {'result': {'name': request.POST['name'], 'events': get_events()}})
	return render(request, 'index.html')

def dashboard(request):
	return render(request, 'dashboard.html', {'result': {'events': get_events()}})

def create_event(request):
	return render(request, 'create_event.html')

def get_events():
	events = [
		{'name': 'ICC Cricket World cup', 'date': '25-feb-2018', 'organisors':'durga'},
		{'name': 'FIFA', 'date': '10-mar-2018', 'organisors':'suresh'},
		{'name': 'ICC Cricket World cup', 'date': '25-feb-2018', 'organisors':'durga'},
		{'name': 'FIFA', 'date': '10-mar-2018', 'organisors':'suresh'}
	]
	return events

def verify_user(username, password):
	if username == 'durga':
		return 'admin'
	else:
		return 'organizor'

