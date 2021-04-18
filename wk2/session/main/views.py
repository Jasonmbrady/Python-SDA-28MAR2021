from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def get_user(request):
    if request.method == "POST":
        request.session['username'] = request.POST['username']
        return redirect("/display_user")
    else:
        return redirect("/")

def display_user(request):
    return render(request, "user.html")

def make_box(request):
    # print(request.session['boxcolor'])
    if "boxcolor" in request.session:
        request.session['boxcolor'].append(request.POST['color'])
        request.session.save()
        print([request.session['boxcolor']])
    else:
        request.session['boxcolor'] = [request.POST['color']]
        print([request.session['boxcolor']])
    return redirect("/")

def clear(request):
    request.session['boxcolor'] = []
    return redirect("/")