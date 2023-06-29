from django.shortcuts import render, redirect
from .models import Url
import uuid
from django.http import HttpResponse



def index(request):
    return render(request, 'index.html',{})


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_detail = Url.objects.get(uuid=pk)
    return redirect(url_detail.link)



