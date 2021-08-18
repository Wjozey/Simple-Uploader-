from django.contrib import admin
from django.urls import path
from Uploader.views import upload_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_file, name='Upload-home')
]
