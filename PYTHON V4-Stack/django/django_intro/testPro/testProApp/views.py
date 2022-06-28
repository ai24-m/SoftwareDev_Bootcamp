from django.shortcuts import render, redirect
import random, datetime

def index(request):

    return render(request, 'index.html', context)

def root(request):

    return redirect("/")

# def index(request):
#     if not 'gold' in request.session:
#         request.session['gold'] = 0
#         request.session['messages'] = []
#     context = {'gold': request.session['gold'], 'messages': request.session['messages']}
#     return render(request, 'index.html', context)

# def processMoney(request):
#     if request.method == "POST":
#         directory = {'farm': [10,20],'cave': [5,10],'house': [2,5],'casino': [-50,50]}
#         now = datetime.datetime.now()

#         for key in directory:
#             if key == request.POST['location']:
#                 temp = random.randint(directory[key][0], directory[key][1])
#                 request.session['gold'] += temp
#                 if temp >= 0:
#                     request.session['messages'].insert(0,'Earned '+ str(temp) + ' golds from the ' + key + '! ('+now.strftime("%Y/%m/%d %I:%M %p")+')')
#                 else:
#                     request.session['messages'].insert(0,'Entered a ' + key + ' and lost '+ str(temp*-1) + ' golds... Ouch.. ('+now.strftime("%Y/%m/%d %I:%M %p")+')')
#     return redirect("/")

# def destroy(request):
#     request.session.clear()
#     return redirect("/")


# from django.shortcuts import render, redirect
# import random
# from datetime import datetime

# def root(request):
#     if 'gold' not in request.session:
#         request.session['gold'] = 0
#     if 'activity' not in request.session:
#         request.session['activity'] = []

#     context = {
#         'gold': request.session['gold'],
#         'activities': request.session['activity'],
#         }
#     return render(request, 'index.html', context)

# def process(request):
#     # if request.method == "POST":
#     now = datetime.now()
#     if 'farm' in request.POST:
#         place = 'Farm'
#         earned = random.randint(10,20)
#     if 'cave' in request.POST:
#         place = 'Cave'
#         earned = random.randint(10,20)
#     if 'house' in request.POST:
#         place = 'House'
#         earned = random.randint(10,20)
#     if 'quest' in request.POST:
#         place = "Quest"
#         earned = random.randint(-50,50)

#     request.session['gold'] = request.session['gold'] + earned 
#     time= now.strftime('(%Y/%m/%d | %-I:%M %p)')

#     if earned < 0:
#         message = 'You failed a '+ place + ' ,and lost ' + str(earned*-1) + ' gold.....Ouch'+ time
#     else:
#         message = 'You entered a '+ place + ' ,and earned ' + str(earned) + ' gold' + time

#     request.session['activity'].append(message)

#     return redirect('/') 

# def reset(request):
#     del  request.session['gold']
#     del request.session['activity']
#     return redirect('/')



# from django.shortcuts import render, redirect
# import random
# from datetime import datetime

# def root(request):
#     if 'gold' not in request.session:
#         request.session['gold'] = 0
#     if 'activity' not in request.session:
#         request.session['activity'] = []

#     context = {
#         'gold': request.session['gold'],
#         'activities': request.session['activity'],
#         }
#     return render(request, 'index.html', context)

# def process(request):
#     # if request.method == "POST":
#     now = datetime.now()
#     if 'farm' in request.POST:
#         place = 'Farm'
#         earned = random.randint(10,20)
#     if 'cave' in request.POST:
#         place = 'Cave'
#         earned = random.randint(10,20)
#     if 'house' in request.POST:
#         place = 'House'
#         earned = random.randint(10,20)
#     if 'quest' in request.POST:
#         place = "Quest"
#         earned = random.randint(-50,50)

#     request.session['gold'] = request.session['gold'] + earned 
#     time= now.strftime('(%Y/%m/%d | %-I:%M %p)')

#     if earned < 0:
#         message = 'You failed a '+ place + ' ,and lost ' + str(earned*-1) + ' gold.....Ouch'+ time
#     else:
#         message = 'You entered a '+ place + ' ,and earned ' + str(earned) + ' gold' + time

#     request.session['activity'].append(message)

#     return redirect('/') 

# def reset(request):
#     del  request.session['gold']
#     del request.session['activity']
#     return redirect('/')