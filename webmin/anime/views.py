from django.shortcuts import render
from django.http import request
from . import views
from datetime import datetime
from django.utils import timezone
x=datetime.now

# Create your views here.

def my_view(request):
    while True:
        now = timezone.now()
        return {'n':now}
def index(request):
    return render(request, 'animeDashboard.html', {'date':x, 'n':my_view})
