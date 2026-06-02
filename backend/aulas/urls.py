from django.urls import path
from . import views

urlpatterns = [
    path('carreras/', views.CarreraMixin.as_view()),
    path('profesores/<int:pk>/', views.ProfesorMixinDetail.as_view()),
]