from django.shortcuts import render,HttpResponseRedirect
from .forms import UserForm
from .models import User


# Create your views here.


# This Function will add New data and Show data in table format
def show(request):
    if request.method == 'POST':
        data = UserForm( request.POST )  # data received from user from 'forms.py'.
        if data.is_valid():  # if data is received and valid then-
            name = data.cleaned_data ['name']  # get cleaned data name
            email = data.cleaned_data ["email"]
            contact = data.cleaned_data ['contact']
            reg = User( name = name,email = email,contact = contact )  # saves the data in the fields inside admin panel
            reg.save()  # save the data and render it in the admin panel and SQLite3 Database.
            messages.add_message(request,messages.SUCCESS,"DONE!!..Your account has been created!!")
    else:
        data = UserForm()
    re = User.objects.all()

    return render( request,'show.html',{'form': data,'re': re} )


# This Function will Delete the data from table which is added by the user
def delete(request,id):
    if request.method == "POST":
        delt = User.objects.get( pk = id )
        delt.delete()
        return HttpResponseRedirect( '/' )


# This Function will Edit/Update the data from table which is added by the User
def update_data(request,id):
    if request.method == 'POST':
        up = User.objects.get( pk = id )
        data = UserForm( request.POST,instance = up )
        if data.is_valid():
            data.save()
    else:
        up = User.objects.get( pk = id )
        data = UserForm( instance = up )
    return render( request,'update.html',{'form': data} )
