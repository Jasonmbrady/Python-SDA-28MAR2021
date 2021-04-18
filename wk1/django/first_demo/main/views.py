from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def success(request, num):
    return HttpResponse(f"I have succeeded! {num}")

def one_more(request, id, color):
    return HttpResponse(f"{id} {color}")

def one_method(request):
    return redirect("/")

def form_handler(request):
    if request.method == "POST":
        words[0] = request.POST["stuff"]
    return redirect("/")