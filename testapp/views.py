from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404

from testapp.models import Poll
# ...
def index(request):
    return render(request, 'testapp/index.html')
