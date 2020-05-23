from django.urls import include, path

app_name = 'django-violations'

urlpatterns = [
    path('threads/', include('apps.threads.urls', namespace='threads')),
]
