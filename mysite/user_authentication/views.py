from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


from user_authentication.forms import SignUpForm

class TestView(TemplateView):
    def get_context_data(self):
        context = super().get_context_data()
        context['articles'] = [{'one': 'blah'}, {'two': 'ahhh'}]
        return context
    def get_template_names(self):
        return 'test_template.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/blog')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})