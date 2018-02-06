from django.conf.urls import url
from first import views
 
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^events$', views.login, name='login'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^create_event$', views.create_event, name='create_event'),
]
