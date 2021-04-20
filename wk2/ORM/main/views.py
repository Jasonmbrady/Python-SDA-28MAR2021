from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "my_book": Book.objects.get(id=1),
    }
    return render(request, "index.html", context)

def add_author(request):
    f_name = request.POST['fname']
    l_name = request.POST['lname']
    Author.objects.create(first_name = f_name, last_name = l_name)
    return redirect("/")