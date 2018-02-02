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
		return render(request, 'login.html', {'result': request.POST['name']})
	return render(request, 'index.html')