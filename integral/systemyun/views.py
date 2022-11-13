from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
import requests

# Create your views here.
def hello(request):

    return render(request,'index.html')
    #return render(request,'dddd.html')

def query(request):
    user_list_obj = models.integral.objects.all()
    return render(request, 't1.html', {'li': user_list_obj})