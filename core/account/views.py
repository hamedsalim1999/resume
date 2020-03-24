from django.shortcuts import render,redirect
from django.contrib.auth import login , authenticate
from django.contrib.forms import UserCrationForm
from django.views.generic import CreateView


class Singup(CreateView):
    model = User
    from_class = UserCrationForm

    def form_calid(self,form):
        from.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('passwords')
        user = authenticate(username = username , password = password)

        login(self.request , user)
        return redirect('home')

