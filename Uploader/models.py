from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class FileFieldModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to = user_directory_path)


    
    def __str__(self):
		    return self.title
