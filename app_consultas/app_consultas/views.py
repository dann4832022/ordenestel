from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeDoneView

def inicio(request):
    template_name = "inicio.html"
    return render(request, template_name)

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'