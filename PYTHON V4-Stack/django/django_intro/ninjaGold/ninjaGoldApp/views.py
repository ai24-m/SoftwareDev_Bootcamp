from django.shortcuts import render, redirect
import random
from datetime import datetime

def root(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []

    context = {
        'gold': request.session['gold'], 
        'messages': request.session['activity'],
            }
    return render(request, 'index.html', context)

def processMoney(request):
    now = datetime.now()
    if 'farm' in request.POST:
        place = 'Farm'
        earned = random.randint(10,20)
    if 'cave' in request.POST:
        place = 'Cave'
        earned = random.randint(10,20)
    if 'house' in request.POST:
        place = 'House'
        earned = random.randint(10,20)
    if 'quest' in request.POST:
        place = "Quest"
        earned = random.randint(-50,50)

    request.session['gold'] = request.session['gold'] + earned 
    time= now.strftime('(%Y/%m/%d | %-I:%M %p)')

    if earned < 0:
        message = 'You failed a '+ place + ' ,and lost ' + str(earned*-1) + ' gold.....Ouch'+ time
    else:
        message = 'You entered a '+ place + ' ,and earned ' + str(earned) + ' gold' + time

    request.session['activity'].append(message)
    return redirect("/")

def destroy(request):
    del  request.session['gold']
    del request.session['activity']
    return redirect("/")