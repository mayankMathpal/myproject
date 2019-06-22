from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from .serializer import demoserialzer
from rest_framework  import viewsets
from django.views.generic import View
from .forms import formdata
# Create your views here.


def ok(request):
    form = formdata()
    return render(request, 'index.html', {'form': form})