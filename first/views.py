from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
 
events = [
	{'name': 'ICC Cricket World cup', 'date': '25-feb-2018', 'organisors':'durga'},
	{'name': 'FIFA', 'date': '10-mar-2018', 'organisors':'suresh'}
]

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def login(request):
	if request.method == "POST":
		print(request.POST['name'])
		print(request.POST['password'])
		return render(request, 'dashboard.html', {'result': {'name': request.POST['name'], 'events': events}})
	return render(request, 'index.html')