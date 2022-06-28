from django.shortcuts import render, redirect 
from .models import *

def index(request):
        _course = Course.objects.all()
        _con = {
            "courses" : _course
        }
        return render(request, "index.html", _con)

def newCourse(request):
    if request.method == 'POST':
        _name = Course.objects.create(
            course_name = request.POST['name'],
            description = request.POST['desc'],
        )
        _name.save()
    
    return redirect('/')

# def dstroy(self, request, id):
#     item_id = request.POST.get('item')
#     items = Items.objects.get(id=item_id)
#     try:
#         Course.objects.filter(id=id).update(item_name=items.name)
#     except:
#         messages.error(request, 'Cannot update')
#     return redirect(reverse("contacts:item_list"))

def delete(request,_id):
    course_id=Course.objects.get(id=_id)
    context={
        'this_course': course_id
    }
    return render(request,'delete.html',context)




def deletethis(request,_id):
    course = Course.objects.get(id=_id)
    course.delete()
    return redirect("/")