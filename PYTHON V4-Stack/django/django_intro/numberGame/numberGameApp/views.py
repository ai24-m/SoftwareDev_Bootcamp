from django.shortcuts import render , redirect 
import random



def index(request): 
  # random.randint(1, 100) 		# random number between 1-100
  return render(request,'game.html')

def show(request):
  # if request.method == 'GET':
  #       return render(request,'game.html')
  _out = ""
  if request.POST['guess']:
  # request.method == 'POST':
  #       request.session['guess'] = request.POST['guess']
        _guess = request.session['guess'] = int(request.POST['guess'])
        _number = request.session['number'] = random.randrange(1,100)
        _newgame = False
        
        if ( _number < _guess):
            #  str(_guess ) + 
            _out =" Too HIGH!! Guess again "
            
        elif(_number  > _guess ):
          # str(_guess ) +
            _out = " Too LOW!! Guess again"
        else:
            
            _out = str(_guess )+ "  : is the Correct number ! "
            _newgame = True

        context ={
          "out" : _out,
          "newgame" : _newgame
        }
  else:
    _Mesage = " Please try to guess number ! "
    context = {
            "noNumberInter" : _Mesage
        }
  return render(request ,'game.html',context )

def newgame(request):
        return redirect('/')



