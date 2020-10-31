from testDB.models import SampleModel
from django.shortcuts import render
from .forms import SampleForm
import socket
from .models import SampleModel

def index(request):
  
    title_list = SampleModel.objects.all()
    form = SampleForm
    context = {
        'title_list' : title_list,
        'form': form,
        'hostname': socket.gethostname()
    }

    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            title_added = form.cleaned_data['title'] 
            form.save()
            print(title_added)

    # output = ', '.join([q.title for q in title_list])
    return render(request, 'testDB/index.html', context)