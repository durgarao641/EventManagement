from django.conf.urls import url
from first import views
 
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^login$', views.login, name='login'),
]
