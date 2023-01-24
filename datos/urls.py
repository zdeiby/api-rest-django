from django.urls import path
from django.contrib import admin
from .views import companyListView 



urlpatterns = [
    path('',companyListView.as_view()),
    path('<int:id>', companyListView.as_view())

]
