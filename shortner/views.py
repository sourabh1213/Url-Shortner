from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())
        new_link = Url(link=url, uuid=uid)
        new_link.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid = pk)
    return redirect('https://'+url_details.link)
