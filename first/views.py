import uuid
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from first.models import Users, Events
from django.views.decorators.csrf import csrf_protect
 
# Create your views here.

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
			return render(request, 'dashboard.html', {'result': {'name': request.POST['name'], 'events': get_events(), 'organizors': get_organizors()}})
		else:
			return render(request, 'organizer.html', {'result': {'name': request.POST['name'], 'events': get_events(), 'organizors': get_organizors()}})
	return render(request, 'index.html')

def dashboard(request):
	return render(request, 'dashboard.html', {'result': {'events': get_events(), 'organizors': get_organizors()}})

@csrf_protect
def create_event(request):
	if request.method == 'POST':
		Events(uuid.uuid4(), request.POST['eventname'], request.POST['eventdate'], ''.join(request.POST.getlist('orgs[]'))).save()
		return HttpResponseRedirect('dashboard', {'result': {'events': get_events(), 'organizors': get_organizors()}})

def get_events():
	events = []
	for event in Events.objects.all():
		events.append(
			{'eventid': event.event_id, 'name': event.name,
			'date': event.date, 'organisors': event.organizors}
		)
	return events

def get_organizors():
	organizors = []
	for user in Users.objects.filter(role='organizor'):
		organizors.append(user.username)
	return organizors

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