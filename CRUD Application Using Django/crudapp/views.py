from django.shortcuts import render,HttpResponseRedirect

from .forms import StudRegistation
from .models import User

# Create your views here.


#this function add new item and show item

def add_shownew(request):
    if request.method=='POST':

        fs=StudRegistation(request.POST)
        if fs.is_valid:
            fs=StudRegistation(request.POST)
            #nm=fs.cleaned_data['name']
            #em=fs.cleaned_data['email']
            #pw=fs.cleaned_data['password']
            #reg89=User(name=nm,email=em,password=pw)
            #reg89.save()
            fs.save()
            fs=StudRegistation()

    else:

        fs=StudRegistation()

    stud=User.objects.all()

    return render(request,'base/addandshow.html',context={'form':fs,'stud1':stud})
#---------------------------------------------------#

#this function will delete

def delete_data(request,id):

    if request.method=='POST':

        pi=User.objects.get(pk=id)

        pi.delete()


    return HttpResponseRedirect('/')

#this finction will delete

def update_data(request,id):

    if request.method=='POST':

        pi=User.objects.get(pk=id)
        fs=StudRegistation(request.POST,instance=pi)

        if fs.is_valid:

            fs.save()
            fs=StudRegistation()
            
            

    else:
        pi=User.objects.get(pk=id)
        fs=StudRegistation(instance=pi)

    return render(request,'base/updatedata.html',{'form':fs})
