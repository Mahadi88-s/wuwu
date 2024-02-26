from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('wertWeRt34ek', views.index, name='index'),
    path('signin', views.signin, name='signin'),

]

urlpatterns = format_suffix_patterns(urlpatterns)