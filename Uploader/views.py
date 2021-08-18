from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import FileFieldModel

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = FileFieldModel(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'Uploader/upload.html', {'form': form})