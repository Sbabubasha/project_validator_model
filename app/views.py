from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.


def model(request):
    MTO=Topicforms()
    d={'MTO': MTO}
    if request.method=='POST':
        TMO=Topicforms(request.POST)
        if TMO.is_valid():
            TMO.save()
            return HttpResponse('data is valid')
        else:
            return HttpResponse('data id notvalid')
        
    return render(request,'model.html',d)