from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('passowrd', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/account/loggedin/')
    else:
        return HttpResponseRedirect('/acoount/invalid/')
		
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/account/loggedout/')
	
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save
            return HttpResponseRedirect('/hello/')
    else:
        form = UserCreationForm()
    return render_to_response('registration/register.html', {'form': form,}, context_instance=RequestContext(request))
