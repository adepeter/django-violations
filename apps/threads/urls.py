from django.urls import path

app_name = 'threads'

from . import views

urlpatterns = [
    path('<int:pk>/', views.read_thread, name='read_thread'),
    path('<int:pk>/report/', views.report_thread, name='report_thread'),
]