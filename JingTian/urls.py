from django.urls import path
from JingTian import views
urlpatterns = [
    path('', views.login,name = 'login'),
]
