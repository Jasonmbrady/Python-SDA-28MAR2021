from django.shortcuts import render, redirect
import random
import time
import datetime

#Front Page Routes
def index(request):
    request.session['status'] = "playing"
    return render(request, "index.html")

def set_rules(request):
    #Do Stuff
    request.session['max_moves'] = request.POST['moves']
    request.session['goal_amount'] = request.POST['goal']
    return redirect("/game")

# Game Board Routes
def game(request):
    # context = {}
    if "curr_gold" not in request.session:
        request.session['curr_gold'] = 0
    if "act_log" not in request.session:
        request.session['act_log'] = []
    # if "status" in request.session:
        
    return render(request, "game.html")

def process_money(request):
    location = request.POST['gold']
    if location == "farm":
        earned = random.randint(10,20)
        request.session["curr_gold"] += earned
        request.session["act_log"].append(f"Earned {earned} gold from the {location} ")
    elif location == "cave":
        earned = random.randint(5,10)
        request.session["curr_gold"] += earned
        request.session["act_log"].append(f"Earned {earned} gold from the {location} ")
    elif location == "house":
        earned = random.randint(2,5)
        request.session["curr_gold"] += earned
        request.session["act_log"].append(f"Earned {earned} gold from the {location} ")
    else:
        earned = random.randint(-50, 50)
        request.session["curr_gold"] += earned
        if earned >= 0:
            request.session["act_log"].append(f"Earned {earned} gold from the {location} ")
        else:
            request.session["act_log"].append(f"Entered the Casino and lost {-earned}... Ouch ")
    if "counter" not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    if request.session['curr_gold'] >= int(request.session['goal_amount']):
        request.session['status'] = "victory"
    if request.session['counter'] >= int(request.session['max_moves']):
        request.session['status'] = "defeat"
    return redirect("/game")

# Misc
def clear(request):
    request.session.flush()
    return redirect("/")
