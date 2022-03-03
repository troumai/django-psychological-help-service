from django.contrib import admin
from django.urls import path, include
from therapists_list import views

urlpatterns = [
    path('', views.therapists_list, name='therapists'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.TherapistsDetailView.as_view(), name='therapists_detail'),
    path('<int:pk>/update', views.TherapistsUpdateView.as_view(), name='therapist_update'),
    path('<int:pk>/delete', views.TherapistsDeleteView.as_view(), name='therapist_delete'),
]