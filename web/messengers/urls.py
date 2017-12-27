from django.urls import path

from . import views

app_name = "messengers"


urlpatterns = [
    path('', views.index, name='index'),
    path('996930e44ffd5292014e1460f72517f2355e1fa114f1ab5268/', views.WebHookView.as_view()),
]
